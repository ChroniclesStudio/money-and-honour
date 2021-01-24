from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *

from yael_util import *

print("  yael_colorblind1_scripts.py")

scripts = [
    # script_yael_colorblind1_teamcolors
    ("yael_colorblind1_teamcolors", [
        #### IDEA
        ## Make sure that unless there are four teams, never both
        ## green and red occur, as those are hardest to distinguish
        ## with color-blindness.
        ## 
        ## Then make sure that IF both are necessary (4 teams), 
        ## the player is gold or blue.
        ## 
        ## NOTE: Colors are red(0), blue(1), green(2), gold(3)
        ## Color assignment per team (0,1,2,3) is stored in trp_temp_array_b
        ## and randomized when this script is called.
        ## 
        ## Likewise, the order of participants is randomized in
        ## trp_temp_array_a, and their team number is
        ## floor(position/teamsize)
        (try_begin),
          (eq,"$cheat_mode",1), 
          (display_message,"@YAEL BEGIN - colorblind team fix"),
        (try_end),
                
        #### Set up fixed team order "blue,gold,red,green"
        (troop_set_slot,"trp_temp_array_b",0,1), # team 0 = blue
        (troop_set_slot,"trp_temp_array_b",1,3), # team 1 = gold
        (troop_set_slot,"trp_temp_array_b",2,0), # team 2 = red
        (troop_set_slot,"trp_temp_array_b",3,2), # team 3 = green

        #### Randomize whether team 3 is green or red.
        (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 2,4),

        #### Determine current index of player.
        (try_for_range, ":slot_no", 0, "$g_tournament_num_participants_for_fight"),
          (troop_get_slot, ":troop_id", "trp_temp_array_a", ":slot_no"),
          (try_begin),
            (eq, ":troop_id", "trp_player"),
            (assign, ":slot_no_player", ":slot_no"),
          (try_end),
        (try_end),
        
        #### Swap player with random slot from blue and gold teams.
        # Randomly select slot
        (store_mul, ":team_1_end", 2, "$g_tournament_next_team_size"),
        (store_random_in_range, ":slot_no_swap", 0, ":team_1_end"),
        # Swap operation.
        (troop_get_slot,":trp_swap","trp_temp_array_a",":slot_no_swap"),
        (troop_set_slot,"trp_temp_array_a",":slot_no_swap", "trp_player"),
        (troop_set_slot,"trp_temp_array_a",":slot_no_player", ":trp_swap"),

        #### When four teams, randomize colors between blue and gold only.
        (try_begin),
          (ge, "$g_tournament_next_num_teams", 4), # ge in case some mod is using more than 4.
          (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 2),
        #### With three or less teams, randomize between first three colors.
        # I.e. between blue,gold, and whichever of red,green was chosen above.
        (else_try),
          (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 3),
        (try_end), 
        
        #### DEBUG OUTPUT
        (try_begin),
          (eq,"$cheat_mode",1),
          #### List order of colors
          (troop_get_slot, reg1, "trp_temp_array_b", 0),
          (troop_get_slot, reg2, "trp_temp_array_b", 1),
          (troop_get_slot, reg3, "trp_temp_array_b", 2),
          (troop_get_slot, reg4, "trp_temp_array_b", 3),
          (display_message, "@YAEL Color Order {reg1},{reg2},{reg3},{reg4}"),
          #### List Participants
          (try_for_range, ":slot_no", 0, "$g_tournament_num_participants_for_fight"),
            (store_div, ":team_no", ":slot_no", "$g_tournament_next_team_size"),
            (try_begin),
              (store_mod, reg1, ":slot_no", "$g_tournament_next_team_size"),
              (eq, reg1, 0),
              # Determine team color
              (troop_get_slot, reg2, "trp_temp_array_b", ":team_no"),
              (try_begin), (eq,reg2,0), (str_store_string,s2,"@red"),
              (else_try),  (eq,reg2,1), (str_store_string,s2,"@blue"),
              (else_try),  (eq,reg2,2), (str_store_string,s2,"@green"),
              (else_try),  (eq,reg2,3), (str_store_string,s2,"@gold"),
              (else_try),               (str_store_string,s2,"@INVALID_COLOR"),
              (try_end),
              (assign, reg1, ":team_no"),
              (display_message, "@YAEL ---- Team {reg1}, color {s2}({reg2})"),
            (try_end),
            (troop_get_slot,":troop_id","trp_temp_array_a",":slot_no"),
            (str_store_troop_name,s1,":troop_id"),
            (assign, reg1, ":slot_no"),
            (assign, reg2, ":troop_id"),
            (try_begin), (eq,":troop_id", "trp_player"), 
              (str_store_string, s2, "@ (PLAYER)"),
            (else_try),
              (str_clear, s2),
            (try_end),
            (display_message,"@YAEL slot {reg1}, troop {reg2}, {s1}{s2}"),
          (try_end),
          #### Goodbye message
          (display_message,"@YAEL END - colorblind team fix"),
        (try_end),

    ]),
]
