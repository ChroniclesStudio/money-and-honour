# -*- python-indent: 2 -*-
from __future__ import print_function

'''
Named integers for the constants from the module system.

For easier debugging of dumped scripts.

Named integers behave like normal integers, but prettyprint as their names.

_-filesnames are not exported on 'from A import *', which we make use of.
'''

from importlib import import_module as _import_module
from pprint import pprint as _pprint

_module_name_list = [
  'header_animations',
  'header_common',
  'header_dialogs',
  'header_factions',
  'header_game_menus',
  'header_ground_types',
  'header_item_modifiers',
  'header_items',
  'header_map_icons',
  'header_meshes',
  'header_mission_templates',
  'header_mission_types',
  'header_music',
  'header_operations',
  'header_particle_systems',
  'header_parties',
  'header_postfx',
  'header_presentations',
  'header_quests',
  'header_scene_props',
  'header_scenes',
  'header_skills',
  'header_skins',
  'header_sounds',
  'header_strings',
  'header_tableau_materials',
  'header_terrain_types',
  'header_triggers',
  'header_troops',
]


class _NamedInt(int):
  '''
  Integers with named print representation.
  Meant for easier debugging of module system dumps.
  '''
  def __new__(cls, name, value):
    self = int.__new__(cls,value)
    self._value = value
    self._name = name
    return self

  def __repr__(self):
    return self._name
  def __str__(self):
    return str(self._value)
  def __int__(self):
    return self._value
  def __trunc__(self):
    return self._value

for _module_name in _module_name_list:
  _module = _import_module(_module_name)
  for _name, _value in vars(_module).items():
    if not _name.startswith("_") and isinstance(_value,int):
      globals()[_name] = _NamedInt(_name, _value)

