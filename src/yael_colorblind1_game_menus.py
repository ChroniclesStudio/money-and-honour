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

SCRIPT_INSERT_PATTERN = [
    # Replace snippet: Used to shuffle team colors.
    # At this point participants are already randomized in order
    # and implicitly assigned to teams (for 3 teams and 24 participants, 
    # team '0' is 0-7, team '1' is 8-15, etc.).
    (try_for_range, ":slot_no", 0, 4),#shuffle teams
      (troop_set_slot, "trp_temp_array_b", ":slot_no", ":slot_no"),
    (try_end),
    (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 4),
]

def modmerge(var_set):
    try:
        print('  yael_colorblind1_game_menus.py')
        game_menus = var_set['game_menus']
        script = y_get_path(game_menus, ('town_tournament', 5, 'tournament_join_next_fight',3))

        ## Add debug option for joining tournament in ``cheatmenu`` mode.
        ## BEWARE: Must add at end of the list, otherwise it messes 
        ## up doors!
        join_tournament = y_get_path(game_menus, ('town', 5, 'join_tournament'))
        cheat_join_tournament = (
            'join_tournament_yael',
            [(eq,"$cheat_mode",1)],
            'CHEAT! Tournament (Yael)', # what is the {!} for?
            join_tournament[3], # Copy script part from original join_tournament option
        )
        y_insert(game_menus, 'end', ('town', 5), cheat_join_tournament)

        ## Make sure that colors are no problem.
        y_replace_sequence_range(
            tree = script,
            pattern = SCRIPT_INSERT_PATTERN, 
            replacement = (
                SCRIPT_INSERT_PATTERN + # Keep pattern in case other mods need it.
                [
                    # Put into script to prevent name clash of local variables.
                    (call_script, "script_yael_colorblind1_teamcolors")
                ]
            )
        )

        # y_pprint_script(script)
        # 
        # y_dump_tree(game_menus)


    except:
        print_exc()
