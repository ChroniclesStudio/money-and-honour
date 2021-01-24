# -*- python-indent: 2 -*-

# FIXME: Bug: Swapping items may fail without error-sound,
# FIXME       when player doesn't meet skill requirement;
# FIXME       Observed for throwing weapons.

from __future__ import print_function

from header_item_modifiers import *
from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
from header_skills import *
import string

from yael_util import *
from pprint import pprint
from itertools import izip_longest

#### Register aliases
reg_ignore = reg50

reg_ol_idx = reg49
reg_ol_type = reg48
reg_ol_troop = reg47
reg_ol_invslot = reg46
reg_ol_itmesh = reg45
reg_ol_itmesh_x = reg44
reg_ol_itmesh_y = reg43
reg_ol_cont = reg42

#### Display states

state_inventory_list = 0
state_leave = 1
state_skill_list = 2

#### Overlay types

ot_inventory_button = 1 
ot_leave_button = 2
ot_itemslot = 3
ot_item_interact = 4
ot_item = 5
ot_passive = 6
ot_can_equip = 7
ot_state_button = 8
ot_banner_button = 9

#### Array layout
_idx = -1;
def _next():
  global _idx
  _idx += 1
  return _idx

arr_ol_object = _next()
arr_ol_type = _next()
arr_ol_troop = _next()
arr_ol_invslot = _next()
arr_ol_itmesh = _next()
arr_ol_itmesh_x = _next()
arr_ol_itmesh_y = _next()
arr_ol_cont = _next()
arr_trp = _next()

arr_slot_max = _next() # defines spacing; Must be one more than maximum offset number.

#### Layout constants

size_inv_slot = 600 # Scaling factor for inventory slots.; 600 best, others for debugging
size_inv_skip = int(size_inv_slot * 0.09) # How much space each slot is supposed to require. 
                                          # 0.09 is just barely not overlapping.
size_scrollable = 2000
size_skill_table_xstep = 17
size_skill_table_skill_font = 800
size_skill_table_name_font = 400
size_skill_table_yoffset = +6

print('  ' + __name__)


#### skill table layout

_STAT_SHORTNAMES = dict(
  ca_strength = 'Str',
  ca_agility = 'Agi',
  ca_intelligence = 'Int',
  ca_charisma = 'Cha',
  skl_ironflesh = 'IF',
  skl_power_strike = 'PS',
  skl_power_throw = 'PT',
  skl_power_draw = 'PD',
  skl_weapon_master = 'WM',
  skl_shield = 'Shd',
  skl_athletics = 'Ath',
  skl_riding = 'Rdg',
  skl_horse_archery = 'HAr',
  skl_looting = 'Ltg',
  skl_trainer = 'Trn',
  skl_tracking = 'Trk',
  skl_tactics = 'Tac',
  skl_pathfinding = 'Pf',
  skl_spotting = 'Sp',
  skl_inventory_management = 'IM',
  skl_wound_treatment = 'Wnd',
  skl_surgery = 'Srg',
  skl_first_aid = 'FA',
  skl_engineer = 'Eng',
  skl_persuasion = 'Per',
  skl_prisoner_management = 'PM',
  skl_leadership = 'Ldp',
  skl_trade = 'Trd',
)


def _put_stat(stat_name, idx):
  '''
  Helper function for creating the skill table.
  Valid only in that context due to local scripts.
  '''
  if stat_name.startswith('skl_'):
    getval = (store_skill_level,reg1,globals()[stat_name], ":trp")
    name = stat_name[4:].title()
  elif stat_name.startswith('ca_'):
    getval = (store_attribute_level,reg1,":trp", globals()[stat_name])
    name = stat_name[3:].title()
  elif stat_name == 'noop':
    return [y_progn]
  else:
    assert False, "Unexpectet stat_name, " + repr(stat_name)
  shortname = _STAT_SHORTNAMES[stat_name]
  return [y_progn,[
    getval,
    ("put_text_offset", ":ol_num", "@{reg1}", 0, size_skill_table_yoffset, 
     size_skill_table_skill_font, size_skill_table_skill_font, tf_center_justify),
    # (overlay_set_tooltip, ":ol_num", "@" + name), # Unreliable effect.
    ("put_text_offset", reg_ignore, "@" + shortname, 0, -8 + size_skill_table_yoffset, 
     size_skill_table_name_font, size_skill_table_name_font, tf_center_justify),
    (val_add, ":x_cur", size_skill_table_xstep),
  ]]

def _put_stats(*stat_names):
  '''
  Helper function for creating the skill table.
  Valid only in that context due to local scripts.
  '''
  out = [(try_begin),(eq,":lineno",1)]
  for i, n in enumerate(stat_names):
    out.extend([
      _put_stat(n, i),
    ])
  out.extend([
    (val_add, ":x_cur", int(size_skill_table_xstep/2)), 
    (try_end),
  ])
  return [y_progn, out]


#### scripts


scripts = [
  #### script_yael_array_set, ARRTROOP, INDEX, OFFSET, VALUE
  # Access array value from TROOP slot, by assuming that 
  # values are grouped in blocks of width ``arr_slot_max``, i.e.
  #   Block INDEX 0:  Slots 0, 1, ... arr_slot_max-1
  #   Block INDEX 1:  Slots arr_slot_max, arr_slot_max+1, ..., 2*arr_slot_max-1
  #   etc,
  ("yael_array_set", y_script(
    (store_script_param, ":troop",  1),
    (store_script_param, ":index",  2),
    (store_script_param, ":offset", 3),
    (store_script_param, ":value",  4),

    (store_mul, ":slot", ":index", arr_slot_max),
    (val_add, ":slot", ":offset"),
    (troop_set_slot, ":troop", ":slot", ":value"),
  )),

  #### script_yael_array_get, TROOP, INDEX, OFFSET -> reg0
  # Getter equivalent to `store_script_param'. 
  ("yael_array_get", y_script(
    (store_script_param, ":troop",  1),
    (store_script_param, ":index",  2),
    (store_script_param, ":offset", 3),
    
    (store_mul, ":slot", ":index", arr_slot_max),
    (val_add, ":slot", ":offset"),
    (troop_get_slot, reg0, ":troop", ":slot"),
  )),

  #### script_yael_set_overlay_info, OVERLAYID, OVERLAY_TYPE, TROOP_ID, INVENTORY_SLOT, ITEM_MESH_OVERLAY_ID
  # Set to -1, when not needed.
  # Increments $yael_num_overlays
  ("yael_set_overlay_info", y_script(
    (store_script_param, ":overlay_id", 1),
    (store_script_param, ":overlay_type", 2),
    (store_script_param, ":troop_id", 3),
    (store_script_param, ":inventory_slot", 4),
    (store_script_param, ":item_mesh_overlay_id", 5),
    (assign, ":IDX", "$yael_num_overlays"),

    ("yael_array_set", "trp_yael_array_a", ":IDX", arr_ol_object, ":overlay_id"),
    ("yael_array_set", "trp_yael_array_a", ":IDX", arr_ol_type,   ":overlay_type"),
    ("yael_array_set", "trp_yael_array_a", ":IDX", arr_ol_troop,  ":troop_id"),
    ("yael_array_set", "trp_yael_array_a", ":IDX", arr_ol_invslot,":inventory_slot"),
    ("yael_array_set", "trp_yael_array_a", ":IDX", arr_ol_itmesh, ":item_mesh_overlay_id"),
    ("yael_array_set", "trp_yael_array_a", ":IDX", arr_ol_cont,   "$yael_current_container_overlay"),
    ("yael_array_set", "trp_yael_array_a", ":IDX", arr_ol_itmesh_x,reg_ol_itmesh_x),
    ("yael_array_set", "trp_yael_array_a", ":IDX", arr_ol_itmesh_y,reg_ol_itmesh_y),                         

    (val_add, "$yael_num_overlays", 1),
  )),

  #### script_yael_get_overlay_info, OVERLAY_ID -> reg_ol_idx, reg_ol_type, reg_ol_troop, reg_ol_invslot, reg_ol_itmesh
  # Searches the known active overlays for OVERLAY_ID.
  # If none is found, sets all the output registers to -1.
  ("yael_get_overlay_info", y_script(
    (store_script_param, ":overlay_id", 1),

    (assign, reg_ol_idx, -1),
    (assign, reg_ol_type, -1),
    (assign, reg_ol_troop, -1),
    (assign, reg_ol_invslot, -1),
    (assign, reg_ol_itmesh, -1),
    (assign, reg_ol_cont, -1),

    (y_deflocal, "get", ["::dest", "::slot"], [
      ("yael_array_get", "trp_yael_array_a", ":idx", "::slot"),
      (assign, "::dest", reg0),
    ]),

    (assign, ":end", "$yael_num_overlays"),
    [try_for_range, ":idx", 0, ":end", [
      ("get", ":this_id", arr_ol_object),
      (eq, ":overlay_id", ":this_id"),
      (assign, reg_ol_idx, ":idx"),

      ("get", reg_ol_type,       arr_ol_type),
      ("get", reg_ol_troop,      arr_ol_troop),
      ("get", reg_ol_invslot,    arr_ol_invslot),
      ("get", reg_ol_itmesh,     arr_ol_itmesh),
      ("get", reg_ol_cont,       arr_ol_cont),
      ("get", reg_ol_itmesh_x,   arr_ol_itmesh_x),
      ("get", reg_ol_itmesh_y,   arr_ol_itmesh_y),
      (assign, ":end", 0), # break
    ]],
  )),

  #### script_yael_dump_overlay_info, 
  # Print info on all defined overlays.
  ("yael_dump_overlay_info", y_script(
    (display_message, "@--- YAEL DUMP OVERLAY INFO BEGIN ---"),
    (assign, reg0, "$yael_num_overlays"),
    (display_message, "@yael_num_overlays = {reg0}"),
    [try_for_range, ":idx", 0, "$yael_num_overlays", [
      (troop_get_slot, ":object", "trp_yael_array_a", ":idx"),
      (troop_get_slot, ":type",   "trp_yael_array_b", ":idx"),
      (troop_get_slot, ":trp",    "trp_yael_array_c", ":idx"),
      (troop_get_slot, ":slot",   "trp_yael_array_d", ":idx"),
      (troop_get_slot, ":itmesh", "trp_yael_array_e", ":idx"),

      (str_store_string, s3, "@INV_TRP"),
      [try_begin,[
        (neq, ":trp", -1),
        (str_store_troop_name, s3, ":trp"),
      ]],

      (assign, ":itemid", -1),
      (str_store_string, s6, "@INV_ITEM"),
      [try_begin, [
        (neq, ":trp", -1),
        (neq, ":slot", -1),
        (troop_get_inventory_slot, ":itemid", ":trp", ":slot"),
        (neq, ":itemid", -1),
        (str_store_item_name, s6, ":itemid"),
      ]],
      
      (assign, reg1, ":object"),
      (assign, reg2, ":type"),
      (assign, reg3, ":trp"),
      (assign, reg4, ":slot"),
      (assign, reg5, ":itmesh"),
      (assign, reg6, ":itemid"),

      (display_message, "@{reg1}, {reg2}, {reg3} {s3}, {reg4}, {reg5}, {reg6} {s6}"),
    ]],
    (display_message, "@--- YAEL DUMP OVERLAY INFO END ---"),
  )),

  #### script_yael_eqmgr_dummy_menu
  # The dummy menu serves to cause (change_screen_*) commands 
  # to return to the presentation.
  ("yael_eqmgr_dummy_menu", y_script(
    (assign, "$yael_num_overlays", 0),
    [try_begin, [
      (eq, "$g_yael_eqmgr_state", state_leave),
      (assign, "$g_yael_eqmgr_state", state_inventory_list),
      (jump_to_menu, "mnu_camp"), 
    ],[
      (start_presentation, "prsnt_yael_equip_overview"), 
    ]],
  )),

  #### script_yael_eqmgr_presentation_load
  # No arguments.
  # On-load event handler of eqmgr presentation.
  ("yael_eqmgr_presentation_load",
   y_script(
     #### INITIALIZATION
     (presentation_set_duration, 999999),
     (set_fixed_point_multiplier, 1000), # must be set for every event
     [try_begin, [
       (eq, "$cheat_mode", 1),
       ('yael_overlay_put_layout_markers', 0xFFFFFF),
     ]],
     (assign, "$yael_num_overlays", 0),
     (assign, "$yael_active_detail_overlay", -1),
     (assign, "$yael_selected_item_overlay", -1),
     (assign, "$yael_current_container_overlay", -1),
     # ("yael_dump_overlay_info"),


     #### deflocal: put_text, DEST, TEXT
     (y_deflocal, 'put_text', ['::dest', '::text' ], [
       # (create_text_overlay, '::dest', '::text'),
       # ('yael_overlay_set_position', '::dest', ':x_cur', ':y_cur'),
       ("put_text_offset", "::dest", "::text", 0, 0, 1000, 1000, 0),
     ]),
     
     #### deflocal: put_text_offset, DEST, TEXT, XOFFSET, YOFFSET, XSCALE, YSCALE, ALIGN_FLAG
     (y_deflocal, "put_text_offset", ["::dest", "::text", "::xoffset", "::yoffset",
                                      "::xscale", "::yscale", "::flag"], 
      [
        (create_text_overlay, "::dest", "::text", "::flag"),
        (store_add, ":_x", ":x_cur", "::xoffset"),
        (store_add, ":_y", ":y_cur", "::yoffset"),
        ("yael_overlay_set_position", "::dest", ":_x", ":_y"),
        ("yael_overlay_set_size", "::dest", "::xscale", "::yscale"),
      ]),
     
     #### Static items
     (assign, ":x_cur", 0), (assign, ":y_cur", 0),
     ("put_text_offset", "$yael_status_box", "@ --status--", 50, 720, 500, 500, tf_left_align),
     [try_begin, [(neq, "$cheat_mode", 1), ("yael_overlay_set_position", "$yael_status_box", 0, -100)]],
     ("put_text_offset", "$yael_requirement_box", "@ Requires <?>", 700, 670, 1000, 1000, tf_left_align),

     (create_button_overlay, ":continuebutton", "@Continue..."),
     ("yael_overlay_set_position", ":continuebutton", 255, 40),
     ("yael_set_overlay_info", ":continuebutton", ot_leave_button, -1, -1, -1),

     [try_begin, [
       (eq, "$g_yael_eqmgr_state", state_inventory_list),
       (str_store_string, s0, "@Equipment Overview"),
       (str_store_string, s1, "@Skills"),       
     ],[
       (str_store_string, s0, "@Skill Overview"),
       (str_store_string, s1, "@Equipment"),       
     ]],
     ("put_text_offset", reg_ignore, "@{s0}", 500, 680, 1500, 1500, tf_center_justify),

     (create_button_overlay, ":switchmode", "@{s1}"),
     ("yael_overlay_set_position", ":switchmode", 400, 40),
     ("yael_set_overlay_info", ":switchmode", ot_state_button, -1, -1, -1),

     [try_begin, [
       (eq, "$cheat_mode", 1),
       (create_button_overlay, ":changebanner", "@Cheat:Banner"),
       ("yael_overlay_set_position", ":changebanner", 550, 40),
       ("yael_set_overlay_info", ":changebanner", ot_banner_button, -1, -1, -1),
     ]],
     



     #### Calculate the troops to print
     (assign, ":party", "p_main_party"),
     (assign, ":idx", 0),
     (party_get_num_companion_stacks, ":num_stacks", ":party"),
     [try_for_range, ":stack_no", 0, ":num_stacks", [
       (party_stack_get_troop_id, ":trp", ":party", ":stack_no"),
       (troop_is_hero, ":trp"),
       ("yael_array_set", "trp_yael_array_a", ":idx", arr_trp, ":trp"),
       (val_add, ":idx", 1),
     ]],
     (assign, ":num_entries", ":idx"),

     #### Begin:Table-Box
     (str_clear, s0),
     (create_text_overlay, ":table_box", s0, tf_scrollable),
     ('yael_overlay_set_position',  ':table_box',   0, 70),
     ('yael_overlay_set_size',      ':table_box', 700,600),
     ('yael_overlay_set_area_size', ':table_box', 700,600),
     (set_container_overlay, ":table_box"),
     (assign, "$yael_current_container_overlay", ":table_box"),
     [try_begin, [
       (eq, "$cheat_mode", 1),
       ("yael_overlay_put_layout_markers", 0xFF0000),
     ]],


     #### Table
     (assign, ":index", -1),
     (assign, ":y_cur", size_scrollable), # Scrolling only works for y>0 so we start from far above.
     [try_for_range, ":idx", 0, ":num_entries", [ 
       ("yael_array_get", "trp_yael_array_a", ":idx", arr_trp),
       (assign, ":trp", reg0),
       
       (val_add, ":index", 1),
       (assign, ":numlines", 3),

       ## Little skip after each character.
       (val_add, ":y_cur", -10),

       [try_for_range, ":lineno", 0, ":numlines", [
         (val_add, ":y_cur", -15),
         (assign, ":x_cur", 30),

         #### Background overlay 'can equip'
         [try_begin, [
           (eq, ":lineno", 2),
           (create_mesh_overlay, ":canequip", "mesh_white_plane"),
           ("yael_overlay_set_position", ":canequip", ":x_cur", ":y_cur"),
           ("yael_overlay_set_size", ":canequip", 100000, int(3000/60.0*size_inv_skip) ),
           ("yael_set_overlay_info", ":canequip", ot_can_equip, ":trp", -1, -1),
           [try_begin,[
             (eq, "$cheat_mode", 1),
             (store_random_in_range, ":color", 0x000000, 0xFFFFFF),
             (overlay_set_color, ":canequip", ":color"),
             (overlay_set_alpha, ":canequip", 0xFF),
           ],[
             (overlay_set_alpha, ":canequip", 0),
           ]],
         ]],

         #### Name - TODO: Indicator for unspent skill points.
         [try_begin,[
           (eq, ":lineno", 1),
           (str_store_troop_name, s1, ":trp"),
           (create_button_overlay, ":button", "@{s1}", tf_left_align),
           ('yael_overlay_set_position', ":button", ":x_cur", ":y_cur"),
           ("yael_set_overlay_info", ":button", ot_inventory_button, ":trp", -1, -1),
         ]],
           (val_add, ":x_cur", 120),

         [try_begin, [
           (eq, "$g_yael_eqmgr_state", state_inventory_list),
           
           #### Skills (equip relevant)
           [try_for_range, ":col", 0, 2, [
             [try_begin, [
               (eq, ":lineno", 0), (eq, ":col", 0),
               (store_skill_level,reg1,skl_power_draw,":trp"),
               (str_store_string, s1, "@PowerDraw"),
             ],[
               (eq,":lineno", 1), (eq, ":col", 0),
               (store_skill_level,reg1,skl_power_throw,":trp"),
               (str_store_string, s1, "@PowerThrow"),
             ],[
               (eq,":lineno", 2), (eq, ":col", 0),
               (store_skill_level,reg1,skl_riding,":trp"),
               (str_store_string, s1, "@Riding"),
             ],[
               (eq,":lineno", 0), (eq, ":col", 1),
               (store_attribute_level,reg1,":trp",ca_strength),
               (str_store_string, s1, "@Strength"),
             ],[
               (assign, reg1, -999), # break condition
             ]],
             (neq, reg1, -999),
             ("put_text_offset", reg_ignore, "@{reg1}", 0, 0, 666, 666, tf_center_justify),
             ("put_text_offset", reg_ignore, "@{s1}", 0, -3, 333, 333, tf_center_justify),
             (val_add, ":x_cur", 30),
           ]],
         
           #### Equipped slots
           # 0-3: hands, 4:helmet, 5:body, 6:feet, 7:gloves, 8: horse
           (assign, ":item_yoffset", -30),
           [try_for_range, ":invslot", 0, 9, [
             [try_begin, [
               (eq, ":lineno", 0),
               ("yael_put_item_slot_overlay", ":x_cur", ":y_cur", 0, ":item_yoffset", ":trp", ":invslot"),
             ]],
             (val_add, ":x_cur", size_inv_skip),
           ]],
         ],[
           (eq, "$g_yael_eqmgr_state", state_skill_list),
           #### Skills (full table)
           [try_begin, [
             (eq, ":lineno", 1),
             (val_add, ":x_cur", int(size_skill_table_xstep / 2)),
           ]],
           _put_stats('ca_strength','ca_agility','ca_intelligence','ca_charisma'),
           _put_stats('skl_ironflesh','skl_power_strike','skl_power_throw','skl_power_draw'),
           _put_stats('skl_weapon_master','skl_shield','skl_athletics','skl_riding','skl_horse_archery',),
           _put_stats('skl_looting','skl_trainer','skl_tracking','skl_tactics'),
           _put_stats('skl_pathfinding','skl_spotting','skl_inventory_management'),
           _put_stats('skl_wound_treatment','skl_surgery','skl_first_aid','skl_engineer'),
           _put_stats('skl_persuasion','skl_prisoner_management','skl_leadership','skl_trade'),
         ]],
       ]],
     ]],
     
     
     #### End:Table-Box
     (set_container_overlay, -1),


     #### Player-inventory
     (create_text_overlay, ":player_inventory_box", "@ ", tf_scrollable),
     ('yael_overlay_set_position',  ':player_inventory_box', 710, 70),
     ('yael_overlay_set_size',      ':player_inventory_box', 190,600),
     ('yael_overlay_set_area_size', ':player_inventory_box', 190,600),
     (set_container_overlay, ":player_inventory_box"),
     (assign, "$yael_current_container_overlay", ":player_inventory_box"),
     [try_begin, [
       (eq, "$cheat_mode", 1),
       ("yael_overlay_put_layout_markers", 0xFF0000),
     ]],

     (troop_get_inventory_capacity, ":slotnomax", "trp_player"), # Include the equipped slots.

     [try_begin,[ # just for intentation
       (assign, ":x", 0),
       (assign, ":y", size_scrollable),
       [try_for_range, ":slotno", 10, ":slotnomax", [

         # Line-break on 1 modulo 3 (since we start at "10").
         [try_begin, [
           (store_mod, reg1, ":slotno", 3),
           (eq, reg1, 1),
           (assign, ":x", 0),
           (val_add, ":y", -size_inv_skip),
         ]],

         ("yael_put_item_slot_overlay", ":x", ":y", 20, size_scrollable, "trp_player", ":slotno"),

         (val_add, ":x", size_inv_skip),
       ]],
     ]],
     (set_container_overlay, -1),


  )),
  
  #### script_yael_eqmgr_presentation_event_state_change
  # No arguments.
  ("yael_eqmgr_presentation_event_state_change",y_script(
    (store_trigger_param_1, ":object"),
    
    # ("yael_dump_overlay_info"),
    ("yael_get_overlay_info", ":object"),
    (assign, ":trp", reg_ol_troop),
    (assign, ":otype", reg_ol_type),
    
    [try_begin,[
      #### Name buttons
      (eq, ":otype", ot_inventory_button),
      (str_store_troop_name, s1, ":trp"),
      # [try_begin, [
      #   (eq, "$g_yael_eqmgr_state", state_inventory_list),
      #   (change_screen_equip_other, ":trp"),
      # ],[
      #   (eq, "$g_yael_eqmgr_state", state_skill_list),
        (change_screen_view_character, ":trp"), # troop argument is undocumented but works.
      # ]],
    ],[
      #### Continue/Leave button
      (eq, ":otype", ot_leave_button),
      (presentation_set_duration, 0),
      (assign, "$g_yael_eqmgr_state", state_leave),
    ],[
      #### Switch state button
      (eq, ":otype", ot_state_button),
      [try_begin, [
        (eq, "$g_yael_eqmgr_state", state_inventory_list),
        (assign, "$g_yael_eqmgr_state", state_skill_list),
      ],[
        (assign, "$g_yael_eqmgr_state", state_inventory_list),
      ]],
      (presentation_set_duration, 0),
    ],[
      #### Banner button (cheat)
      (eq, ":otype", ot_banner_button),
      (start_presentation, "prsnt_banner_selection"),
    ]],
  )),

  #### script_yael_eqmgr_presentation_on_mouse_enter_leave
  ("yael_eqmgr_presentation_on_mouse_enter_leave",y_script(
    (store_trigger_param_1, ":object"),
    (store_trigger_param_2, ":enter_leave"),

    ("yael_get_overlay_info", ":object"),
    (assign, ":trp", reg_ol_troop),
    (assign, ":otype", reg_ol_type),
    (assign, ":invslot", reg_ol_invslot),
        
    (assign, ":itemid", -1),
    [try_begin, [
      (eq, ":otype", ot_item_interact),
      #### Item Details // Allow equip overlay
      ## TODO would be better if equip-overlay remained fixed after selecting item
      [try_begin, [
        (eq, ":enter_leave", 1), # leave
        (eq, ":object", "$yael_active_detail_overlay"), # prevents spurious closing
        (close_item_details),
        [try_for_range, ":idx", 0, "$yael_num_overlays", [
          ("yael_array_get", "trp_yael_array_a", ":idx", arr_ol_type),
          (eq, reg0, ot_can_equip),
          ("yael_array_get", "trp_yael_array_a", ":idx", arr_ol_object),
          (assign, ":ce", reg0),
          (overlay_set_alpha, ":ce", 0x00),
        ]],
      ],[
        (eq, ":enter_leave", 0), #enter
        (neq, ":trp", -1),
        (troop_get_inventory_slot, ":itemid", ":trp", ":invslot"),
        (troop_get_inventory_slot_modifier, ":itemmod", ":trp", ":invslot"),
        (neq, ":itemid", -1), 
        (overlay_get_position, pos1, ":object"),
        (show_item_details_with_modifier, ":itemid", ":itemmod", pos1, 100),
        (assign, "$yael_active_detail_overlay", ":object"),
        [try_for_range, ":idx", 0, "$yael_num_overlays", [
          ("yael_array_get", "trp_yael_array_a", ":idx", arr_ol_type),
          (eq, reg0, ot_can_equip),
          ("yael_array_get", "trp_yael_array_a", ":idx", arr_ol_object), (assign, ":ce", reg0),
          ("yael_array_get", "trp_yael_array_a", ":idx", arr_ol_troop), (assign, ":cetrp", reg0),
          [try_begin,[
            ("yael_item_usable_by_troop", ":cetrp", ":itemid"),
            (eq, reg0, 1),
            (overlay_set_alpha, ":ce", 0x00),
          ],[
            (overlay_set_color, ":ce", 0xFF0000),
            (overlay_set_alpha, ":ce", 0xAA),
          ]],
        ]],
      ]],
    ]],

    #### Debug Message
    ("yael_event_debug", ":object", ":enter_leave"),

  )),

  #### script_yael_eqmgr_presentation_on_mouse_press
  ("yael_eqmgr_presentation_on_mouse_press", y_script(
    (store_trigger_param_1, ":object"),
    (store_trigger_param_2, ":mouse_state"), # 0 left, 1 right, 2 middle
    (set_fixed_point_multiplier, 1000), # must be set for every event

    ("yael_get_overlay_info", ":object"),
    (assign, ":otype", reg_ol_type),

    [try_begin, [
      (eq, ":otype", ot_item_interact),
      [try_begin,[
        #### Selection clear - click same slot again or right-click
        (this_or_next|eq, ":object", "$yael_selected_item_overlay"),
        (eq, ":mouse_state", 1),
        (neq, "$yael_selected_item_overlay", -1),
        (overlay_set_alpha, "$yael_selected_item_overlay", 0x00),
        (assign, "$yael_selected_item_overlay", -1),
        (play_sound, "snd_click"),
      ],[
        #### Selection - left-click slot, when nothing is selected
        (eq, ":mouse_state", 0),
        (eq, "$yael_selected_item_overlay", -1),
        (overlay_set_alpha, ":object", 0xFF),
        (assign, "$yael_selected_item_overlay", ":object"),
        (play_sound, "snd_click"),
      ],[
        #### Selection swap - left-click, on other slot
        (eq, ":mouse_state", 0),
        (assign, ":a_overlay", ":object"),
        (assign, ":b_overlay", "$yael_selected_item_overlay"),

        ("yael_get_overlay_info", ":a_overlay"),
        (assign, ":a_trp", reg_ol_troop),
        (assign, ":a_invslot", reg_ol_invslot),
        ("yael_get_overlay_info", ":b_overlay"),
        (assign, ":b_trp", reg_ol_troop),
        (assign, ":b_invslot", reg_ol_invslot),

        ("yael_troop_swap_inventory_slots", ":a_trp", ":a_invslot", ":b_trp", ":b_invslot"),
        (assign, ":swap_errcode", reg0),
        
        [try_begin,[
          ## On success, remove selection state and redisplay.
          (eq, ":swap_errcode", 0),
          (assign, "$yael_selected_item_overlay", -1),
          (overlay_set_alpha, ":a_overlay", 0x00),
          (overlay_set_alpha, ":b_overlay", 0x00),
          (play_sound, "snd_click"),
          (presentation_set_duration, 0),
        ],[
          ## On failure, do nothing.
          (play_sound, "snd_man_grunt"),
        ]],
      ]],
    ]],

     
  )),

  #### script_yael_event_debug, OBJECT, STATE
  ("yael_event_debug", y_script(
    (store_script_param, ":object", 1),
    (store_script_param, ":state", 2),
    (set_fixed_point_multiplier, 1000), # must be set for every event

    ("yael_get_overlay_info", ":object"),
    (assign, ":trp", reg_ol_troop),
    (assign, ":otype", reg_ol_type),
    (assign, ":invslot", reg_ol_invslot),
    (assign, ":itmesh_x", reg_ol_itmesh_x),
    (assign, ":itmesh_y", reg_ol_itmesh_y),

    ("yael_describe_inventory_slot", ":trp", ":invslot"), 
    (str_store_string_reg, s8, s0),
    (overlay_get_position, pos1, ":object"),
    (position_get_x, reg31, pos1),
    (position_get_y, reg32, pos1),
    (position_get_z, reg33, pos1),
    (assign, reg1, ":object"),
    (assign, reg2, ":state"),
    (assign, reg4, ":invslot"),
    (assign, reg5, ":otype"),
    (assign, reg41, ":itmesh_x"),
    (assign, reg42, ":itmesh_y"),
    (overlay_set_text, "$yael_status_box", 
     "@object {reg1} type {reg5} at ({reg31},{reg32},{reg33}), itmesh at ({reg41},{reg42}), state {reg2}, {s8}"),
  )),

  #### script_yael_overlay_set_size, OVERLAY, WIDTH, HEIGHT
  # Remember that for text overlays WIDTH,HEIGHT are relative to 
  # the default font-size, and rescaled by set_fixed_point_multiplier.
  ("yael_overlay_set_size", y_script(
    (store_script_param, ":overlay", 1),
    (store_script_param, ":width", 2),
    (store_script_param, ":height", 3),
    (position_set_x, pos8, ":width"),
    (position_set_y, pos8, ":height"),
    (overlay_set_size, ":overlay", pos8),
  )),

  #### script_yael_overlay_set_area_size, OVERLAY, WIDTH, HEIGHT
  ("yael_overlay_set_area_size", y_script(
    (store_script_param, ":overlay", 1),
    (store_script_param, ":width", 2),
    (store_script_param, ":height", 3),
    (position_set_x, pos8, ":width"),
    (position_set_y, pos8, ":height"),
    (position_set_z, pos8, 1000),
    (overlay_set_area_size, ":overlay", pos8),
  )),

  #### script_yael_overlay_set_position, OVERLAY, X, Y
  ("yael_overlay_set_position", y_script(
    (store_script_param, ":overlay", 1),
    (store_script_param, ":x", 2),
    (store_script_param, ":y", 3),
    (position_set_x, pos8, ":x"),
    (position_set_y, pos8, ":y"),
    (assign, reg10, ":overlay"),
    (assign, reg11, ":x"),
    (assign, reg12, ":y"),
    (overlay_set_position, ":overlay", pos8),
  )),

  #### script_yael_overlay_put_layout_markers, COLOR
  ## Prints a mesh of position markers on the presentation, 
  ## to help with positioning overlays.
  ("yael_overlay_put_layout_markers", y_script(
    (store_script_param, ":color", 1),
     [try_for_range, ':i', -20, 20, [
       [try_for_range, ':j', -20, 20, [
         (store_mul, reg1, ':i', 100),
         (store_mul, reg2, ':j', 100),
         (create_text_overlay, ':text', '@{reg1}|-|{reg2}', tf_center_justify),
         ('yael_overlay_set_position', ':text', reg1, reg2),
         ('yael_overlay_set_size', ':text', 500, 500),
         (overlay_set_color, ":text", ":color"),
       ]],
     ]],
  )),

  #### script_yael_put_item_slot_overlay, X, Y, XOFFSET, YOFFSET, TROOP, SLOTNO -> reg0, reg1
  # reg0: Item mesh or -1 if no item. set TROOP=-1 to create only background mesh.
  # reg1: Background mesh
  ("yael_put_item_slot_overlay", y_script(
    (y_store_params, ":x", ":y", ":xo", ":yo", ":trp", ":slotno"),
    (val_add, ":x", ":xo"),
    (val_add, ":y", ":yo"),
    
    #### Layout Calculation
    (assign, ":xs", int(size_inv_slot*0.7)), # sizes of bgimage
    (assign, ":ys", int(size_inv_slot*0.7)),
    (assign, ":xsi", size_inv_slot), # sizes of item image
    (assign, ":ysi", size_inv_slot),
    (assign, ":xio", size_inv_slot*0.044), # offset for item mesh over background mesh
    (assign, ":yio", size_inv_slot*0.044), 
    (assign, ":xins", int(size_inv_slot*4.9)), # size of interact layer
    (assign, ":yins", int(size_inv_slot*4.9)),
    (assign, ":xino", int(-1.5*size_inv_slot/300.0)), # offset of mesh_white_plane position
    (assign, ":yino", int(-1.5*size_inv_slot/300.0)),

    ## get item info
    [try_begin, [
      (eq, ":trp", -1),
      (assign, ":itemid", -1),
    ],[
      (troop_get_inventory_slot, ":itemid", ":trp", ":slotno"),
      (neq, ":itemid", -1),
    ]],

    ## background mesh
    [try_begin, 
     [(neq, ":itemid",-1),(assign, ":bgmesh", "mesh_mp_inventory_slot_empty"),
     ],[(eq, ":slotno", 0),(assign, ":bgmesh", "mesh_mp_inventory_slot_equip"),
     ],[(eq, ":slotno", 1),(assign, ":bgmesh", "mesh_mp_inventory_slot_equip"),
     ],[(eq, ":slotno", 2),(assign, ":bgmesh", "mesh_mp_inventory_slot_equip"),
     ],[(eq, ":slotno", 3),(assign, ":bgmesh", "mesh_mp_inventory_slot_equip"),
     ],[(eq, ":slotno", 4),(assign, ":bgmesh", "mesh_mp_inventory_slot_helmet"),
     ],[(eq, ":slotno", 5),(assign, ":bgmesh", "mesh_mp_inventory_slot_armor"),
     ],[(eq, ":slotno", 6),(assign, ":bgmesh", "mesh_mp_inventory_slot_boot"),
     ],[(eq, ":slotno", 7),(assign, ":bgmesh", "mesh_mp_inventory_slot_glove"),
     ],[(eq, ":slotno", 8),(assign, ":bgmesh", "mesh_mp_inventory_slot_horse"),
     ],[(assign, ":bgmesh", "mesh_mp_inventory_slot_empty"),
     ]],
    # A full-alpha empty-slot mesh, with half-alpha symbol mesh, for 
    # better readabilty of the interface.
    (create_mesh_overlay, ":bg", "mesh_mp_inventory_slot_empty"),
    ("yael_overlay_set_position", ":bg", ":x", ":y"),
    ("yael_overlay_set_size", ":bg", ":xs", ":ys"),
    (create_mesh_overlay, ":bg", "mesh_mp_inventory_slot_empty"),
    ("yael_overlay_set_position", ":bg", ":x", ":y"),
    ("yael_overlay_set_size", ":bg", ":xs", ":ys"),
    (create_mesh_overlay, ":bg", ":bgmesh"),
    ("yael_overlay_set_position", ":bg", ":x", ":y"),
    ("yael_overlay_set_size", ":bg", ":xs", ":ys"),
    (overlay_set_alpha, ":bg", 0x20),

    ## item mesh
    [try_begin, [
      (eq, ":trp", -1),
      (assign, ":itmesh", -1),
    ],[
      (troop_get_inventory_slot, ":itemid", ":trp", ":slotno"),
      (neq, ":itemid", -1),

      (create_mesh_overlay_with_item_id, ":itmesh", ":itemid"),
      (store_add, ":xitem", ":x", ":xio"),
      (store_add, ":yitem", ":y", ":yio"),
      ("yael_overlay_set_position", ":itmesh", ":xitem", ":yitem"),
      ("yael_overlay_set_size", ":itmesh", ":xsi", ":ysi"),
      (str_store_item_name, s1, ":itemid"),
    ]],

    ## Some items meshes (boots!) are not recognized by events. 
    ## For these we add an invisible interaction-mesh on top.
    (store_add, ":xin", ":x", ":xino"),
    (store_add, ":yin", ":y", ":yino"),
    (create_mesh_overlay, ":interact", "mesh_white_plane"),
    ("yael_overlay_set_position", ":interact", ":xin", ":yin"),
    ("yael_overlay_set_size", ":interact", ":xins", ":yins"),
    (overlay_set_alpha, ":interact", 0x00),
    (overlay_set_color, ":interact", 0x0000FF),

    # -- Unnecessary due to :interact mesh:
    # (troop_set_slot, "trp_yael_array_d", ":bg", ":trp"),
    # (troop_set_slot, "trp_yael_array_c", ":bg", ":slotno"),
    # (troop_set_slot, "trp_yael_array_b", ":bg", ot_itemslot),

    [try_begin, [
      (neq, ":itmesh", -1),
      ("yael_set_overlay_info", ":itmesh", ot_item, ":trp", ":slotno", -1),
    ]],
    (assign, reg_ol_itmesh_x, ":xitem"),
    (assign, reg_ol_itmesh_y, ":yitem"),
    ("yael_set_overlay_info", ":interact", ot_item_interact, ":trp", ":slotno", ":itmesh"),

    (assign, reg1, ":bg"),
    (assign, reg0, ":itmesh"),
    (assign, reg2, ":interact"),
  )),

  #### script_yael_imod_to_name, ITEM_MODIFIER -> s0
  ("yael_imod_to_name", y_script(
    (store_script_param, ":imod", 1),
    [y_progn,
     [(try_begin), (eq, 1, 0)], # noop for code-generation
     [[y_progn, [(else_try), (eq, ":imod", imod_value), (str_store_string, s0, "@" + imod_name[5:])]]
      for imod_name, imod_value in globals().items()
      if imod_name.startswith('imod_')]],
    (else_try), (str_store_string, s0, "@INVALID_IMOD"),
    (try_end),
  )),

  #### script_yael_itype_to_name, STR_REG, ITEMTYPE
  # Store name of item type (see header items, itp_type_*) in the given string register.
  ("yael_itype_to_name", y_script(
    (store_script_param, ":reg", 1),
    (store_script_param, ":type",  2),
    [y_progn,
     [(try_begin), (eq, 1, 0)], # noop for code-generation
     [[y_progn, [(else_try), (eq, ":type", value), (str_store_string, ":reg", "@" + name)]]
      for name, value in globals().items()
      if name.startswith('itp_type_')]],
    (else_try), (str_store_string, s0, "@INVALID_TYPE"),
    (try_end),
  )),
  
  #### script_yael_describe_inventory_slot, TROOP, SLOT -> s0, ; Uses s1..s4
  ("yael_describe_inventory_slot", y_script(
    (store_script_param, ":troop", 1),
    (store_script_param, ":slot", 2),

    [try_begin,[
      (eq, ":troop", -1),
      (assign, ":item_id", -1),
      (assign, ":imod", -1),
      (assign, ":amount", -1),
    ],[
      (troop_get_inventory_slot, ":item_id", ":troop", ":slot"),
      (troop_get_inventory_slot_modifier, ":imod", ":troop", ":slot"),
      (troop_inventory_slot_get_item_amount, ":amount", ":troop", ":slot"),
    ]],

    [try_for_range, ":s", s0, s4, [(str_clear, ":s")]],

    [try_begin,[
      (eq, ":troop", -1),
      (str_store_string, s1, "@INV_TROOP"),
    ],[
      (str_store_troop_name, s1, ":troop"),
    ]],
    (assign, reg1, ":troop"),

    (assign, reg2, ":slot"),
    ("yael_imod_to_name", ":imod"), (str_store_string_reg, s3, s0),
    (assign, reg3, ":imod"),
    [try_begin, [
      (eq, ":item_id", -1),
      (str_store_string, s4, "@INV_ITEM"),
    ],[
      (str_store_item_name, s4, ":item_id"),
    ]],
    (assign, reg4, ":item_id"),
    (assign, reg5, ":amount"),
    [try_begin, [
      (neq, ":item_id", -1),
      (item_get_type, reg6, ":item_id"),
      (item_get_slot, reg7, ":item_id", slot_item_food_bonus),
      (item_get_difficulty, reg8, ":item_id"), 
    ],[
      (assign, reg6, -1),
      (assign, reg7, -1),
      (assign, reg8, -1),
    ]],
    ("yael_itype_to_name", s6, reg6),


    (str_store_string, s0, (
      "@{s1}({reg1}), {reg2}, {reg5} x {s4}({reg4}), {s3}({reg3}), {s6}({reg6}), fb({reg7}), d({reg8})")),

    [try_for_range, ":s", s1, s4, [(str_clear, ":s")]],
 )),

  #### script_yael_report_inventory_slot, TROOP, SLOT
  ("yael_report_inventory_slot", y_script(
    (store_script_param, ":troop", 1),
    (store_script_param, ":slot", 2),
    ("yael_describe_inventory_slot", ":troop", ":slot"),
    (display_message, s0),
  )),

  #### script_yael_troop_set_inventory_slot, TROOP, SLOT, ITEM_ID, ITEM_MOD, ITEM_AMOUNT
  ("yael_troop_set_inventory_slot", y_script(
    (store_script_param, ":trp", 1),
    (store_script_param, ":slot", 2),
    (store_script_param, ":id", 3),
    (store_script_param, ":imod", 4),
    (store_script_param, ":num", 5),
    
    ## debug message
    [try_begin, [
      (eq, "$cheat_mode", 1),
      (assign, reg1, ":trp"),
      (assign, reg2, ":slot"),
      (assign, reg3, ":id"),
      (assign, reg4, ":imod"),
      (assign, reg5, ":num"),
      (display_message, "@-- :trp {reg1}, :slot {reg2}, :id {reg3}, :imod {reg4}, :num {reg5}"),
    ]],
    
    (y_deflocal, "dump", ["::prefix"], [
      [try_begin,[
        (eq, "$cheat_mode", 1),
        ("yael_describe_inventory_slot", ":trp", ":slot"),
        (str_store_string, s1, "::prefix"),
        (display_message, "@{s0} - after {s1}"),
      ]],
    ]),
    
    ## Apply
    ("dump", "@start "),
    (troop_set_inventory_slot,             ":trp", ":slot", 0),
    (troop_set_inventory_slot_modifier,    ":trp", ":slot", 0),
    (troop_inventory_slot_set_item_amount, ":trp", ":slot", 0),
    (troop_set_inventory_slot,             ":trp", ":slot", ":id"),
    ("dump", "@id    "),
    (troop_set_inventory_slot_modifier,    ":trp", ":slot", ":imod"),
    ("dump", "@imod  "),
    [try_begin, [ # for amount-less items, setting this results in invalid item.
      [try_begin, [
        (neq, ":id", -1),
        (item_get_type, ":type", ":id"),
      ],[
        (assign, ":type", -1),
      ]],
      (this_or_next|eq, ":type", itp_type_arrows),
      (this_or_next|eq, ":type", itp_type_bolts),
      (this_or_next|eq, ":type", itp_type_thrown),
      (this_or_next|eq, ":type", itp_type_bullets),
      (this_or_next|eq, ":type", itp_type_arrows),
      (             eq, ":type", itp_type_goods),
      (troop_inventory_slot_set_item_amount, ":trp", ":slot", ":num"),
      ("dump", "@amount"),
    ]],
  )),

  #### script_yael_troop_eq_inventory_slot, TROOP, SLOT, ITEM_ID, ITEM_MOD, ITEM_AMOUNT -> reg0
  # Returns 1 if slot matches given values.
  # Returns 0 otherwise.
  ("yael_troop_eq_inventory_slot", y_script(
    (store_script_param, ":trp", 1),
    (store_script_param, ":slot", 2),
    (store_script_param, ":id", 3),
    (store_script_param, ":imod", 4),
    (store_script_param, ":num", 5),

    (troop_get_inventory_slot, ":a_id", ":trp", ":slot"),
    (troop_get_inventory_slot_modifier, ":a_imod", ":trp", ":slot"),
    (troop_inventory_slot_get_item_amount, ":a_num", ":trp", ":slot"),
    
    [try_begin,[
      (eq, ":id", ":a_id"),
      (eq, ":imod", ":a_imod"),
      (eq, ":num", ":a_num"),
      (assign, reg0, 1),
    ],[
      (assign, reg0, 0),
    ]],
  )),

  #### script_yael_item_allowed_in_slot, SLOTNO, ITEMID -> reg0
  # Returns 0 if no allowed, 1 if allowed.
  ("yael_item_allowed_in_slot", y_script(
    (store_script_param, ":slotno", 1),
    (store_script_param, ":itemid", 2),

    (assign, reg0, 0), 

    [try_begin, [
      (ge, ":itemid", 0),
      (item_get_type, ":type", ":itemid"),
    ],[
      (assign, ":type", -1),
    ]],

    [try_begin,[
      ## Negative item ID/slot number is always allowed 
      (this_or_next|lt, ":itemid", 0),
      (lt, ":slotno", 0),
      (assign, reg0, 1),
    ],[
      ## Slots 0-3: Hands
      (this_or_next|eq, ":slotno", ek_item_0),
      (this_or_next|eq, ":slotno", ek_item_1),
      (this_or_next|eq, ":slotno", ek_item_2),
      (             eq, ":slotno", ek_item_3),
      (this_or_next|eq, ":type", itp_type_one_handed_wpn),
      (this_or_next|eq, ":type", itp_type_two_handed_wpn),
      (this_or_next|eq, ":type", itp_type_polearm),
      (this_or_next|eq, ":type", itp_type_arrows),
      (this_or_next|eq, ":type", itp_type_bolts),
      (this_or_next|eq, ":type", itp_type_shield),
      (this_or_next|eq, ":type", itp_type_bow),
      (this_or_next|eq, ":type", itp_type_crossbow),
      (this_or_next|eq, ":type", itp_type_thrown),
      (this_or_next|eq, ":type", itp_type_pistol),
      (this_or_next|eq, ":type", itp_type_musket),
      (             eq, ":type", itp_type_bullets),
      (assign, reg0, 1),
    ],[
      (eq, ":slotno", ek_head),
      (eq, ":type", itp_type_head_armor),
      (assign, reg0, 1),
    ],[
      (eq, ":slotno", ek_body),
      (eq, ":type", itp_type_body_armor),
      (assign, reg0, 1),
    ],[
      (eq, ":slotno", ek_foot),
      (eq, ":type", itp_type_foot_armor),
      (assign, reg0, 1),
    ],[
      (eq, ":slotno", ek_gloves),
      (eq, ":type", itp_type_hand_armor),
      (assign, reg0, 1),
    ],[
      (eq, ":slotno", ek_horse),
      (eq, ":type", itp_type_horse),
      (assign, reg0, 1),
    ],[
      ## Slot ef_food unused by game, so we assume it is invalid.
      (eq, ":slotno", ek_food),
    ],[
      ## All items are allowed in "backpack".
      (gt, ":slotno", ek_food),
      (assign, reg0, 1),
    ],[
      ## Unexpected slot number. Assume disallowed.
    ]],
  )),

  #### script_yael_item_usable_by_troop, TROOP, ITEM_ID -> reg0
  # 1 if troup can use, according to stats.
  # 0 otherwise.
  ("yael_item_usable_by_troop", y_script(
    (store_script_param, ":trp", 1),
    (store_script_param, ":item_id", 2),
    
    [try_begin, [
      (neq, ":item_id", -1),
      (item_get_type, ":type", ":item_id"),
      (item_get_difficulty, ":diff", ":item_id"),
    ],[
      (assign, ":type", -1),
    ]],

    ## Depending on item type, obtain the correct item type.
    ## Unless known to depend on a specific skill, assume strengths.
    [try_begin, [
      (eq, ":type", itp_type_horse),
      (store_skill_level, ":stat", skl_riding, ":trp"),
      (str_store_string, s0, "@Riding"),
    ],[
      (eq, ":type", itp_type_bow),
      (store_skill_level, ":stat", skl_power_draw, ":trp"),
      (str_store_string, s0, "@Power Draw"),
    ],[
      (eq, ":type", itp_type_thrown),
      (store_skill_level, ":stat", skl_power_throw, ":trp"),
      (str_store_string, s0, "@Power Throw"),
    ],[
      (store_attribute_level, ":stat", ":trp", ca_strength),
      (str_store_string, s0, "@Strength"),      
    ]],

    [try_begin, [
      (gt, ":diff", 0),
      (assign, reg0, ":diff"),
      (overlay_set_text, "$yael_requirement_box", "@{s0} {reg0}"),
    ],[
      (overlay_set_text, "$yael_requirement_box", "@ "),
    ]],
    
    ## debug_start
    # [try_begin, [
    #   (eq, "$cheat_mode", 1),
    #   (str_store_troop_name, s1, ":trp"),
    #   (assign, reg1, ":stat"),
    #   (display_message, "@Requires {s0} ge {reg0}, has {reg1} ({s1})."),
    # ]],
    ## debug_end

    [try_begin,[
      (ge, ":stat", ":diff"),
      (assign, reg0, 1),
    ],[
      (assign, reg0, 0),
    ]],
  )),

  #### script_yael_troop_swap_inventory_slots, TRP1, SLOT1, TRP2, SLOT2 -> reg0
  # Swap inventory slots between two troops.
  # Returns "0" on success, some other value on failure, 
  # without guaranteed completeness:
  #   - 1: Somehow exited unexpectedly, without setting reg0 properly.
  #   - 2: Would have assigned an item that wasn't suitable for the slot (e.g. weapon to helmet slot)
  #   - 3: Internal error: Assignment resulted in unexpected slot contents. 
  #                        Previous should be restored. 
  #   - 4: Character doesn't meet skill/stats requirements of item.
  ("yael_troop_swap_inventory_slots", y_script(
    (store_script_param, ":trp1", 1),
    (store_script_param, ":slo1", 2),
    (store_script_param, ":trp2", 3),
    (store_script_param, ":slo2", 4),

    (assign, ":err_noerror_success", 0),
    (assign, ":err_unexpected_exit", 1),
    (assign, ":err_not_allowed_in_slot", 2),
    (assign, ":err_swap_failed", 3),
    (assign, ":err_stats_too_low", 4),

    (assign, reg0, ":err_unexpected_exit"),

    (troop_get_inventory_slot, ":ite1", ":trp1", ":slo1"),
    (troop_get_inventory_slot, ":ite2", ":trp2", ":slo2"),
    (troop_get_inventory_slot_modifier, ":mod1", ":trp1", ":slo1"),
    (troop_get_inventory_slot_modifier, ":mod2", ":trp2", ":slo2"),
    (troop_inventory_slot_get_item_amount, ":num1", ":trp1", ":slo1"),
    (troop_inventory_slot_get_item_amount, ":num2", ":trp2", ":slo2"),

    [try_begin,[
      ## Check if item is allowed in the slot.
      ("yael_item_allowed_in_slot", ":slo2", ":ite1"), (assign, ":c1", reg0),
      ("yael_item_allowed_in_slot", ":slo1", ":ite2"), (assign, ":c2", reg0),
      (this_or_next|eq, ":c1", 0), (eq, ":c2", 0),
      (assign, reg0, ":err_not_allowed_in_slot"),
    ],[
      ## Check if stats are sufficient - only for equipment slots!
      ("yael_item_usable_by_troop", ":trp1", ":ite2"), (assign, ":canuse1", reg0),
      ("yael_item_usable_by_troop", ":trp2", ":ite1"), (assign, ":canuse2", reg0),
      [try_begin, [
        (lt, ":slo1", 10),
        (eq, ":canuse1", 0),
        (assign, reg0, ":err_stats_too_low"),
      ],[
        (lt, ":slo2", 10),
        (eq, ":canuse2", 0),
        (assign, reg0, ":err_stats_too_low"),
      ]],
      (neq, reg0, ":err_unexpected_exit"),
    ],[
      ## Swap contents
      ("yael_troop_set_inventory_slot", ":trp1", ":slo1", ":ite2", ":mod2", ":num2"),
      ("yael_troop_set_inventory_slot", ":trp2", ":slo2", ":ite1", ":mod1", ":num1"),
      ## Verifiy correctness of contents
      [try_begin, [
        ("yael_troop_eq_inventory_slot", ":trp1", ":slo1", ":ite2", ":mod2", ":num2"), 
        (this_or_next|eq, reg0, 0),
        ("yael_troop_eq_inventory_slot", ":trp2", ":slo2", ":ite1", ":mod1", ":num1"),
        (eq, reg0, 0),
        ("yael_troop_set_inventory_slot", ":trp1", ":slo1", ":ite1", ":mod1", ":num1"),
        ("yael_troop_set_inventory_slot", ":trp2", ":slo2", ":ite2", ":mod2", ":num2"),
        (assign, reg0, ":err_swap_failed"),
      ],[
        (assign, reg0, ":err_noerror_success"),
      ]],
    ]],

    [try_begin, [
      (eq, "$cheat_mode", 1),
      [try_begin, [(eq,0,1),
      ],[(eq, reg0, ":err_noerror_success"), (str_store_string, s0, "@:err_noerror_success"),
      ],[(eq, reg0, ":err_unexpected_exit"), (str_store_string, s0, "@:err_unexpected_exit"),
      ],[(eq, reg0, ":err_not_allowed_in_slot"), (str_store_string, s0, "@:err_not_allowed_in_slot"),
      ],[(eq, reg0, ":err_swap_failed"), (str_store_string, s0, "@:err_swap_failed"),
      ],[(eq, reg0, ":err_stats_too_low"), (str_store_string, s0, "@:err_stats_too_low"),
      ],[(str_store_string, s0, "@UNDEF_ERR")
      ]],
      (display_message, "@Item swap failure: Errorcode {reg0} ({s0})"),
    ]],
  )),

  #### END

]

if False:
  for (name, script) in scripts:
    print('(', repr(name), ',')
    y_pprint_script(script)
    print('),')
