# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: premium_marketing/v1/PremiumMarketingComponentProperties.proto
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
    'premium_marketing/v1/PremiumMarketingComponentProperties.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>premium_marketing/v1/PremiumMarketingComponentProperties.proto\x12#discord_protos.premium_marketing.v1\"\xb9\x11\n#PremiumMarketingComponentProperties\x12\x13\n\x0bplaceholder\x18\x01 \x01(\t\x12\x92\x01\n\x1c\x61nnouncement_modal_variant_1\x18\x02 \x01(\x0b\x32l.discord_protos.premium_marketing.v1.PremiumMarketingComponentProperties.AnnouncementModalVariant1Properties\x12\x1a\n\x12\x63ontent_identifier\x18\x03 \x01(\t\x1am\n\x0b\x46\x65\x61tureCard\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x0c\n\x04pill\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x12\x12\n\nimage_link\x18\x04 \x01(\t\x12\x1e\n\x16image_link_light_theme\x18\x05 \x01(\t\x1a\x90\x01\n\x12SubscriptionButton\x12\x0c\n\x04\x63opy\x18\x01 \x01(\t\x12l\n\rbutton_action\x18\x02 \x01(\x0e\x32U.discord_protos.premium_marketing.v1.PremiumMarketingComponentProperties.ButtonAction\x1a<\n\x08Subtitle\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\x0e\n\x06locale\x18\x02 \x01(\t\x12\x12\n\nis_default\x18\x03 \x01(\x08\x1a\xff\x05\n\x0fVariant1Storage\x12\xb5\x01\n)hero_art_localized_video_links_dark_theme\x18\x01 \x03(\x0b\x32\x81\x01.discord_protos.premium_marketing.v1.PremiumMarketingComponentProperties.Variant1Storage.HeroArtLocalizedVideoLinksDarkThemeEntry\x12\xb7\x01\n*hero_art_localized_video_links_light_theme\x18\x02 \x03(\x0b\x32\x82\x01.discord_protos.premium_marketing.v1.PremiumMarketingComponentProperties.Variant1Storage.HeroArtLocalizedVideoLinksLightThemeEntry\x12\x9e\x01\n\x1dhero_art_video_subtitle_links\x18\x03 \x03(\x0b\x32w.discord_protos.premium_marketing.v1.PremiumMarketingComponentProperties.Variant1Storage.HeroArtVideoSubtitleLinksEntry\x1aJ\n(HeroArtLocalizedVideoLinksDarkThemeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aK\n)HeroArtLocalizedVideoLinksLightThemeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a@\n\x1eHeroArtVideoSubtitleLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x85\x06\n#AnnouncementModalVariant1Properties\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x11\n\tsubheader\x18\x02 \x01(\t\x12\x12\n\nvideo_link\x18\x03 \x01(\t\x12\x17\n\x0fhelp_article_id\x18\x04 \x01(\t\x12k\n\rfeature_cards\x18\x05 \x03(\x0b\x32T.discord_protos.premium_marketing.v1.PremiumMarketingComponentProperties.FeatureCard\x12p\n\x06\x62utton\x18\x06 \x01(\x0b\x32[.discord_protos.premium_marketing.v1.PremiumMarketingComponentProperties.SubscriptionButtonH\x00\x88\x01\x01\x12\x13\n\x0b\x64ismiss_key\x18\x07 \x01(\t\x12\'\n\x1fhero_art_video_link_light_theme\x18\x08 \x01(\t\x12&\n\x1ehero_art_image_link_dark_theme\x18\t \x01(\t\x12\'\n\x1fhero_art_image_link_light_theme\x18\n \x01(\t\x12\x16\n\x0emodal_top_pill\x18\x0b \x01(\t\x12\x0c\n\x04\x62ody\x18\x0c \x01(\t\x12s\n\x18hero_art_video_subtitles\x18\r \x03(\x0b\x32Q.discord_protos.premium_marketing.v1.PremiumMarketingComponentProperties.Subtitle\x12n\n\x07storage\x18\x0e \x01(\x0b\x32X.discord_protos.premium_marketing.v1.PremiumMarketingComponentProperties.Variant1StorageH\x01\x88\x01\x01\x42\t\n\x07_buttonB\n\n\x08_storage\"\x81\x01\n\x0c\x42uttonAction\x12\x1d\n\x19\x42UTTON_ACTION_UNSPECIFIED\x10\x00\x12%\n!BUTTON_ACTION_OPEN_MARKETING_PAGE\x10\x01\x12+\n\'BUTTON_ACTION_OPEN_TIER_2_PAYMENT_MODAL\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'premium_marketing.v1.PremiumMarketingComponentProperties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTLOCALIZEDVIDEOLINKSDARKTHEMEENTRY']._loaded_options = None
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTLOCALIZEDVIDEOLINKSDARKTHEMEENTRY']._serialized_options = b'8\001'
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTLOCALIZEDVIDEOLINKSLIGHTTHEMEENTRY']._loaded_options = None
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTLOCALIZEDVIDEOLINKSLIGHTTHEMEENTRY']._serialized_options = b'8\001'
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTVIDEOSUBTITLELINKSENTRY']._loaded_options = None
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTVIDEOSUBTITLELINKSENTRY']._serialized_options = b'8\001'
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES']._serialized_start=104
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES']._serialized_end=2337
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_FEATURECARD']._serialized_start=341
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_FEATURECARD']._serialized_end=450
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_SUBSCRIPTIONBUTTON']._serialized_start=453
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_SUBSCRIPTIONBUTTON']._serialized_end=597
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_SUBTITLE']._serialized_start=599
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_SUBTITLE']._serialized_end=659
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE']._serialized_start=662
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE']._serialized_end=1429
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTLOCALIZEDVIDEOLINKSDARKTHEMEENTRY']._serialized_start=1212
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTLOCALIZEDVIDEOLINKSDARKTHEMEENTRY']._serialized_end=1286
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTLOCALIZEDVIDEOLINKSLIGHTTHEMEENTRY']._serialized_start=1288
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTLOCALIZEDVIDEOLINKSLIGHTTHEMEENTRY']._serialized_end=1363
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTVIDEOSUBTITLELINKSENTRY']._serialized_start=1365
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_VARIANT1STORAGE_HEROARTVIDEOSUBTITLELINKSENTRY']._serialized_end=1429
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_ANNOUNCEMENTMODALVARIANT1PROPERTIES']._serialized_start=1432
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_ANNOUNCEMENTMODALVARIANT1PROPERTIES']._serialized_end=2205
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_BUTTONACTION']._serialized_start=2208
  _globals['_PREMIUMMARKETINGCOMPONENTPROPERTIES_BUTTONACTION']._serialized_end=2337
# @@protoc_insertion_point(module_scope)
