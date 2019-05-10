# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: match.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import lobby_custom_pb2 as lobby__custom__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='match.proto',
  package='protocol',
  syntax='proto3',
  serialized_pb=_b('\n\x0bmatch.proto\x12\x08protocol\x1a\x12lobby_custom.proto\">\n\tCMD_MATCH\"1\n\x04\x45NUM\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05MATCH\x10\x01\x12\x11\n\x0cMSGCMDOFFSET\x10\x88\'\";\n\x17\x45NUM_MATCH_COMMON_ERROR\" \n\x04\x45NUM\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0cSYSTEM_ERROR\x10\x01\"!\n\x0fMSG_MATCH_MATCH\x12\x0e\n\x06RoleID\x18\x01 \x01(\x04\"v\n\x16MSG_MATCH_MATCH_RESULT\x12\x33\n\x03\x45rr\x18\x01 \x01(\x0e\x32&.protocol.ENUM_MATCH_COMMON_ERROR.ENUM\x12\'\n\x05Roles\x18\x02 \x03(\x0b\x32\x18.protocol.ROLE_BASE_INFOb\x06proto3')
  ,
  dependencies=[lobby__custom__pb2.DESCRIPTOR,])



_CMD_MATCH_ENUM = _descriptor.EnumDescriptor(
  name='ENUM',
  full_name='protocol.CMD_MATCH.ENUM',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MATCH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSGCMDOFFSET', index=2, number=5000,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=58,
  serialized_end=107,
)
_sym_db.RegisterEnumDescriptor(_CMD_MATCH_ENUM)

_ENUM_MATCH_COMMON_ERROR_ENUM = _descriptor.EnumDescriptor(
  name='ENUM',
  full_name='protocol.ENUM_MATCH_COMMON_ERROR.ENUM',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM_ERROR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=136,
  serialized_end=168,
)
_sym_db.RegisterEnumDescriptor(_ENUM_MATCH_COMMON_ERROR_ENUM)


_CMD_MATCH = _descriptor.Descriptor(
  name='CMD_MATCH',
  full_name='protocol.CMD_MATCH',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CMD_MATCH_ENUM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=107,
)


_ENUM_MATCH_COMMON_ERROR = _descriptor.Descriptor(
  name='ENUM_MATCH_COMMON_ERROR',
  full_name='protocol.ENUM_MATCH_COMMON_ERROR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENUM_MATCH_COMMON_ERROR_ENUM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=168,
)


_MSG_MATCH_MATCH = _descriptor.Descriptor(
  name='MSG_MATCH_MATCH',
  full_name='protocol.MSG_MATCH_MATCH',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RoleID', full_name='protocol.MSG_MATCH_MATCH.RoleID', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=203,
)


_MSG_MATCH_MATCH_RESULT = _descriptor.Descriptor(
  name='MSG_MATCH_MATCH_RESULT',
  full_name='protocol.MSG_MATCH_MATCH_RESULT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Err', full_name='protocol.MSG_MATCH_MATCH_RESULT.Err', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Roles', full_name='protocol.MSG_MATCH_MATCH_RESULT.Roles', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=323,
)

_CMD_MATCH_ENUM.containing_type = _CMD_MATCH
_ENUM_MATCH_COMMON_ERROR_ENUM.containing_type = _ENUM_MATCH_COMMON_ERROR
_MSG_MATCH_MATCH_RESULT.fields_by_name['Err'].enum_type = _ENUM_MATCH_COMMON_ERROR_ENUM
_MSG_MATCH_MATCH_RESULT.fields_by_name['Roles'].message_type = lobby__custom__pb2._ROLE_BASE_INFO
DESCRIPTOR.message_types_by_name['CMD_MATCH'] = _CMD_MATCH
DESCRIPTOR.message_types_by_name['ENUM_MATCH_COMMON_ERROR'] = _ENUM_MATCH_COMMON_ERROR
DESCRIPTOR.message_types_by_name['MSG_MATCH_MATCH'] = _MSG_MATCH_MATCH
DESCRIPTOR.message_types_by_name['MSG_MATCH_MATCH_RESULT'] = _MSG_MATCH_MATCH_RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CMD_MATCH = _reflection.GeneratedProtocolMessageType('CMD_MATCH', (_message.Message,), dict(
  DESCRIPTOR = _CMD_MATCH,
  __module__ = 'match_pb2'
  # @@protoc_insertion_point(class_scope:protocol.CMD_MATCH)
  ))
_sym_db.RegisterMessage(CMD_MATCH)

ENUM_MATCH_COMMON_ERROR = _reflection.GeneratedProtocolMessageType('ENUM_MATCH_COMMON_ERROR', (_message.Message,), dict(
  DESCRIPTOR = _ENUM_MATCH_COMMON_ERROR,
  __module__ = 'match_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ENUM_MATCH_COMMON_ERROR)
  ))
_sym_db.RegisterMessage(ENUM_MATCH_COMMON_ERROR)

MSG_MATCH_MATCH = _reflection.GeneratedProtocolMessageType('MSG_MATCH_MATCH', (_message.Message,), dict(
  DESCRIPTOR = _MSG_MATCH_MATCH,
  __module__ = 'match_pb2'
  # @@protoc_insertion_point(class_scope:protocol.MSG_MATCH_MATCH)
  ))
_sym_db.RegisterMessage(MSG_MATCH_MATCH)

MSG_MATCH_MATCH_RESULT = _reflection.GeneratedProtocolMessageType('MSG_MATCH_MATCH_RESULT', (_message.Message,), dict(
  DESCRIPTOR = _MSG_MATCH_MATCH_RESULT,
  __module__ = 'match_pb2'
  # @@protoc_insertion_point(class_scope:protocol.MSG_MATCH_MATCH_RESULT)
  ))
_sym_db.RegisterMessage(MSG_MATCH_MATCH_RESULT)


# @@protoc_insertion_point(module_scope)
