
#! python3

import protocol.login_pb2
import protocol.gateway_pb2

LOGIN = protocol.login_pb2._CMD_LOGIN_ENUM.values_by_name["LOGIN"].index
VERIFY_TOKEN = protocol.gateway_pb2._CMD_GATEWAY_ENUM.values_by_name["VERIFY_TOKEN"].index
