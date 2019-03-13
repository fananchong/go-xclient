
#! python3

import protocol.login_pb2
import protocol.gateway_pb2
import protocol.lobby_pb2

# login server
LOGIN = protocol.login_pb2._CMD_LOGIN_ENUM.values_by_name["LOGIN"].number

# gateway server
VERIFY_TOKEN = protocol.gateway_pb2._CMD_GATEWAY_ENUM.values_by_name["VERIFY_TOKEN"].number

# lobby server
LOBBY_MSGCMDOFFSET = protocol.lobby_pb2._CMD_LOBBY_ENUM.values_by_name["MSGCMDOFFSET"].number
LOGIN_LOBBY = LOBBY_MSGCMDOFFSET + \
    protocol.lobby_pb2._CMD_LOBBY_ENUM.values_by_name["LOGIN"].number
CREATE_ROLE = LOBBY_MSGCMDOFFSET + \
    protocol.lobby_pb2._CMD_LOBBY_ENUM.values_by_name["CREATE_ROLE"].number
ENTER_GAME = LOBBY_MSGCMDOFFSET + \
    protocol.lobby_pb2._CMD_LOBBY_ENUM.values_by_name["ENTER_GAME"].number
CHAT = LOBBY_MSGCMDOFFSET + \
    protocol.lobby_pb2._CMD_LOBBY_ENUM.values_by_name["CHAT"].number
