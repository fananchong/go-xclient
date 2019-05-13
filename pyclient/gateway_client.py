#! python3
# -*- coding: utf-8 -*-

import tcp_client
import protocol.gateway_pb2
import protocol.cmd
import log
from server_type import *


class GatewayClient(tcp_client.TcpClient):
    def __init__(self, user, args, cfg):
        tcp_client.TcpClient.__init__(self, self)
        self.user = user
        self.cfg = cfg
        self.args = args
        self.address = ""
        self.port = 0
        self.ID = 0
        self.token = ""

    def init_cmds(self):
        self.cmds[protocol.cmd.VERIFY_TOKEN] = self.on_verify_token_msg
        self.default_cmd_hander = self.user.clients[ServerType.Lobby].on_recv

    def verify_token(self):
        if self.connect("网关", self.address, self.port) is False:
            return False
        log.info("开始发送令牌验证协议。 account: {0}".format(self.user.account))
        msg = protocol.gateway_pb2.MSG_GATEWAY_VERIFY_TOKEN()
        msg.Account = self.user.account
        msg.Token = self.token
        self.send(protocol.cmd.VERIFY_TOKEN, msg)
        return True

    def on_verify_token_msg(self, data):
        msg = protocol.gateway_pb2.MSG_GATEWAY_VERIFY_TOKEN_RESULT()
        msg.ParseFromString(data)
        log.info("令牌验证结果。 Err: {0}, account: {1}".format(
            msg.Err, self.user.account))
        if msg.Err == 0:
            self.user.clients[ServerType.Lobby].login()
        else:
            log.error("令牌验证失败")
