# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buildstream/v2/source.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

from buildstream._protos.build.bazel.remote.execution.v2 import (
    remote_execution_pb2 as build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2,
)
from buildstream._protos.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='buildstream/v2/source.proto',
  package='buildstream.v2',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1b\x62uildstream/v2/source.proto\x12\x0e\x62uildstream.v2\x1a\x36\x62uild/bazel/remote/execution/v2/remote_execution.proto\x1a\x1cgoogle/api/annotations.proto\"Q\n\x06Source\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x36\n\x05\x66iles\x18\x02 \x01(\x0b\x32\'.build.bazel.remote.execution.v2.Digest\"<\n\x10GetSourceRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x11\n\tcache_key\x18\x02 \x01(\t\"g\n\x13UpdateSourceRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x11\n\tcache_key\x18\x02 \x01(\t\x12&\n\x06source\x18\x03 \x01(\x0b\x32\x16.buildstream.v2.Source2\xa7\x01\n\rSourceService\x12G\n\tGetSource\x12 .buildstream.v2.GetSourceRequest\x1a\x16.buildstream.v2.Source\"\x00\x12M\n\x0cUpdateSource\x12#.buildstream.v2.UpdateSourceRequest\x1a\x16.buildstream.v2.Source\"\x00\x62\x06proto3'
  ,
  dependencies=[build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='buildstream.v2.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='buildstream.v2.Source.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='buildstream.v2.Source.files', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=133,
  serialized_end=214,
)


_GETSOURCEREQUEST = _descriptor.Descriptor(
  name='GetSourceRequest',
  full_name='buildstream.v2.GetSourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='buildstream.v2.GetSourceRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cache_key', full_name='buildstream.v2.GetSourceRequest.cache_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=216,
  serialized_end=276,
)


_UPDATESOURCEREQUEST = _descriptor.Descriptor(
  name='UpdateSourceRequest',
  full_name='buildstream.v2.UpdateSourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='buildstream.v2.UpdateSourceRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cache_key', full_name='buildstream.v2.UpdateSourceRequest.cache_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='buildstream.v2.UpdateSourceRequest.source', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=278,
  serialized_end=381,
)

_SOURCE.fields_by_name['files'].message_type = build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2._DIGEST
_UPDATESOURCEREQUEST.fields_by_name['source'].message_type = _SOURCE
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.message_types_by_name['GetSourceRequest'] = _GETSOURCEREQUEST
DESCRIPTOR.message_types_by_name['UpdateSourceRequest'] = _UPDATESOURCEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'buildstream.v2.source_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.Source)
  })
_sym_db.RegisterMessage(Source)

GetSourceRequest = _reflection.GeneratedProtocolMessageType('GetSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSOURCEREQUEST,
  '__module__' : 'buildstream.v2.source_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.GetSourceRequest)
  })
_sym_db.RegisterMessage(GetSourceRequest)

UpdateSourceRequest = _reflection.GeneratedProtocolMessageType('UpdateSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESOURCEREQUEST,
  '__module__' : 'buildstream.v2.source_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.UpdateSourceRequest)
  })
_sym_db.RegisterMessage(UpdateSourceRequest)



_SOURCESERVICE = _descriptor.ServiceDescriptor(
  name='SourceService',
  full_name='buildstream.v2.SourceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=384,
  serialized_end=551,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSource',
    full_name='buildstream.v2.SourceService.GetSource',
    index=0,
    containing_service=None,
    input_type=_GETSOURCEREQUEST,
    output_type=_SOURCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateSource',
    full_name='buildstream.v2.SourceService.UpdateSource',
    index=1,
    containing_service=None,
    input_type=_UPDATESOURCEREQUEST,
    output_type=_SOURCE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SOURCESERVICE)

DESCRIPTOR.services_by_name['SourceService'] = _SOURCESERVICE

# @@protoc_insertion_point(module_scope)
