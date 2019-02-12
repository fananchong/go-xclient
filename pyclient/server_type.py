#! python3

import enum


class ServerType(enum.Enum):
    Login = 1
    Gateway = 2
    Lobby = 3
