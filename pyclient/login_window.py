#! python3
# -*- coding: utf-8 -*-

import wx
import hashlib


class LoginWindow(wx.Frame):
    def __init__(self, user, args, cfg):
        wx.Frame.__init__(self, None, style=wx.CAPTION | wx.CLOSE_BOX)
        self.user = user
        self.cfg = cfg
        self.args = args
        self.close_flag = 0
        self.init()

    def init(self):
        self.SetTitle(self.cfg["title"] + " - 登录")
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        w = 240
        h = 160
        self.SetMaxSize((w, h))
        self.SetMinSize((w, h))
        self.SetSize((w, h))
        self.init_window()
        self.Bind(wx.EVT_BUTTON, self.OnLogin, self.btnLogin)
        self.Centre()

    def init_window(self):
        wx.StaticText(self, -1, "账号：", pos=wx.Point(30, 15))
        self.txtAccount = wx.TextCtrl(
            self, -1, pos=(100, 15), size=(100, -1), value=self.cfg["login"]["account"])
        wx.StaticText(self, -1, "密码：", pos=wx.Point(30, 45))
        self.txtPassword = wx.TextCtrl(
            self, -1, pos=(100, 45), size=(100, -1), value=self.cfg["login"]["password"])
        self.btnLogin = wx.Button(self, -1, "登陆", pos=(70, 90), size=(100, 25))

    def OnLogin(self, evt):
        account = self.txtAccount.GetValue()
        password = self.txtPassword.GetValue()
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        password = m.hexdigest()
        self.user.login(account, password)

    def OnClose(self, evt):
        if self.close_flag == 0:
            self.user.close()
        evt.Skip()


g_win = None


def new(user, args, cfg):
    global g_win
    g_win = LoginWindow(user, args, cfg)
    g_win.Show()


def close(flag):
    global g_win
    g_win.close_flag = flag
    g_win.Close()
    g_win = None
