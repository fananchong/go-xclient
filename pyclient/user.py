#! python3

import login_client
import gateway_client
import lobby_client
from server_type import *


class User():
    def __init__(self, args, cfg):
        self.args = args
        self.cfg = cfg
        self.clients = {}
        self.account = ""
        self.password = ""
        self.current_role_index = 0
        self.current_role = None

    def init(self):
        self.clients[ServerType.Login] = login_client.LoginClient(
            self, self.args, self. cfg)
        self.clients[ServerType.Gateway] = gateway_client.GatewayClient(
            self, self.args, self. cfg)
        self.clients[ServerType.Lobby] = lobby_client.LobbyClient(
            self, self.args, self. cfg)

        for client in self.clients.values():
            client.init()
        return self

    def login(self, account, password):
        self.account = account
        self.password = password
        self.clients[ServerType.Login].login()

    def close(self):
        for client in self.clients.values():
            client.close()
