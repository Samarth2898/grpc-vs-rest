# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: labsix.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0clabsix.proto\"\x1e\n\x06\x61\x64\x64Msg\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\"\x1a\n\x0brawImageMsg\x12\x0b\n\x03img\x18\x01 \x01(\x0c\"%\n\rdotProductMsg\x12\t\n\x01\x61\x18\x01 \x03(\x02\x12\t\n\x01\x62\x18\x02 \x03(\x02\"\x1b\n\x0cjsonImageMsg\x12\x0b\n\x03img\x18\x01 \x01(\t\"\x17\n\x08\x61\x64\x64Reply\x12\x0b\n\x03sum\x18\x01 \x01(\x05\"%\n\x0f\x64otProductReply\x12\x12\n\ndotproduct\x18\x01 \x01(\x02\"+\n\nimageReply\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x32\xd0\x01\n\x06labSix\x12%\n\rAddTwoNumbers\x12\x07.addMsg\x1a\t.addReply\"\x00\x12\x33\n\x14GetRawImageDimensons\x12\x0c.rawImageMsg\x1a\x0b.imageReply\"\x00\x12\x33\n\rGetDotProduct\x12\x0e.dotProductMsg\x1a\x10.dotProductReply\"\x00\x12\x35\n\x15GetJsonImageDimensons\x12\r.jsonImageMsg\x1a\x0b.imageReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'labsix_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ADDMSG']._serialized_start=16
  _globals['_ADDMSG']._serialized_end=46
  _globals['_RAWIMAGEMSG']._serialized_start=48
  _globals['_RAWIMAGEMSG']._serialized_end=74
  _globals['_DOTPRODUCTMSG']._serialized_start=76
  _globals['_DOTPRODUCTMSG']._serialized_end=113
  _globals['_JSONIMAGEMSG']._serialized_start=115
  _globals['_JSONIMAGEMSG']._serialized_end=142
  _globals['_ADDREPLY']._serialized_start=144
  _globals['_ADDREPLY']._serialized_end=167
  _globals['_DOTPRODUCTREPLY']._serialized_start=169
  _globals['_DOTPRODUCTREPLY']._serialized_end=206
  _globals['_IMAGEREPLY']._serialized_start=208
  _globals['_IMAGEREPLY']._serialized_end=251
  _globals['_LABSIX']._serialized_start=254
  _globals['_LABSIX']._serialized_end=462
# @@protoc_insertion_point(module_scope)
