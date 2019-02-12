#! python3
# -*- coding: utf-8 -*-

import wx


class LobbyWindow(wx.Frame):
    def __init__(self, user, args, cfg):
        wx.Frame.__init__(self, None, style=wx.CAPTION | wx.CLOSE_BOX)
        self.user = user
        self.cfg = cfg
        self.args = args
        self.init()

    def init(self):
        self.SetTitle(self.cfg["title"])
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        w = 240
        h = 160
        self.SetMaxSize((w, h))
        self.Centre()

    def OnClose(self, evt):
        self.user.close()
        evt.Skip()


g_win = None


def new(user, args, cfg):
    global g_win
    g_win = LobbyWindow(user, args, cfg)
    g_win.Show()
