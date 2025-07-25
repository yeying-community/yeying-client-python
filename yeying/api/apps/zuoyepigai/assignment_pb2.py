# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yeying/api/apps/zuoyepigai/assignment.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 28, 1, "", "yeying/api/apps/zuoyepigai/assignment.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yeying.api.common import message_pb2 as yeying_dot_api_dot_common_dot_message__pb2
from yeying.api.apps.zuoyepigai import imagecontent_pb2 as yeying_dot_api_dot_apps_dot_zuoyepigai_dot_imagecontent__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n+yeying/api/apps/zuoyepigai/assignment.proto\x12\x1ayeying.api.apps.zuoyepigai\x1a\x1fyeying/api/common/message.proto\x1a-yeying/api/apps/zuoyepigai/imagecontent.proto"\x92\x01\n\x17\x41ssignmentUploadRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12\x45\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x37.yeying.api.apps.zuoyepigai.AssignmentUploadRequestBody"\xb4\x01\n\x1b\x41ssignmentUploadRequestBody\x12\x0b\n\x03\x64id\x18\x01 \x01(\t\x12\x0f\n\x07\x66ileUrl\x18\x02 \x03(\t\x12\x0f\n\x07taskUid\x18\x03 \x01(\t\x12>\n\x04type\x18\x04 \x01(\x0e\x32\x30.yeying.api.apps.zuoyepigai.ImageContentTypeEnum\x12\x0f\n\x07subject\x18\x05 \x01(\t\x12\x15\n\rtestPaperName\x18\x06 \x01(\t"\x94\x01\n\x18\x41ssignmentUploadResponse\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12\x46\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x38.yeying.api.apps.zuoyepigai.AssignmentUploadResponseBody"a\n\x1c\x41ssignmentUploadResponseBody\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.yeying.api.common.ResponseStatus\x12\x0e\n\x06result\x18\x02 \x01(\t"\x96\x01\n\x19\x41ssignmentBigModelRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12G\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x39.yeying.api.apps.zuoyepigai.AssignmentBigModelRequestBody"1\n\x1d\x41ssignmentBigModelRequestBody\x12\x10\n\x08question\x18\x01 \x01(\t"\x98\x01\n\x1a\x41ssignmentBigModelResponse\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12H\n\x04\x62ody\x18\x02 \x01(\x0b\x32:.yeying.api.apps.zuoyepigai.AssignmentBigModelResponseBody"c\n\x1e\x41ssignmentBigModelResponseBody\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.yeying.api.common.ResponseStatus\x12\x0e\n\x06result\x18\x02 \x01(\t"\x9a\x01\n\x1b\x41ssignmentArtificialRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12I\n\x04\x62ody\x18\x02 \x01(\x0b\x32;.yeying.api.apps.zuoyepigai.AssignmentArtificialRequestBody"2\n\x1f\x41ssignmentArtificialRequestBody\x12\x0f\n\x07\x66ileUrl\x18\x01 \x01(\t"\x9c\x01\n\x1c\x41ssignmentArtificialResponse\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12J\n\x04\x62ody\x18\x02 \x01(\x0b\x32<.yeying.api.apps.zuoyepigai.AssignmentArtificialResponseBody"e\n AssignmentArtificialResponseBody\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.yeying.api.common.ResponseStatus\x12\x0e\n\x06result\x18\x02 \x01(\t"\x8c\x01\n\x14StudentActionRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12\x42\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x34.yeying.api.apps.zuoyepigai.StudentActionRequestBody"H\n\x18StudentActionRequestBody\x12\x0f\n\x07taskUid\x18\x01 \x01(\t\x12\x0b\n\x03\x64id\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t"\x8e\x01\n\x15StudentActionResponse\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12\x43\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x35.yeying.api.apps.zuoyepigai.StudentActionResponseBody"N\n\x19StudentActionResponseBody\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.yeying.api.common.ResponseStatus"\x9a\x01\n\x1b\x41ssignmentCorrectionRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12I\n\x04\x62ody\x18\x02 \x01(\x0b\x32;.yeying.api.apps.zuoyepigai.AssignmentCorrectionRequestBody"-\n\x1f\x41ssignmentCorrectionRequestBody\x12\n\n\x02qa\x18\x01 \x01(\t"\x9c\x01\n\x1c\x41ssignmentCorrectionResponse\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .yeying.api.common.MessageHeader\x12J\n\x04\x62ody\x18\x02 \x01(\x0b\x32<.yeying.api.apps.zuoyepigai.AssignmentCorrectionResponseBody"e\n AssignmentCorrectionResponseBody\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.yeying.api.common.ResponseStatus\x12\x0e\n\x06result\x18\x02 \x01(\t2\x91\x05\n\nAssignment\x12u\n\x06Upload\x12\x33.yeying.api.apps.zuoyepigai.AssignmentUploadRequest\x1a\x34.yeying.api.apps.zuoyepigai.AssignmentUploadResponse"\x00\x12\x83\x01\n\x10\x42igModelGenerate\x12\x35.yeying.api.apps.zuoyepigai.AssignmentBigModelRequest\x1a\x36.yeying.api.apps.zuoyepigai.AssignmentBigModelResponse"\x00\x12\x89\x01\n\x12\x41rtificialGenerate\x12\x37.yeying.api.apps.zuoyepigai.AssignmentArtificialRequest\x1a\x38.yeying.api.apps.zuoyepigai.AssignmentArtificialResponse"\x00\x12v\n\rStudentAction\x12\x30.yeying.api.apps.zuoyepigai.StudentActionRequest\x1a\x31.yeying.api.apps.zuoyepigai.StudentActionResponse"\x00\x12\x81\x01\n\nCorrection\x12\x37.yeying.api.apps.zuoyepigai.AssignmentCorrectionRequest\x1a\x38.yeying.api.apps.zuoyepigai.AssignmentCorrectionResponse"\x00\x42\x1cZ\x1ayeying/api/apps/zuoyepigaib\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "yeying.api.apps.zuoyepigai.assignment_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z\032yeying/api/apps/zuoyepigai"
    _globals["_ASSIGNMENTUPLOADREQUEST"]._serialized_start = 156
    _globals["_ASSIGNMENTUPLOADREQUEST"]._serialized_end = 302
    _globals["_ASSIGNMENTUPLOADREQUESTBODY"]._serialized_start = 305
    _globals["_ASSIGNMENTUPLOADREQUESTBODY"]._serialized_end = 485
    _globals["_ASSIGNMENTUPLOADRESPONSE"]._serialized_start = 488
    _globals["_ASSIGNMENTUPLOADRESPONSE"]._serialized_end = 636
    _globals["_ASSIGNMENTUPLOADRESPONSEBODY"]._serialized_start = 638
    _globals["_ASSIGNMENTUPLOADRESPONSEBODY"]._serialized_end = 735
    _globals["_ASSIGNMENTBIGMODELREQUEST"]._serialized_start = 738
    _globals["_ASSIGNMENTBIGMODELREQUEST"]._serialized_end = 888
    _globals["_ASSIGNMENTBIGMODELREQUESTBODY"]._serialized_start = 890
    _globals["_ASSIGNMENTBIGMODELREQUESTBODY"]._serialized_end = 939
    _globals["_ASSIGNMENTBIGMODELRESPONSE"]._serialized_start = 942
    _globals["_ASSIGNMENTBIGMODELRESPONSE"]._serialized_end = 1094
    _globals["_ASSIGNMENTBIGMODELRESPONSEBODY"]._serialized_start = 1096
    _globals["_ASSIGNMENTBIGMODELRESPONSEBODY"]._serialized_end = 1195
    _globals["_ASSIGNMENTARTIFICIALREQUEST"]._serialized_start = 1198
    _globals["_ASSIGNMENTARTIFICIALREQUEST"]._serialized_end = 1352
    _globals["_ASSIGNMENTARTIFICIALREQUESTBODY"]._serialized_start = 1354
    _globals["_ASSIGNMENTARTIFICIALREQUESTBODY"]._serialized_end = 1404
    _globals["_ASSIGNMENTARTIFICIALRESPONSE"]._serialized_start = 1407
    _globals["_ASSIGNMENTARTIFICIALRESPONSE"]._serialized_end = 1563
    _globals["_ASSIGNMENTARTIFICIALRESPONSEBODY"]._serialized_start = 1565
    _globals["_ASSIGNMENTARTIFICIALRESPONSEBODY"]._serialized_end = 1666
    _globals["_STUDENTACTIONREQUEST"]._serialized_start = 1669
    _globals["_STUDENTACTIONREQUEST"]._serialized_end = 1809
    _globals["_STUDENTACTIONREQUESTBODY"]._serialized_start = 1811
    _globals["_STUDENTACTIONREQUESTBODY"]._serialized_end = 1883
    _globals["_STUDENTACTIONRESPONSE"]._serialized_start = 1886
    _globals["_STUDENTACTIONRESPONSE"]._serialized_end = 2028
    _globals["_STUDENTACTIONRESPONSEBODY"]._serialized_start = 2030
    _globals["_STUDENTACTIONRESPONSEBODY"]._serialized_end = 2108
    _globals["_ASSIGNMENTCORRECTIONREQUEST"]._serialized_start = 2111
    _globals["_ASSIGNMENTCORRECTIONREQUEST"]._serialized_end = 2265
    _globals["_ASSIGNMENTCORRECTIONREQUESTBODY"]._serialized_start = 2267
    _globals["_ASSIGNMENTCORRECTIONREQUESTBODY"]._serialized_end = 2312
    _globals["_ASSIGNMENTCORRECTIONRESPONSE"]._serialized_start = 2315
    _globals["_ASSIGNMENTCORRECTIONRESPONSE"]._serialized_end = 2471
    _globals["_ASSIGNMENTCORRECTIONRESPONSEBODY"]._serialized_start = 2473
    _globals["_ASSIGNMENTCORRECTIONRESPONSEBODY"]._serialized_end = 2574
    _globals["_ASSIGNMENT"]._serialized_start = 2577
    _globals["_ASSIGNMENT"]._serialized_end = 3234
# @@protoc_insertion_point(module_scope)
