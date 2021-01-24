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

print '  yael_ransomtavern_dialogs.py'

TAVERNKEEP_INSERT_DIALOGS = [
    [
        anyone|plyr, 
        "tavernkeeper_talk", 
        [
            # (display_message, "@I am testing if this is applicable."),
            (is_between, "$g_talk_troop", tavernkeepers_begin, tavernkeepers_end)
        ],
        "Can I pay my bill in dish-washers?",
        "ransom_broker_sell_prisoners",
        [
            ## Fake identity of the tavern keeper; Seems to work as intended.
            ## NOTE: Cannot use (change_screen_trade_prisoners) here directly, 
            ## has to go through the ransom_broker_sell_prisoners dialog to work.
            (assign, ":actual_troop", "$g_talk_troop"),
            (assign, "$g_talk_troop", ransom_brokers_begin),
        ],
        []
    ]
]

def modmerge(var_set):
    from traceback import print_exc
    try:
        dialogs = var_set['dialogs']

        #### Find the close_window option for tavern keepers.
    
        index,close_dialog = [
            (index,diag) for index,diag in enumerate(dialogs)
            if diag[1] == 'tavernkeeper_talk'
            and diag[4] == 'close_window'
        ][-1]
        
        #### Insert dialog before the 'close_window' dialog option.
        dialogs[index:index] = TAVERNKEEP_INSERT_DIALOGS

    except:
        print_exc()
