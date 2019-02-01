#! python3
# -*- coding: utf-8 -*-

import tcp_client
import protocol.login_pb2
import protocol.cmd
import log


class LoginClient(tcp_client.TcpClient):
    def __init__(self, user, args, cfg):
        tcp_client.TcpClient.__init__(self, self)
        self.user = user
        self.cfg = cfg
        self.args = args

    def init_cmds(self):
        self.cmds[protocol.cmd.LOGIN] = self.on_login_msg

    def login(self):
        if self.connect("登录", self.cfg["addr"], self.cfg["port"]) is False:
            return False
        log.info("开始发送登陆协议。 account: {0}".format(self.user.account))
        msg = protocol.login_pb2.MSG_LOGIN()
        msg.Account = self.user.account
        msg.Password = self.user.password
        self.send(protocol.cmd.LOGIN, msg)
        return True

    def on_login_msg(self, data):
        msg = protocol.login_pb2.MSG_LOGIN_RESULT()
        msg.ParseFromString(data)
        log.info("登陆结果。 Err: {0}, Token: {1}, Address: {2}, Port: {3}, NodeTyps: {4}, account: {5}".format(
            msg.Err, msg.Token, msg.Address, msg.Port, msg.NodeTyps, self.user.account))
        self.user.gateway_client.token = msg.Token
        for i in range(len(msg.NodeTyps)):
            if msg.NodeTyps[i] == 3:
                self.user.gateway_client.address = msg.Address[i]
                self.user.gateway_client.port = msg.Port[i]
                break
        if msg.Err == 0:
            self.user.gateway_client.verify_token()
        else:
            log.error("登录失败，account: {0}", self.user.account)
