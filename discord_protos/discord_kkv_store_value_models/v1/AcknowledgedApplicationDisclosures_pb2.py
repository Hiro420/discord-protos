# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: discord_kkv_store_value_models/v1/AcknowledgedApplicationDisclosures.proto
# Protobuf Python Version: 5.29.3
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
    3,
    '',
    'discord_kkv_store_value_models/v1/AcknowledgedApplicationDisclosures.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJdiscord_kkv_store_value_models/v1/AcknowledgedApplicationDisclosures.proto\x12\x30\x64iscord_protos.discord_kkv_store_value_models.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa6\x05\n\"AcknowledgedApplicationDisclosures\x12\x91\x01\n\x11\x61\x63ked_disclosures\x18\x01 \x03(\x0b\x32v.discord_protos.discord_kkv_store_value_models.v1.AcknowledgedApplicationDisclosures.AcknowledgedApplicationDisclosure\x1a\xed\x01\n!AcknowledgedApplicationDisclosure\x12\x87\x01\n\x0f\x64isclosure_type\x18\x01 \x01(\x0e\x32n.discord_protos.discord_kkv_store_value_models.v1.AcknowledgedApplicationDisclosures.ApplicationDisclosureType\x12\x31\n\x08\x61\x63ked_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x42\x0b\n\t_acked_at\"\xfb\x01\n\x19\x41pplicationDisclosureType\x12\x36\n2APPLICATION_DISCLOSURE_TYPE_UNSPECIFIED_DISCLOSURE\x10\x00\x12+\n\'APPLICATION_DISCLOSURE_TYPE_IP_LOCATION\x10\x01\x12\x37\n3APPLICATION_DISCLOSURE_TYPE_DISPLAYS_ADVERTISEMENTS\x10\x02\x12@\n<APPLICATION_DISCLOSURE_TYPE_PARTNER_SDK_DATA_SHARING_MESSAGE\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'discord_kkv_store_value_models.v1.AcknowledgedApplicationDisclosures_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ACKNOWLEDGEDAPPLICATIONDISCLOSURES']._serialized_start=194
  _globals['_ACKNOWLEDGEDAPPLICATIONDISCLOSURES']._serialized_end=872
  _globals['_ACKNOWLEDGEDAPPLICATIONDISCLOSURES_ACKNOWLEDGEDAPPLICATIONDISCLOSURE']._serialized_start=381
  _globals['_ACKNOWLEDGEDAPPLICATIONDISCLOSURES_ACKNOWLEDGEDAPPLICATIONDISCLOSURE']._serialized_end=618
  _globals['_ACKNOWLEDGEDAPPLICATIONDISCLOSURES_APPLICATIONDISCLOSURETYPE']._serialized_start=621
  _globals['_ACKNOWLEDGEDAPPLICATIONDISCLOSURES_APPLICATIONDISCLOSURETYPE']._serialized_end=872
# @@protoc_insertion_point(module_scope)
