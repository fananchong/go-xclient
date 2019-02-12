#! python3
# -*- coding: utf-8 -*-

import protocol.lobby_pb2
import protocol.lobby_custom_pb2
import protocol.cmd
import log


class LobbyClient():
    def __init__(self, user, args, cfg):
        self.user = user
        self.cfg = cfg
        self.args = args

    def init_cmds(self):
        pass

    def close(self):
        pass
