#! python3

import wx
import config
import user
import login_window
import log

if __name__ == "__main__":
    args, cfg = config.load_config()
    usr = user.User(args, cfg).init()
    log.init(cfg["logfile"])
    app = wx.App(False)
    login_window.new(usr, args, cfg)
    app.MainLoop()
