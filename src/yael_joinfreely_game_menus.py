from __future__ import print_function

#### HEADER

from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from module_constants import *

#### MOD CODE

from traceback import print_exc
from pprint import pprint
from yael_util import *

print('  ' + __name__)

game_menus = [ 
  ( # Copied from module_game_menus, removed the checks, added relation-ship feedback.
    "pre_join",0,
    "You come across a battle between {s2}({reg2}) and {s1}({reg1}). You decide to...",
    "none",
    [
        (str_store_party_name, 1,"$g_encountered_party"),
        (str_store_party_name, 2,"$g_encountered_party_2"),
        (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
        (store_relation, reg2, ":attacker_faction", "fac_player_supporters_faction"),
        (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
        (store_relation, reg1, ":defender_faction", "fac_player_supporters_faction"),
      ],
    [
      ("pre_join_help_attackers",[
          ],
          "Move in to help the {s2}.",[
              (select_enemy,0),
              (assign,"$g_enemy_party","$g_encountered_party"),
              (assign,"$g_ally_party","$g_encountered_party_2"),
              (jump_to_menu,"mnu_join_battle")]),
      ("pre_join_help_defenders",[
          ],
          "Rush to the aid of the {s1}.",[
              (select_enemy,1),
              (assign,"$g_enemy_party","$g_encountered_party_2"),
              (assign,"$g_ally_party","$g_encountered_party"),
              (jump_to_menu,"mnu_join_battle")]),
      ("pre_join_leave",[],"Don't get involved.",[(leave_encounter),(change_screen_return)]),
    ]
  ),

]
