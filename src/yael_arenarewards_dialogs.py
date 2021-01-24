# -*- coding: us-ascii -*-


#### HEADER
from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *
from module_constants import *

#### MOD

from yael_util import *

print '  ' + __name__


def modmerge(var_set):
    from traceback import print_exc
    try:
        dialogs = var_set['dialogs']

        #### For each arena-result dialog identify the tier, and patch the experience amount.

        result_dialogs = [
            diag for diag in dialogs
            if diag[1] == 'arena_master_fight_result' ]

        y_dump_tree(result_dialogs)

        for diag in result_dialogs:            
            diag[5][0:0] = [
                (store_mul, ":yael_arenarewards_exp", "$g_arena_training_kills", yael_arena_exp_per_enemy),
                (add_xp_to_troop,":yael_arenarewards_exp", "trp_player"),
            ]

    except:
        print_exc()
