#! python3
# -*- coding: utf-8 -*-

import protocol.lobby_pb2
import protocol.lobby_custom_pb2
import protocol.cmd
import log
from server_type import *


class LobbyClient():
    def __init__(self, user, args, cfg):
        self.user = user
        self.cfg = cfg
        self.args = args
        self.cmds = {}

    def init(self):
        self.init_cmds()

    def init_cmds(self):
        self.cmds[protocol.cmd.QUERY_ROLELIST] = self.on_query_rolelist_msg

    def login(self):
        log.info("开始请求角色列表协议。 account: {0}".format(self.user.account))
        msg = protocol.lobby_pb2.MSG_LOBBY_QUERY_ROLELIST()
        self.send(protocol.cmd.QUERY_ROLELIST, msg)

    def on_query_rolelist_msg(self, data):
        msg = protocol.lobby_pb2.MSG_LOBBY_QUERY_ROLELIST_RESULT()
        msg.ParseFromString(data)
        log.info("请求角色列表结果。 Err: {0}, account: {1}".format(
            msg.Err, self.user.account))

    def on_recv(self, cmd, data):
        if cmd in self.cmds:
            self.cmds[cmd](data)
        else:
            log.error("[大厅] 未处理的消息。 cmd: {0}, account: {1}".format(
                cmd, self.user.account))

    def send(self, cmd, msg):
        self.user.clients[ServerType.Gateway].send(cmd, msg)

    def close(self):
        pass
