# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: discord_users/v1/FrecencyUserSettings.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'discord_users/v1/FrecencyUserSettings.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+discord_users/v1/FrecencyUserSettings.proto\x12\x1f\x64iscord_protos.discord_users.v1\"\xdb!\n\x14\x46recencyUserSettings\x12U\n\x08versions\x18\x01 \x01(\x0b\x32>.discord_protos.discord_users.v1.FrecencyUserSettings.VersionsH\x00\x88\x01\x01\x12^\n\rfavorite_gifs\x18\x02 \x01(\x0b\x32\x42.discord_protos.discord_users.v1.FrecencyUserSettings.FavoriteGIFsH\x01\x88\x01\x01\x12\x66\n\x11\x66\x61vorite_stickers\x18\x03 \x01(\x0b\x32\x46.discord_protos.discord_users.v1.FrecencyUserSettings.FavoriteStickersH\x02\x88\x01\x01\x12\x64\n\x10sticker_frecency\x18\x04 \x01(\x0b\x32\x45.discord_protos.discord_users.v1.FrecencyUserSettings.StickerFrecencyH\x03\x88\x01\x01\x12\x62\n\x0f\x66\x61vorite_emojis\x18\x05 \x01(\x0b\x32\x44.discord_protos.discord_users.v1.FrecencyUserSettings.FavoriteEmojisH\x04\x88\x01\x01\x12`\n\x0e\x65moji_frecency\x18\x06 \x01(\x0b\x32\x43.discord_protos.discord_users.v1.FrecencyUserSettings.EmojiFrecencyH\x05\x88\x01\x01\x12{\n\x1c\x61pplication_command_frecency\x18\x07 \x01(\x0b\x32P.discord_protos.discord_users.v1.FrecencyUserSettings.ApplicationCommandFrecencyH\x06\x88\x01\x01\x12w\n\x1a\x66\x61vorite_soundboard_sounds\x18\x08 \x01(\x0b\x32N.discord_protos.discord_users.v1.FrecencyUserSettings.FavoriteSoundboardSoundsH\x07\x88\x01\x01\x12l\n\x14\x61pplication_frecency\x18\t \x01(\x0b\x32I.discord_protos.discord_users.v1.FrecencyUserSettings.ApplicationFrecencyH\x08\x88\x01\x01\x12k\n\x14heard_sound_frecency\x18\n \x01(\x0b\x32H.discord_protos.discord_users.v1.FrecencyUserSettings.HeardSoundFrecencyH\t\x88\x01\x01\x12m\n\x15played_sound_frecency\x18\x0b \x01(\x0b\x32I.discord_protos.discord_users.v1.FrecencyUserSettings.PlayedSoundFrecencyH\n\x88\x01\x01\x12v\n\x1aguild_and_channel_frecency\x18\x0c \x01(\x0b\x32M.discord_protos.discord_users.v1.FrecencyUserSettings.GuildAndChannelFrecencyH\x0b\x88\x01\x01\x12i\n\x17\x65moji_reaction_frecency\x18\r \x01(\x0b\x32\x43.discord_protos.discord_users.v1.FrecencyUserSettings.EmojiFrecencyH\x0c\x88\x01\x01\x1aP\n\x08Versions\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\r\x12\x16\n\x0eserver_version\x18\x02 \x01(\r\x12\x14\n\x0c\x64\x61ta_version\x18\x03 \x01(\r\x1a\x97\x01\n\x0b\x46\x61voriteGIF\x12M\n\x06\x66ormat\x18\x01 \x01(\x0e\x32=.discord_protos.discord_users.v1.FrecencyUserSettings.GIFType\x12\x0b\n\x03src\x18\x02 \x01(\t\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\r\n\x05order\x18\x05 \x01(\r\x1a\xf0\x01\n\x0c\x46\x61voriteGIFs\x12Z\n\x04gifs\x18\x01 \x03(\x0b\x32L.discord_protos.discord_users.v1.FrecencyUserSettings.FavoriteGIFs.GifsEntry\x12\x14\n\x0chide_tooltip\x18\x02 \x01(\x08\x1an\n\tGifsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12P\n\x05value\x18\x02 \x01(\x0b\x32\x41.discord_protos.discord_users.v1.FrecencyUserSettings.FavoriteGIF:\x02\x38\x01\x1a\'\n\x10\x46\x61voriteStickers\x12\x13\n\x0bsticker_ids\x18\x01 \x03(\x06\x1aX\n\x0c\x46recencyItem\x12\x12\n\ntotal_uses\x18\x01 \x01(\r\x12\x13\n\x0brecent_uses\x18\x02 \x03(\x04\x12\x10\n\x08\x66recency\x18\x03 \x01(\x05\x12\r\n\x05score\x18\x04 \x01(\x05\x1a\xed\x01\n\x0fStickerFrecency\x12\x65\n\x08stickers\x18\x01 \x03(\x0b\x32S.discord_protos.discord_users.v1.FrecencyUserSettings.StickerFrecency.StickersEntry\x1as\n\rStickersEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\x1a$\n\x0e\x46\x61voriteEmojis\x12\x12\n\x06\x65mojis\x18\x01 \x03(\tB\x02\x10\x00\x1a\xe3\x01\n\rEmojiFrecency\x12_\n\x06\x65mojis\x18\x01 \x03(\x0b\x32O.discord_protos.discord_users.v1.FrecencyUserSettings.EmojiFrecency.EmojisEntry\x1aq\n\x0b\x45mojisEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\x1a\xa6\x02\n\x1a\x41pplicationCommandFrecency\x12\x87\x01\n\x14\x61pplication_commands\x18\x01 \x03(\x0b\x32i.discord_protos.discord_users.v1.FrecencyUserSettings.ApplicationCommandFrecency.ApplicationCommandsEntry\x1a~\n\x18\x41pplicationCommandsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\x1a-\n\x18\x46\x61voriteSoundboardSounds\x12\x11\n\tsound_ids\x18\x01 \x03(\x06\x1a\x81\x02\n\x13\x41pplicationFrecency\x12q\n\x0c\x61pplications\x18\x01 \x03(\x0b\x32[.discord_protos.discord_users.v1.FrecencyUserSettings.ApplicationFrecency.ApplicationsEntry\x1aw\n\x11\x41pplicationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\x1a\xfd\x01\n\x12HeardSoundFrecency\x12o\n\x0cheard_sounds\x18\x01 \x03(\x0b\x32Y.discord_protos.discord_users.v1.FrecencyUserSettings.HeardSoundFrecency.HeardSoundsEntry\x1av\n\x10HeardSoundsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\x1a\x82\x02\n\x13PlayedSoundFrecency\x12r\n\rplayed_sounds\x18\x01 \x03(\x0b\x32[.discord_protos.discord_users.v1.FrecencyUserSettings.PlayedSoundFrecency.PlayedSoundsEntry\x1aw\n\x11PlayedSoundsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\x1a\x97\x02\n\x17GuildAndChannelFrecency\x12\x7f\n\x12guild_and_channels\x18\x01 \x03(\x0b\x32\x63.discord_protos.discord_users.v1.FrecencyUserSettings.GuildAndChannelFrecency.GuildAndChannelsEntry\x1a{\n\x15GuildAndChannelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\"D\n\x07GIFType\x12\x11\n\rGIF_TYPE_NONE\x10\x00\x12\x12\n\x0eGIF_TYPE_IMAGE\x10\x01\x12\x12\n\x0eGIF_TYPE_VIDEO\x10\x02\x42\x0b\n\t_versionsB\x10\n\x0e_favorite_gifsB\x14\n\x12_favorite_stickersB\x13\n\x11_sticker_frecencyB\x12\n\x10_favorite_emojisB\x11\n\x0f_emoji_frecencyB\x1f\n\x1d_application_command_frecencyB\x1d\n\x1b_favorite_soundboard_soundsB\x17\n\x15_application_frecencyB\x17\n\x15_heard_sound_frecencyB\x18\n\x16_played_sound_frecencyB\x1d\n\x1b_guild_and_channel_frecencyB\x1a\n\x18_emoji_reaction_frecencyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'discord_users.v1.FrecencyUserSettings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY']._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY']._serialized_options = b'8\001'
  _globals['_FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY']._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY']._serialized_options = b'8\001'
  _globals['_FRECENCYUSERSETTINGS_FAVORITEEMOJIS'].fields_by_name['emojis']._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_FAVORITEEMOJIS'].fields_by_name['emojis']._serialized_options = b'\020\000'
  _globals['_FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY']._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY']._serialized_options = b'8\001'
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY']._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY']._serialized_options = b'8\001'
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONFRECENCY_APPLICATIONSENTRY']._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONFRECENCY_APPLICATIONSENTRY']._serialized_options = b'8\001'
  _globals['_FRECENCYUSERSETTINGS_HEARDSOUNDFRECENCY_HEARDSOUNDSENTRY']._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_HEARDSOUNDFRECENCY_HEARDSOUNDSENTRY']._serialized_options = b'8\001'
  _globals['_FRECENCYUSERSETTINGS_PLAYEDSOUNDFRECENCY_PLAYEDSOUNDSENTRY']._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_PLAYEDSOUNDFRECENCY_PLAYEDSOUNDSENTRY']._serialized_options = b'8\001'
  _globals['_FRECENCYUSERSETTINGS_GUILDANDCHANNELFRECENCY_GUILDANDCHANNELSENTRY']._loaded_options = None
  _globals['_FRECENCYUSERSETTINGS_GUILDANDCHANNELFRECENCY_GUILDANDCHANNELSENTRY']._serialized_options = b'8\001'
  _globals['_FRECENCYUSERSETTINGS']._serialized_start=81
  _globals['_FRECENCYUSERSETTINGS']._serialized_end=4396
  _globals['_FRECENCYUSERSETTINGS_VERSIONS']._serialized_start=1495
  _globals['_FRECENCYUSERSETTINGS_VERSIONS']._serialized_end=1575
  _globals['_FRECENCYUSERSETTINGS_FAVORITEGIF']._serialized_start=1578
  _globals['_FRECENCYUSERSETTINGS_FAVORITEGIF']._serialized_end=1729
  _globals['_FRECENCYUSERSETTINGS_FAVORITEGIFS']._serialized_start=1732
  _globals['_FRECENCYUSERSETTINGS_FAVORITEGIFS']._serialized_end=1972
  _globals['_FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY']._serialized_start=1862
  _globals['_FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY']._serialized_end=1972
  _globals['_FRECENCYUSERSETTINGS_FAVORITESTICKERS']._serialized_start=1974
  _globals['_FRECENCYUSERSETTINGS_FAVORITESTICKERS']._serialized_end=2013
  _globals['_FRECENCYUSERSETTINGS_FRECENCYITEM']._serialized_start=2015
  _globals['_FRECENCYUSERSETTINGS_FRECENCYITEM']._serialized_end=2103
  _globals['_FRECENCYUSERSETTINGS_STICKERFRECENCY']._serialized_start=2106
  _globals['_FRECENCYUSERSETTINGS_STICKERFRECENCY']._serialized_end=2343
  _globals['_FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY']._serialized_start=2228
  _globals['_FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY']._serialized_end=2343
  _globals['_FRECENCYUSERSETTINGS_FAVORITEEMOJIS']._serialized_start=2345
  _globals['_FRECENCYUSERSETTINGS_FAVORITEEMOJIS']._serialized_end=2381
  _globals['_FRECENCYUSERSETTINGS_EMOJIFRECENCY']._serialized_start=2384
  _globals['_FRECENCYUSERSETTINGS_EMOJIFRECENCY']._serialized_end=2611
  _globals['_FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY']._serialized_start=2498
  _globals['_FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY']._serialized_end=2611
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY']._serialized_start=2614
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY']._serialized_end=2908
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY']._serialized_start=2782
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY']._serialized_end=2908
  _globals['_FRECENCYUSERSETTINGS_FAVORITESOUNDBOARDSOUNDS']._serialized_start=2910
  _globals['_FRECENCYUSERSETTINGS_FAVORITESOUNDBOARDSOUNDS']._serialized_end=2955
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONFRECENCY']._serialized_start=2958
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONFRECENCY']._serialized_end=3215
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONFRECENCY_APPLICATIONSENTRY']._serialized_start=3096
  _globals['_FRECENCYUSERSETTINGS_APPLICATIONFRECENCY_APPLICATIONSENTRY']._serialized_end=3215
  _globals['_FRECENCYUSERSETTINGS_HEARDSOUNDFRECENCY']._serialized_start=3218
  _globals['_FRECENCYUSERSETTINGS_HEARDSOUNDFRECENCY']._serialized_end=3471
  _globals['_FRECENCYUSERSETTINGS_HEARDSOUNDFRECENCY_HEARDSOUNDSENTRY']._serialized_start=3353
  _globals['_FRECENCYUSERSETTINGS_HEARDSOUNDFRECENCY_HEARDSOUNDSENTRY']._serialized_end=3471
  _globals['_FRECENCYUSERSETTINGS_PLAYEDSOUNDFRECENCY']._serialized_start=3474
  _globals['_FRECENCYUSERSETTINGS_PLAYEDSOUNDFRECENCY']._serialized_end=3732
  _globals['_FRECENCYUSERSETTINGS_PLAYEDSOUNDFRECENCY_PLAYEDSOUNDSENTRY']._serialized_start=3613
  _globals['_FRECENCYUSERSETTINGS_PLAYEDSOUNDFRECENCY_PLAYEDSOUNDSENTRY']._serialized_end=3732
  _globals['_FRECENCYUSERSETTINGS_GUILDANDCHANNELFRECENCY']._serialized_start=3735
  _globals['_FRECENCYUSERSETTINGS_GUILDANDCHANNELFRECENCY']._serialized_end=4014
  _globals['_FRECENCYUSERSETTINGS_GUILDANDCHANNELFRECENCY_GUILDANDCHANNELSENTRY']._serialized_start=3891
  _globals['_FRECENCYUSERSETTINGS_GUILDANDCHANNELFRECENCY_GUILDANDCHANNELSENTRY']._serialized_end=4014
  _globals['_FRECENCYUSERSETTINGS_GIFTYPE']._serialized_start=4016
  _globals['_FRECENCYUSERSETTINGS_GIFTYPE']._serialized_end=4084
# @@protoc_insertion_point(module_scope)
