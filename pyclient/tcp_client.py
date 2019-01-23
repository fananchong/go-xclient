#! python3
# -*- coding: utf-8 -*-

import socket
import log
import protocol.message
import threading


class TcpClient:
    def __init__(self, derive):
        self.derive = derive
        self.sock = None
        self.thread_recv_data = None
        self.thread_recv_data_flag = "terminate"
        self.left_data = b""
        self.cmds = {}
        self.derive.init_cmds()

    def connect(self, addr, port):
        log.info("开始连接登陆服务器。 addr: {0}, port: {1}, account: {2}".format(
            addr, port, self.derive.user.account))
        self.close()
        self.left_data = b""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((addr, int(port)))
            log.info("连接登陆服务器成功。 addr: {0}, port: {1}, account: {2}".format(
                addr, port, self.derive.user.account))
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
        if self.sock != None:
            self.sock.send(protomsg)
        else:
            log.error("TCP连接已关闭，消息未发送成功。 cmd: {0}, account: {1}".format(
                cmd, self.derive.user.account))

    def on_recv(self, data):
        msgs = protocol.message.on_recv(self, data)
        if len(msgs) == 0:
            return
        for (cmd, data) in msgs:
            if cmd in self.cmds:
                self.cmds[cmd](data)
            else:
                log.error("未处理的消息。 cmd: {0}, account: {1}".format(
                    cmd, self.derive.user.account))

    def close(self):
        if self.sock != None:
            self.sock.close()
            self.sock = None
        if self.thread_recv_data != None:
            self.thread_recv_data_flag = "terminate"
            self.thread_recv_data.join()
            self.thread_recv_data = None

    def __thread_recv_data(self):
        log.info("开启 TCP 接收数据线程。account: {0}".format(self.derive.user.account))
        while self.thread_recv_data_flag == "start":
            data = None
            try:
                BUFSIZ = 128 * 1024
                data = self.sock.recv(BUFSIZ)
            except Exception as e:
                log.error(e)
                self.sock = None
                log.info("关闭 TCP 接收数据线程。account: {0}".format(
                    self.derive.user.account))
                return
            if data != None:
                self.on_recv(data)
        log.info("关闭 TCP 接收数据线程。account: {0}".format(self.derive.user.account))
