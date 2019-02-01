#! python3
# -*- coding: utf-8 -*-

import socket
import log
import protocol.message
import threading


class TcpClient:
    def __init__(self, derive):
        self.derive = derive
        self.name = ""
        self.sock = None
        self.thread_recv_data = None
        self.thread_recv_data_flag = "terminate"
        self.left_data = b""
        self.cmds = {}
        self.derive.init_cmds()

    def connect(self, name, addr, port):
        log.info("开始连接{3}服务器。 addr: {0}, port: {1}, account: {2}".format(
            addr, port, self.derive.user.account, name))
        self.name = name
        self.close()
        self.left_data = b""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((addr, int(port)))
            log.info("连接{3}服务器成功。 addr: {0}, port: {1}, account: {2}".format(
                addr, port, self.derive.user.account, name))
            #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self.thread_recv_data_flag = "start"
            self.thread_recv_data = threading.Thread(
                target=self.__thread_recv_data)
            self.thread_recv_data.start()
        except Exception as e:
            log.info(e)
            return False
        return True

    def send(self, cmd, msg):
        data = msg.SerializeToString()
        protomsg = protocol.message.pack(cmd, data)
        if self.sock is not None:
            self.sock.send(protomsg)
        else:
            log.error("[{2}] TCP连接已关闭，消息未发送成功。 cmd: {0}, account: {1}".format(
                cmd, self.derive.user.account, self.name))

    def on_recv(self, data):
        msgs = protocol.message.on_recv(self, data)
        if len(msgs) == 0:
            return
        for (cmd, data) in msgs:
            if cmd in self.cmds:
                self.cmds[cmd](data)
            else:
                log.error("[{2}] 未处理的消息。 cmd: {0}, account: {1}".format(
                    cmd, self.derive.user.account, self.name))

    def close(self):
        if self.sock is not None:
            self.sock.close()
            self.sock = None
        if self.thread_recv_data is not None:
            self.thread_recv_data_flag = "terminate"
            self.thread_recv_data.join()
            self.thread_recv_data = None

    def __thread_recv_data(self):
        log.info("[{1}] 开启 TCP 接收数据线程。account: {0}".format(
            self.derive.user.account, self.name))
        while self.thread_recv_data_flag == "start":
            data = None
            try:
                BUFSIZ = 128 * 1024
                data = self.sock.recv(BUFSIZ)
                if data is None or len(data) == 0:
                    self.sock.close()
                    self.sock = None
                    break
            except Exception as e:
                log.error(e)
                if self.sock is not None:
                    self.sock.close()
                    self.sock = None
                log.info("[{1}] 关闭 TCP 接收数据线程。account: {0}".format(
                    self.derive.user.account, self.name))
                return
            self.on_recv(data)
        log.info("[{1}] 关闭 TCP 接收数据线程。account: {0}".format(
            self.derive.user.account, self.name))
