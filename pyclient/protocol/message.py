#! python3
# -*- coding: utf-8 -*-

import struct
import hashlib
from enum import Enum
import zlib

'''
数据块格式
  * 3个字节 数据块大小
  * 1个字节标志位： 0未压缩；1 zlib压缩
  * 数据块：2个字节消息ID；剩余protobuf消息块
'''

DATA0_LEN = 6
CMD_LEN = 2


def unpack_header(rawdata):
    l1, l2, l3, flag, cmd = struct.unpack("<BBBBH", rawdata[:DATA0_LEN])
    l = l1 + (l2 << 8) + (l3 << 16)
    return l, flag, cmd


def unpack(rawdata):
    l, flag, cmd = unpack_header(rawdata)
    data = rawdata[DATA0_LEN:]
    if l != len(data) + CMD_LEN:  # len = cmd + data
        print("flag=", flag, "cmd=", cmd, "l=", l, " len(data)=", len(data))
        exit(1)
    return cmd, data


def pack(cmd, data):
    l = len(data) + CMD_LEN
    l1 = l & 0xFF
    l2 = (l >> 8) & 0xFF
    l3 = (l >> 16) & 0xFF
    flag = 0
    return struct.pack("<BBBBH", l1, l2, l3, flag, cmd) + data


def on_recv(client, data):
    msgs = []
    if len(data) == 0:
        return msgs

    left_data = client.left_data
    rawdata = left_data + data
    while True:
        if len(rawdata) > DATA0_LEN:
            l, flag, cmd = unpack_header(rawdata)
            data = rawdata[DATA0_LEN:]
            if l <= len(data) + CMD_LEN:
                if flag == 1:
                    msgs.append((cmd, zlib.decompress(data[:l - CMD_LEN])))
                else:
                    msgs.append((cmd, data[:l - CMD_LEN]))
                rawdata = data[l - CMD_LEN:]
            else:
                break
        else:
            break
    left_data = rawdata
    client.left_data = left_data
    return msgs
