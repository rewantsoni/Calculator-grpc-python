# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator-grpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator-grpc.proto',
  package='main',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x63\x61lculator-grpc.proto\x12\x04main\"\x12\n\x03num\x12\x0b\n\x03num\x18\x01 \x01(\x03\")\n\x07twoNums\x12\x0e\n\x06numOne\x18\x01 \x01(\x03\x12\x0e\n\x06numTwo\x18\x02 \x01(\x03\x32\x89\x01\n\x03\x61pi\x12\x1f\n\x03\x61\x64\x64\x12\r.main.twoNums\x1a\t.main.num\x12\x1f\n\x03sub\x12\r.main.twoNums\x1a\t.main.num\x12\x1f\n\x03mul\x12\r.main.twoNums\x1a\t.main.num\x12\x1f\n\x03\x64iv\x12\r.main.twoNums\x1a\t.main.numb\x06proto3')
)




_NUM = _descriptor.Descriptor(
  name='num',
  full_name='main.num',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='main.num.num', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=49,
)


_TWONUMS = _descriptor.Descriptor(
  name='twoNums',
  full_name='main.twoNums',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numOne', full_name='main.twoNums.numOne', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numTwo', full_name='main.twoNums.numTwo', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['num'] = _NUM
DESCRIPTOR.message_types_by_name['twoNums'] = _TWONUMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

num = _reflection.GeneratedProtocolMessageType('num', (_message.Message,), dict(
  DESCRIPTOR = _NUM,
  __module__ = 'calculator_grpc_pb2'
  # @@protoc_insertion_point(class_scope:main.num)
  ))
_sym_db.RegisterMessage(num)

twoNums = _reflection.GeneratedProtocolMessageType('twoNums', (_message.Message,), dict(
  DESCRIPTOR = _TWONUMS,
  __module__ = 'calculator_grpc_pb2'
  # @@protoc_insertion_point(class_scope:main.twoNums)
  ))
_sym_db.RegisterMessage(twoNums)



_API = _descriptor.ServiceDescriptor(
  name='api',
  full_name='main.api',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=95,
  serialized_end=232,
  methods=[
  _descriptor.MethodDescriptor(
    name='add',
    full_name='main.api.add',
    index=0,
    containing_service=None,
    input_type=_TWONUMS,
    output_type=_NUM,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='sub',
    full_name='main.api.sub',
    index=1,
    containing_service=None,
    input_type=_TWONUMS,
    output_type=_NUM,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='mul',
    full_name='main.api.mul',
    index=2,
    containing_service=None,
    input_type=_TWONUMS,
    output_type=_NUM,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='div',
    full_name='main.api.div',
    index=3,
    containing_service=None,
    input_type=_TWONUMS,
    output_type=_NUM,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['api'] = _API

# @@protoc_insertion_point(module_scope)