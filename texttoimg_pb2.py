# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: texttoimg.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'texttoimg.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftexttoimg.proto\x12\ntext2image\"\x1e\n\x0cImageRequest\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"F\n\rImageResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x14\n\x0cimage_base64\x18\x03 \x01(\t2Y\n\x11Text2ImageService\x12\x44\n\rGenerateImage\x12\x18.text2image.ImageRequest\x1a\x19.text2image.ImageResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'texttoimg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IMAGEREQUEST']._serialized_start=31
  _globals['_IMAGEREQUEST']._serialized_end=61
  _globals['_IMAGERESPONSE']._serialized_start=63
  _globals['_IMAGERESPONSE']._serialized_end=133
  _globals['_TEXT2IMAGESERVICE']._serialized_start=135
  _globals['_TEXT2IMAGESERVICE']._serialized_end=224
# @@protoc_insertion_point(module_scope)
