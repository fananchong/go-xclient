#! python3
# -*- coding: utf-8 -*-

import wx
import protocol.lobby_pb2
import log
from server_type import *

W = 600
H = 400


class LobbyWindow(wx.Frame):
    def __init__(self, user, args, cfg):
        wx.Frame.__init__(self, None, style=wx.CAPTION | wx.CLOSE_BOX)
        self.user = user
        self.cfg = cfg
        self.args = args
        self.init()

    def init(self):
        self.SetTitle(self.cfg["title"] + " - 大厅")
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.SetClientSize((W, H))
        self.init_window()
        self.Centre()

    def init_window(self):
        (w, h) = self.GetClientSize()

        # 角色信息区
        panelTopH = 50
        panelTop = wx.Panel(self, -1, (1, 1), (w-2, panelTopH-2))
        wx.StaticText(panelTop, -1, "账号：", (30, 15))
        wx.StaticText(panelTop, -1, self.user.account,  (70, 15))
        wx.StaticText(panelTop, -1, "角色ID：", (120, 15))
        wx.StaticText(panelTop, -1, str(self.user.current_role.id), (170, 15))
        wx.StaticText(panelTop, -1, "角色名：", (210, 15))
        wx.StaticText(panelTop, -1, self.user.current_role.name, (260, 15))

        # 聊天区
        panelChatH = 180
        panelChat = wx.Panel(
            self, -1, (1, h - panelChatH+1), (w-2, panelChatH-2))
        wx.StaticText(panelChat, -1, "聊天对象：", (30, 15))
        self.chatTo = wx.TextCtrl(panelChat, -1, "", (100, 15))
        wx.StaticText(panelChat, -1, "聊天内容：", (230, 15))
        self.chatTxt = wx.TextCtrl(panelChat, -1, "", (300, 15), (w - 440, 25))
        binChat = wx.Button(panelChat, -1, "发送", (w - 120, 15))
        self.Bind(wx.EVT_BUTTON, self.OnChat, binChat)
        self.chatHistory = wx.TextCtrl(
            panelChat, -1, "", (30, 50), (w - 62, panelChatH - 60))
        self.chatHistory.Enabled = False

        # 功能区
        panelFunction = wx.Panel(
            self, -1, (1, panelTopH), (w-2, h - panelTopH - panelChatH))
        binMatch = wx.Button(panelFunction, -1, "开始匹配",
                             (0, 0), panelFunction.GetSize())
        self.Bind(wx.EVT_BUTTON, self.OnMatch, binMatch)

    def OnChat(self, evt):
        to = self.chatTo.GetValue()
        txt = self.chatTxt.GetValue()
        self.user.clients[ServerType.Lobby].chat(to, txt)

    def OnMatch(self, evt):
        pass

    def OnClose(self, evt):
        self.user.close()
        evt.Skip()


g_win = None


def new(user, args, cfg):
    global g_win
    g_win = LobbyWindow(user, args, cfg)
    g_win.Show()
