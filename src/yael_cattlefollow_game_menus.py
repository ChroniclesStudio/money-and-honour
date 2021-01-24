from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from module_constants import *

from yael_util import *
from pprint import pprint

def modmerge(var_set):
    try:
        game_menus = var_set['game_menus']
        y_insert(
            game_menus,
            'before',('cattle_herd',5,'cattle_drive_away'),
            (
                "yael_cattlefollow",
                [],
                "Have your men keep the cattle close.",
                [
                    (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 1),
                    (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_escort_party),
                    (party_set_ai_object,"$g_encountered_party", "p_main_party"),
                    (change_screen_return),
                ]
            ))

        # pprint(y_get_path(game_menus,('cattle_herd',5)))
    except Exception as e:
        print(e)
        import traceback
        print traceback.print_exc()

