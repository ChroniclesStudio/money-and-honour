# -*- coding: us-ascii -*-

from __future__ import print_function

#### SETTINGS

## LIST OF QUEST IDS TO DISABLE.
## 
## Only works for randomized quests, which are started by a dialog for
## which the condition block has the form
## 
##     [(eq, "$random_quest_no", qst_SOME_ID), ...
## 
## Subsequently a list of such quest IDs I found. Uncomment to disable
## the quest, comment out to enable the quest. Some of them might not
## actually be enabled in the game.
DISABLED_QUEST_IDS = [
    # "qst_rescue_prisoner",                        # [(eq,"$random_quest_no","qst_rescue_prisoner"), ...
    # "qst_deliver_message",                        # [(eq,"$random_quest_no","qst_deliver_message"), ...
    # "qst_deliver_message_to_enemy_lord",          # [(eq,"$random_quest_no","qst_deliver_message_to_enemy_lord"), ...
    # "qst_escort_lady",                            # [(eq,"$random_quest_no","qst_escort_lady"), ...
    # "qst_hunt_down_raiders",                      # [(eq,"$random_quest_no","qst_hunt_down_raiders"), ...
    # "qst_bring_back_deserters",                   # [(eq,"$random_quest_no","qst_bring_back_deserters"), ...
    # "qst_deliver_supply_to_center_under_siege",   # [(eq,"$random_quest_no","qst_deliver_supply_to_center_under_siege"), ...
    # "qst_bring_reinforcements_to_siege",          # [(eq,"$random_quest_no","qst_bring_reinforcements_to_siege"), ...
    # "qst_rescue_lady_under_siege",                # [(eq,"$random_quest_no","qst_rescue_lady_under_siege"), ...
    # "qst_bring_prisoners_to_enemy",               # [(eq,"$random_quest_no","qst_bring_prisoners_to_enemy"), ...
    # "qst_deal_with_bandits_at_lords_village",     # [(eq,"$random_quest_no","qst_deal_with_bandits_at_lords_village"), ...
    # "qst_raise_troops",                           # [(eq,"$random_quest_no","qst_raise_troops"), ...
    # "qst_collect_taxes",                          # [(eq,"$random_quest_no","qst_collect_taxes"), ...
    # "qst_hunt_down_fugitive",                     # [(eq,"$random_quest_no","qst_hunt_down_fugitive"), ...
    # "qst_capture_messenger",                      # [(eq,"$random_quest_no","qst_capture_messenger"), ...
    # "qst_kill_local_merchant",                    # [(eq,"$random_quest_no","qst_kill_local_merchant"), ...
    # "qst_meet_spy_in_enemy_town",                 # [(eq,"$random_quest_no","qst_meet_spy_in_enemy_town"), ...
    # "qst_cause_provocation",                      # [(eq,"$random_quest_no","qst_cause_provocation"), ...
    # "qst_bring_back_runaway_serfs",               # [(eq,"$random_quest_no","qst_bring_back_runaway_serfs"), ...
    # "qst_follow_spy",                             # [(eq,"$random_quest_no","qst_follow_spy"), ...
    # "qst_capture_enemy_hero",                     # [(eq,"$random_quest_no","qst_capture_enemy_hero"), ...
    # "qst_lend_companion",                         # [(eq,"$random_quest_no","qst_lend_companion"), ...
    # "qst_collect_debt",                           # [(eq,"$random_quest_no","qst_collect_debt"), ...
    # "qst_capture_conspirators",                   # [(eq,"$random_quest_no","qst_capture_conspirators"), ...
    # "qst_defend_nobles_against_peasants",         # [(eq,"$random_quest_no","qst_defend_nobles_against_peasants"), ...
    # "qst_incriminate_loyal_commander",            # [(eq, "$random_quest_no", "qst_incriminate_loyal_commander"), ...
    # "qst_capture_prisoners",                      # [(eq,"$random_quest_no","qst_capture_prisoners"), ...
    # "qst_lend_surgeon",                           # [(eq,"$random_quest_no","qst_lend_surgeon"), ...
    # "qst_duel_for_lady",                          # [(eq, "$random_quest_no", "qst_duel_for_lady"), ...
    # "qst_deliver_grain",                          # [(eq,"$random_quest_no","qst_deliver_grain"), ...
    # "qst_train_peasants_against_bandits",         # [(eq,"$random_quest_no", "qst_train_peasants_against_bandits"), ...
    # "qst_deliver_cattle",                         # [(eq,"$random_quest_no","qst_deliver_cattle"), ...
]

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


#### MODULE CODE

from yael_util import *


def modmerge(var_set):
    print('  yael_disablequests_dialogs.py')
    dialogs = var_set['dialogs']

    conditions_to_remove = [
        (eq, "$random_quest_no", id)
        for id in DISABLED_QUEST_IDS ]
    dialogs_to_remove = [
        dialog for dialog in dialogs
        if len(dialog[2]) > 0
        and dialog[2][0] in conditions_to_remove ]
    ellipsis = y_symbol('...')

    for dialog in dialogs_to_remove:
        quest_id = [
            cond for cond in conditions_to_remove
            if dialog[2][0] == cond 
        ][0]
        print('    Disabling dialog', repr([
            dialog[0], dialog[1], [cond, ellipsis], ellipsis]))
        # dialogs.remove(dialog) # plain removal breaks it; Instead give it an always-failing condition.
        dialog[2][0] = (eq, 1, 2)
