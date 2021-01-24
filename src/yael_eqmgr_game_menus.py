from __future__ import print_function

#### HEADER

from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################


#### MOD CODE

from traceback import print_exc
from pprint import pprint
from yael_util import *


EQMGR_PATH = ('camp', 5, 'resume_travelling')
EQMGR_OPTION = (
    'yael_eqmgr_open',
    [],
    "Manage equipment",
    [
        (assign, "$g_yael_eqmgr_state", 0),
        (jump_to_menu, "mnu_yael_eqmgr_dummy_menu"),
    ],
)

EXTRA_MENUS = [
    ("yael_eqmgr_dummy_menu", 0, "Dummy. Shouldn't be seen.", "none", 
     [
         (call_script, "script_yael_eqmgr_dummy_menu"),
     ], 
     [
        ("yael_eqmgr_dummy_leave", [], "Leave.", [(jump_to_menu, "mnu_camp"),])
     ]
    ),
]



def modmerge(var_set):
    try:
        print('  ' + __name__)
        game_menus = var_set['game_menus']

        y_insert(game_menus, 'before', EQMGR_PATH, EQMGR_OPTION)

        game_menus.extend(EXTRA_MENUS)
        
    except:
        print_exc()
