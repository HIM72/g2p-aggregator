# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/variant_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh import variants_pb2 as ga4gh_dot_variants__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/variant_service.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n\x1bga4gh/variant_service.proto\x12\x05ga4gh\x1a\x14ga4gh/variants.proto\x1a\x1cgoogle/api/annotations.proto\"U\n\x18SearchVariantSetsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"]\n\x19SearchVariantSetsResponse\x12\'\n\x0cvariant_sets\x18\x01 \x03(\x0b\x32\x11.ga4gh.VariantSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\".\n\x14GetVariantSetRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t\"\xa0\x01\n\x15SearchVariantsRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61ll_set_ids\x18\x02 \x03(\t\x12\x16\n\x0ereference_name\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x03\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12\x12\n\npage_token\x18\x07 \x01(\t\"S\n\x16SearchVariantsResponse\x12 \n\x08variants\x18\x01 \x03(\x0b\x32\x0e.ga4gh.Variant\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\'\n\x11GetVariantRequest\x12\x12\n\nvariant_id\x18\x01 \x01(\t\"{\n\x15SearchCallSetsRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rbio_sample_id\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"T\n\x16SearchCallSetsResponse\x12!\n\tcall_sets\x18\x01 \x03(\x0b\x32\x0e.ga4gh.CallSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"(\n\x11GetCallSetRequest\x12\x13\n\x0b\x63\x61ll_set_id\x18\x01 \x01(\t2\xaf\x05\n\x0eVariantService\x12\x7f\n\x11SearchVariantSets\x12\x1f.ga4gh.SearchVariantSetsRequest\x1a .ga4gh.SearchVariantSetsResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v0.6.0a8/variantsets/search:\x01*\x12o\n\rGetVariantSet\x12\x1b.ga4gh.GetVariantSetRequest\x1a\x11.ga4gh.VariantSet\".\x82\xd3\xe4\x93\x02(\x12&/v0.6.0a8/variantsets/{variant_set_id}\x12s\n\x0eSearchVariants\x12\x1c.ga4gh.SearchVariantsRequest\x1a\x1d.ga4gh.SearchVariantsResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v0.6.0a8/variants/search:\x01*\x12_\n\nGetVariant\x12\x18.ga4gh.GetVariantRequest\x1a\x0e.ga4gh.Variant\"\'\x82\xd3\xe4\x93\x02!\"\x1f/v0.6.0a8/variants/{variant_id}\x12s\n\x0eSearchCallSets\x12\x1c.ga4gh.SearchCallSetsRequest\x1a\x1d.ga4gh.SearchCallSetsResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v0.6.0a8/callsets/search:\x01*\x12`\n\nGetCallSet\x12\x18.ga4gh.GetCallSetRequest\x1a\x0e.ga4gh.CallSet\"(\x82\xd3\xe4\x93\x02\"\x12 /v0.6.0a8/callsets/{call_set_id}b\x06proto3')
  ,
  dependencies=[ga4gh_dot_variants__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHVARIANTSETSREQUEST = _descriptor.Descriptor(
  name='SearchVariantSetsRequest',
  full_name='ga4gh.SearchVariantSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.SearchVariantSetsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchVariantSetsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchVariantSetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=90,
  serialized_end=175,
)


_SEARCHVARIANTSETSRESPONSE = _descriptor.Descriptor(
  name='SearchVariantSetsResponse',
  full_name='ga4gh.SearchVariantSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_sets', full_name='ga4gh.SearchVariantSetsResponse.variant_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchVariantSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=177,
  serialized_end=270,
)


_GETVARIANTSETREQUEST = _descriptor.Descriptor(
  name='GetVariantSetRequest',
  full_name='ga4gh.GetVariantSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_set_id', full_name='ga4gh.GetVariantSetRequest.variant_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=272,
  serialized_end=318,
)


_SEARCHVARIANTSREQUEST = _descriptor.Descriptor(
  name='SearchVariantsRequest',
  full_name='ga4gh.SearchVariantsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_set_id', full_name='ga4gh.SearchVariantsRequest.variant_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_set_ids', full_name='ga4gh.SearchVariantsRequest.call_set_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='ga4gh.SearchVariantsRequest.reference_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh.SearchVariantsRequest.start', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh.SearchVariantsRequest.end', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchVariantsRequest.page_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchVariantsRequest.page_token', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=321,
  serialized_end=481,
)


_SEARCHVARIANTSRESPONSE = _descriptor.Descriptor(
  name='SearchVariantsResponse',
  full_name='ga4gh.SearchVariantsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variants', full_name='ga4gh.SearchVariantsResponse.variants', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchVariantsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=483,
  serialized_end=566,
)


_GETVARIANTREQUEST = _descriptor.Descriptor(
  name='GetVariantRequest',
  full_name='ga4gh.GetVariantRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_id', full_name='ga4gh.GetVariantRequest.variant_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=568,
  serialized_end=607,
)


_SEARCHCALLSETSREQUEST = _descriptor.Descriptor(
  name='SearchCallSetsRequest',
  full_name='ga4gh.SearchCallSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_set_id', full_name='ga4gh.SearchCallSetsRequest.variant_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.SearchCallSetsRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bio_sample_id', full_name='ga4gh.SearchCallSetsRequest.bio_sample_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchCallSetsRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchCallSetsRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=609,
  serialized_end=732,
)


_SEARCHCALLSETSRESPONSE = _descriptor.Descriptor(
  name='SearchCallSetsResponse',
  full_name='ga4gh.SearchCallSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_sets', full_name='ga4gh.SearchCallSetsResponse.call_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchCallSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=734,
  serialized_end=818,
)


_GETCALLSETREQUEST = _descriptor.Descriptor(
  name='GetCallSetRequest',
  full_name='ga4gh.GetCallSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_set_id', full_name='ga4gh.GetCallSetRequest.call_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=820,
  serialized_end=860,
)

_SEARCHVARIANTSETSRESPONSE.fields_by_name['variant_sets'].message_type = ga4gh_dot_variants__pb2._VARIANTSET
_SEARCHVARIANTSRESPONSE.fields_by_name['variants'].message_type = ga4gh_dot_variants__pb2._VARIANT
_SEARCHCALLSETSRESPONSE.fields_by_name['call_sets'].message_type = ga4gh_dot_variants__pb2._CALLSET
DESCRIPTOR.message_types_by_name['SearchVariantSetsRequest'] = _SEARCHVARIANTSETSREQUEST
DESCRIPTOR.message_types_by_name['SearchVariantSetsResponse'] = _SEARCHVARIANTSETSRESPONSE
DESCRIPTOR.message_types_by_name['GetVariantSetRequest'] = _GETVARIANTSETREQUEST
DESCRIPTOR.message_types_by_name['SearchVariantsRequest'] = _SEARCHVARIANTSREQUEST
DESCRIPTOR.message_types_by_name['SearchVariantsResponse'] = _SEARCHVARIANTSRESPONSE
DESCRIPTOR.message_types_by_name['GetVariantRequest'] = _GETVARIANTREQUEST
DESCRIPTOR.message_types_by_name['SearchCallSetsRequest'] = _SEARCHCALLSETSREQUEST
DESCRIPTOR.message_types_by_name['SearchCallSetsResponse'] = _SEARCHCALLSETSRESPONSE
DESCRIPTOR.message_types_by_name['GetCallSetRequest'] = _GETCALLSETREQUEST

SearchVariantSetsRequest = _reflection.GeneratedProtocolMessageType('SearchVariantSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHVARIANTSETSREQUEST,
  __module__ = 'ga4gh.variant_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchVariantSetsRequest)
  ))
_sym_db.RegisterMessage(SearchVariantSetsRequest)

SearchVariantSetsResponse = _reflection.GeneratedProtocolMessageType('SearchVariantSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHVARIANTSETSRESPONSE,
  __module__ = 'ga4gh.variant_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchVariantSetsResponse)
  ))
_sym_db.RegisterMessage(SearchVariantSetsResponse)

GetVariantSetRequest = _reflection.GeneratedProtocolMessageType('GetVariantSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVARIANTSETREQUEST,
  __module__ = 'ga4gh.variant_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetVariantSetRequest)
  ))
_sym_db.RegisterMessage(GetVariantSetRequest)

SearchVariantsRequest = _reflection.GeneratedProtocolMessageType('SearchVariantsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHVARIANTSREQUEST,
  __module__ = 'ga4gh.variant_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchVariantsRequest)
  ))
_sym_db.RegisterMessage(SearchVariantsRequest)

SearchVariantsResponse = _reflection.GeneratedProtocolMessageType('SearchVariantsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHVARIANTSRESPONSE,
  __module__ = 'ga4gh.variant_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchVariantsResponse)
  ))
_sym_db.RegisterMessage(SearchVariantsResponse)

GetVariantRequest = _reflection.GeneratedProtocolMessageType('GetVariantRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVARIANTREQUEST,
  __module__ = 'ga4gh.variant_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetVariantRequest)
  ))
_sym_db.RegisterMessage(GetVariantRequest)

SearchCallSetsRequest = _reflection.GeneratedProtocolMessageType('SearchCallSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHCALLSETSREQUEST,
  __module__ = 'ga4gh.variant_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchCallSetsRequest)
  ))
_sym_db.RegisterMessage(SearchCallSetsRequest)

SearchCallSetsResponse = _reflection.GeneratedProtocolMessageType('SearchCallSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHCALLSETSRESPONSE,
  __module__ = 'ga4gh.variant_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchCallSetsResponse)
  ))
_sym_db.RegisterMessage(SearchCallSetsResponse)

GetCallSetRequest = _reflection.GeneratedProtocolMessageType('GetCallSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCALLSETREQUEST,
  __module__ = 'ga4gh.variant_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetCallSetRequest)
  ))
_sym_db.RegisterMessage(GetCallSetRequest)


# @@protoc_insertion_point(module_scope)
