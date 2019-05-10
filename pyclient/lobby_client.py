#! python3
# -*- coding: utf-8 -*-

import protocol.lobby_pb2
import protocol.lobby_custom_pb2
import protocol.cmd
import log
from server_type import *
import lobby_window
import login_window
import wx
import role


class LobbyClient():
    def __init__(self, user, args, cfg):
        self.user = user
        self.cfg = cfg
        self.args = args
        self.cmds = {}
        self.address = ""
        self.port = 0

    def init(self):
        self.init_cmds()

    def init_cmds(self):
        self.cmds[protocol.cmd.LOGIN_LOBBY] = self.on_login_msg
        self.cmds[protocol.cmd.CREATE_ROLE] = self.on_create_role_msg
        self.cmds[protocol.cmd.ENTER_GAME] = self.on_enter_game_msg
        self.cmds[protocol.cmd.CHAT] = self.on_chat_msg

    def login(self):
        log.info("开始请求角色列表协议。 account: {0}".format(self.user.account))
        msg = protocol.lobby_pb2.MSG_LOBBY_LOGIN()
        self.send(protocol.cmd.LOGIN_LOBBY, msg)

    def on_login_msg(self, data):
        msg = protocol.lobby_pb2.MSG_LOBBY_LOGIN_RESULT()
        msg.ParseFromString(data)
        log.info("请求角色列表结果。 Err: {0}, account: {1}".format(
            msg.Err, self.user.account))
        if msg.Err == 0:
            for index in range(0, len(msg.Roles)):
                log.info("\t\t角色{0}: {1}".format(index, msg.Roles[index]))
            if msg.Roles[self.user.current_role_index].RoleID == 0:
                self.create_role()
            else:
                self.enter_game()

    def create_role(self):
        log.info("开始请求创建角色。 account: {0}, current_role_index: {1}".format(
            self.user.account, self.user.current_role_index))
        msg = protocol.lobby_pb2.MSG_LOBBY_CREATE_ROLE()
        msg.Slot = self.user.current_role_index
        msg.Info.RoleName = self.user.account+"_rolename"
        self.send(protocol.cmd.CREATE_ROLE, msg)

    def on_create_role_msg(self, data):
        msg = protocol.lobby_pb2.MSG_LOBBY_CREATE_ROLE_RESULT()
        msg.ParseFromString(data)
        log.info("请求创建角色结果。 Err: {0}, account: {1}".format(
            msg.Err, self.user.account))
        if msg.Err == 0:
            self.enter_game()

    def enter_game(self):
        log.info("开始请求进入游戏。 account: {0}, current_role_index: {1}".format(
            self.user.account, self.user.current_role_index))
        msg = protocol.lobby_pb2.MSG_LOBBY_ENTER_GAME()
        msg.Slot = self.user.current_role_index
        self.send(protocol.cmd.ENTER_GAME, msg)

    def on_enter_game_msg(self, data):
        msg = protocol.lobby_pb2.MSG_LOBBY_ENTER_GAME_RESULT()
        msg.ParseFromString(data)
        log.info("请求进入游戏结果。 Err: {0}, account: {1}".format(
            msg.Err, self.user.account))
        if msg.Err == 0:
            self.user.current_role = role.Role(self.args, self.cfg)
            self.user.current_role.id = msg.DetailInfo.BaseInfo.RoleID
            self.user.current_role.name = msg.DetailInfo.BaseInfo.RoleName
            log.info("账号: {0}, 角色ID: {1}, 角色名: {2}".format(
                self.user.account, self.user.current_role.id, self.user.current_role.name))
            login_window.close(1)
            wx.CallAfter(lobby_window.new, self.user, self.args, self.cfg)

    def chat(self, to, txt):
        log.info("开始发送聊天协议。 account: {0}".format(self.user.account))
        msg = protocol.lobby_pb2.MSG_LOBBY_CHAT()
        msg.To = to
        msg.Txt = txt
        self.send(protocol.cmd.CHAT, msg)

    def on_chat_msg(self, data):
        msg = protocol.lobby_pb2.MSG_LOBBY_CHAT()
        msg.ParseFromString(data)
        log.info("收到聊天消息。 From: {0}, To: {1}, Txt: {2}".format(
            msg.From, msg.To, msg.Txt))
        lobby_window.get().add_chat_history(msg.From, msg.To, msg.Txt)

    def match(self):
        log.info("开始发送匹配协议。 account: {0}".format(self.user.account))
        msg = protocol.lobby_pb2.MSG_LOBBY_MATCH()
        self.send(protocol.cmd.MATCH, msg)

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
