# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ohsu/g2p.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ga4gh import sequence_annotations_pb2 as ga4gh_dot_sequence__annotations__pb2
from ga4gh import genotype_phenotype_pb2 as ga4gh_dot_genotype__phenotype__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ohsu/g2p.proto',
  package='ohsu.g2p',
  syntax='proto3',
  serialized_pb=_b('\n\x0eohsu/g2p.proto\x12\x08ohsu.g2p\x1a\x1cgoogle/protobuf/struct.proto\x1a ga4gh/sequence_annotations.proto\x1a\x1ega4gh/genotype_phenotype.proto\"\xd0\x02\n\x08\x45vidence\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0c\n\x04gene\x18\x02 \x01(\t\x12\x1f\n\x07\x66\x65\x61ture\x18\x03 \x01(\x0b\x32\x0e.ga4gh.Feature\x12\x37\n\x0b\x61ssociation\x18\x04 \x01(\x0b\x32\".ga4gh.FeaturePhenotypeAssociation\x12$\n\x03\x63gi\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12$\n\x03jax\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12&\n\x05\x63ivic\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06oncokb\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12/\n\x0emolecularmatch\x18\t \x01(\x0b\x32\x17.google.protobuf.Structb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,ga4gh_dot_sequence__annotations__pb2.DESCRIPTOR,ga4gh_dot_genotype__phenotype__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EVIDENCE = _descriptor.Descriptor(
  name='Evidence',
  full_name='ohsu.g2p.Evidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='ohsu.g2p.Evidence.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gene', full_name='ohsu.g2p.Evidence.gene', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature', full_name='ohsu.g2p.Evidence.feature', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='association', full_name='ohsu.g2p.Evidence.association', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cgi', full_name='ohsu.g2p.Evidence.cgi', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jax', full_name='ohsu.g2p.Evidence.jax', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='civic', full_name='ohsu.g2p.Evidence.civic', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oncokb', full_name='ohsu.g2p.Evidence.oncokb', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='molecularmatch', full_name='ohsu.g2p.Evidence.molecularmatch', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=125,
  serialized_end=461,
)

_EVIDENCE.fields_by_name['feature'].message_type = ga4gh_dot_sequence__annotations__pb2._FEATURE
_EVIDENCE.fields_by_name['association'].message_type = ga4gh_dot_genotype__phenotype__pb2._FEATUREPHENOTYPEASSOCIATION
_EVIDENCE.fields_by_name['cgi'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_EVIDENCE.fields_by_name['jax'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_EVIDENCE.fields_by_name['civic'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_EVIDENCE.fields_by_name['oncokb'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_EVIDENCE.fields_by_name['molecularmatch'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['Evidence'] = _EVIDENCE

Evidence = _reflection.GeneratedProtocolMessageType('Evidence', (_message.Message,), dict(
  DESCRIPTOR = _EVIDENCE,
  __module__ = 'ohsu.g2p_pb2'
  # @@protoc_insertion_point(class_scope:ohsu.g2p.Evidence)
  ))
_sym_db.RegisterMessage(Evidence)


# @@protoc_insertion_point(module_scope)
