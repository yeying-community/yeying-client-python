# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yeying/api/apps/zuoyepigai/message.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 28, 1, "", "yeying/api/apps/zuoyepigai/message.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yeying.api.common import message_pb2 as yeying_dot_api_dot_common_dot_message__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yeying.api.apps.zuoyepigai import meta_pb2 as yeying_dot_api_dot_apps_dot_zuoyepigai_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n(yeying/api/apps/zuoyepigai/message.proto\x12\x1ayeying.api.apps.zuoyepigai\x1a\x1fyeying/api/common/message.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a%yeying/api/apps/zuoyepigai/meta.proto"\x88\x01\n\x12MessageListRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12@\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x32.yeying.api.apps.zuoyepigai.MessageListRequestBody"w\n\x16MessageListRequestBody\x12.\n\tpageIndex\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\x08pageSize\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value"\x8a\x01\n\x13MessageListResponse\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12\x41\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x33.yeying.api.apps.zuoyepigai.MessageListResponseBody"\x96\x01\n\x17MessageListResponseBody\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.yeying.api.common.ResponseStatus\x12\x39\n\x04list\x18\x02 \x03(\x0b\x32+.yeying.api.apps.zuoyepigai.MessageMetadata\x12\r\n\x05total\x18\x03 \x01(\x04"|\n\x0c\x43ountRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12:\n\x04\x62ody\x18\x02 \x01(\x0b\x32,.yeying.api.apps.zuoyepigai.CountRequestBody"\x12\n\x10\x43ountRequestBody"~\n\rCountResponse\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12;\n\x04\x62ody\x18\x02 \x01(\x0b\x32-.yeying.api.apps.zuoyepigai.CountResponseBody"\x7f\n\x11\x43ountResponseBody\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.yeying.api.common.ResponseStatus\x12\x37\n\x04meta\x18\x02 \x03(\x0b\x32).yeying.api.apps.zuoyepigai.CountMetadata",\n\rCountMetadata\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05"~\n\rListByRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12;\n\x04\x62ody\x18\x02 \x01(\x0b\x32-.yeying.api.apps.zuoyepigai.ListByRequestBody"1\n\x11ListByRequestBody\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05"\x80\x01\n\x0eListByResponse\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12<\n\x04\x62ody\x18\x02 \x01(\x0b\x32..yeying.api.apps.zuoyepigai.ListByResponseBody"\x91\x01\n\x12ListByResponseBody\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.yeying.api.common.ResponseStatus\x12\x39\n\x04meta\x18\x02 \x03(\x0b\x32+.yeying.api.apps.zuoyepigai.MessageMetadata\x12\r\n\x05\x63ount\x18\x03 \x01(\x05"\x86\x01\n\x11MarkAsReadRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12?\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x31.yeying.api.apps.zuoyepigai.MarkAsReadRequestBody"$\n\x15MarkAsReadRequestBody\x12\x0b\n\x03uid\x18\x01 \x01(\t"\x88\x01\n\x12MarkAsReadResponse\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12@\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x32.yeying.api.apps.zuoyepigai.MarkAsReadResponseBody"K\n\x16MarkAsReadResponseBody\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.yeying.api.common.ResponseStatus2\xa6\x03\n\x07Message\x12i\n\x04List\x12..yeying.api.apps.zuoyepigai.MessageListRequest\x1a/.yeying.api.apps.zuoyepigai.MessageListResponse"\x00\x12^\n\x05\x43ount\x12(.yeying.api.apps.zuoyepigai.CountRequest\x1a).yeying.api.apps.zuoyepigai.CountResponse"\x00\x12\x61\n\x06ListBy\x12).yeying.api.apps.zuoyepigai.ListByRequest\x1a*.yeying.api.apps.zuoyepigai.ListByResponse"\x00\x12m\n\nMarkAsRead\x12-.yeying.api.apps.zuoyepigai.MarkAsReadRequest\x1a..yeying.api.apps.zuoyepigai.MarkAsReadResponse"\x00\x42\x1cZ\x1ayeying/api/apps/zuoyepigaib\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "yeying.api.apps.zuoyepigai.message_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z\032yeying/api/apps/zuoyepigai"
    _globals["_MESSAGELISTREQUEST"]._serialized_start = 177
    _globals["_MESSAGELISTREQUEST"]._serialized_end = 313
    _globals["_MESSAGELISTREQUESTBODY"]._serialized_start = 315
    _globals["_MESSAGELISTREQUESTBODY"]._serialized_end = 434
    _globals["_MESSAGELISTRESPONSE"]._serialized_start = 437
    _globals["_MESSAGELISTRESPONSE"]._serialized_end = 575
    _globals["_MESSAGELISTRESPONSEBODY"]._serialized_start = 578
    _globals["_MESSAGELISTRESPONSEBODY"]._serialized_end = 728
    _globals["_COUNTREQUEST"]._serialized_start = 730
    _globals["_COUNTREQUEST"]._serialized_end = 854
    _globals["_COUNTREQUESTBODY"]._serialized_start = 856
    _globals["_COUNTREQUESTBODY"]._serialized_end = 874
    _globals["_COUNTRESPONSE"]._serialized_start = 876
    _globals["_COUNTRESPONSE"]._serialized_end = 1002
    _globals["_COUNTRESPONSEBODY"]._serialized_start = 1004
    _globals["_COUNTRESPONSEBODY"]._serialized_end = 1131
    _globals["_COUNTMETADATA"]._serialized_start = 1133
    _globals["_COUNTMETADATA"]._serialized_end = 1177
    _globals["_LISTBYREQUEST"]._serialized_start = 1179
    _globals["_LISTBYREQUEST"]._serialized_end = 1305
    _globals["_LISTBYREQUESTBODY"]._serialized_start = 1307
    _globals["_LISTBYREQUESTBODY"]._serialized_end = 1356
    _globals["_LISTBYRESPONSE"]._serialized_start = 1359
    _globals["_LISTBYRESPONSE"]._serialized_end = 1487
    _globals["_LISTBYRESPONSEBODY"]._serialized_start = 1490
    _globals["_LISTBYRESPONSEBODY"]._serialized_end = 1635
    _globals["_MARKASREADREQUEST"]._serialized_start = 1638
    _globals["_MARKASREADREQUEST"]._serialized_end = 1772
    _globals["_MARKASREADREQUESTBODY"]._serialized_start = 1774
    _globals["_MARKASREADREQUESTBODY"]._serialized_end = 1810
    _globals["_MARKASREADRESPONSE"]._serialized_start = 1813
    _globals["_MARKASREADRESPONSE"]._serialized_end = 1949
    _globals["_MARKASREADRESPONSEBODY"]._serialized_start = 1951
    _globals["_MARKASREADRESPONSEBODY"]._serialized_end = 2026
    _globals["_MESSAGE"]._serialized_start = 2029
    _globals["_MESSAGE"]._serialized_end = 2451
# @@protoc_insertion_point(module_scope)
