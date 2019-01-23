#! python3

import login_client


class User():
    def __init__(self, args, cfg):
        self.args = args
        self.cfg = cfg
        self.login_client = login_client.LoginClient(self, args, cfg)
        self.account = ""
        self.password = ""

    def login(self, account, password):
        self.account = account
        self.password = password
        self.login_client.login()

    def close(self):
        self.login_client.close()
