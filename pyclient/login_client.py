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
        if self.connect(self.cfg["addr"], self.cfg["port"]) == False:
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