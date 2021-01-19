# POLITICAL (1.2) by Lazeras
# Released 1 December 2014
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

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

# Manualy all lines under the `scripts` into the bottom of the module_scripts at the bottom of the file
scripts = [
#KAOS (POLITICAL)  

########################################################################################################################
#  OVER WRITING OF SCRIPTS                                                                                             #
########################################################################################################################


  #script_game_get_troop_note
  # This script is called from the game engine when the notes of a troop is needed.
  # INPUT: arg1 = troop_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_troop_note",
    [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":note_index"),
      (set_trigger_result, 0),

      (str_store_troop_name, s54, ":troop_no"),
      (try_begin),
        (eq, ":troop_no", "trp_player"),
        (this_or_next|eq, "$player_has_homage", 1),
        (eq, "$players_kingdom", "fac_player_supporters_faction"),
        (assign, ":troop_faction", "$players_kingdom"),
      (else_try),
        (store_troop_faction, ":troop_faction", ":troop_no"),
    

    
      (try_end),
      (str_clear, s49),
    
    #Family notes
      (try_begin),
        #(this_or_next|is_between, ":troop_no", lords_begin, kingdom_ladies_end),
      #KAOS  (POLITICAL)
      (this_or_next|is_between, ":troop_no", active_npcs_begin, kingdom_ladies_end),
      #KAOS  (POLITICAL)
        (eq, ":troop_no", "trp_player"),
        (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
        (assign, ":num_relations", 0),

        (try_begin),
          (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
          (gt, reg0, 0),
          (val_add, ":num_relations", 1),
        (try_end),
        (try_for_range, ":aristocrat", active_npcs_begin, kingdom_ladies_end),
        (this_or_next|troop_slot_eq, ":aristocrat", slot_troop_occupation, slto_kingdom_hero),
        (troop_slot_eq, ":aristocrat", slot_troop_occupation, slto_kingdom_lady),
          (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
          (gt, reg0, 0),
          (val_add, ":num_relations", 1),
        (try_end),
        (try_begin),
          (gt, ":num_relations", 0),
          (try_begin),
            (eq, ":troop_no", "trp_player"),
            (str_store_string, s49, "str__family_"),
          (else_try),
            (troop_get_slot, reg1, ":troop_no", slot_troop_age),
            (str_store_string, s49, "str__age_reg1_family_"),
          (try_end),
          (try_begin),
            (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
            (gt, reg0, 0),
            (str_store_troop_name_link, s12, "trp_player"),
            (val_sub, ":num_relations", 1),
            (try_begin),
              (eq, ":num_relations", 0),
              (str_store_string, s49, "str_s49_s12_s11_end"),
            (else_try),
              (str_store_string, s49, "str_s49_s12_s11"),
            (try_end),
          (try_end),
          (try_for_range, ":aristocrat", active_npcs_begin, kingdom_ladies_end),
        (this_or_next|troop_slot_eq, ":aristocrat", slot_troop_occupation, slto_kingdom_hero),
        (troop_slot_eq, ":aristocrat", slot_troop_occupation, slto_kingdom_lady),
            (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
            (gt, reg0, 0),
            (try_begin),
              (neg|is_between, ":aristocrat", kingdom_ladies_begin, kingdom_ladies_end),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name_link, s12, ":aristocrat"),
              (call_script, "script_troop_get_relation_with_troop", ":aristocrat", ":troop_no"),
              (str_store_string, s49, "str_s49_s12_s11_rel_reg0"),
            (else_try),
              (str_store_troop_name_link, s12, ":aristocrat"),
              (val_sub, ":num_relations", 1),
              (try_begin),
                (eq, ":num_relations", 0),
                (str_store_string, s49, "str_s49_s12_s11_end"),
              (else_try),
                (str_store_string, s49, "str_s49_s12_s11"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
      
      (try_begin),
        (neq, ":troop_no", "trp_player"),
        (neg|is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
        (neg|is_between, ":troop_no", companions_begin, companions_end),
        (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),

        (try_begin),
          (eq, ":note_index", 0),
          (str_store_string, s0, "str_s54_has_left_the_realm"),
          (set_trigger_result, 1),
        (else_try),
          (str_clear, s0),
          (this_or_next|eq, ":note_index", 1),
          (eq, ":note_index", 2),
          (set_trigger_result, 1),
        (try_end),

      (else_try),
        (is_between, ":troop_no", companions_begin, companions_end),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (eq, ":note_index", 0),
        (set_trigger_result, 1),
        (str_clear, s0),
        (assign, ":companion", ":troop_no"),
        (str_store_troop_name, s4, ":companion"),
        (try_begin),
      (troop_get_slot, ":days_left", ":companion", slot_troop_days_on_mission),

      (this_or_next|main_party_has_troop, ":companion"),
      (this_or_next|troop_slot_ge, ":companion", slot_troop_current_mission, 1),
        (eq, "$g_player_minister", ":companion"),

      (try_begin),
        (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_kingsupport),
        (str_store_string, s8, "str_gathering_support"),
        (try_begin),
          (eq, ":days_left", 1),
          (str_store_string, s5, "str_expected_back_imminently"),
        (else_try), 
          (assign, reg3, ":days_left"),
          (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
        (try_end),
      (else_try),
        (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_gather_intel),
        (troop_get_slot, ":town_with_contacts", ":companion", slot_troop_town_with_contacts),
        (str_store_party_name, s11, ":town_with_contacts"),
        
        (str_store_string, s8, "str_gathering_intelligence"),
        (try_begin),
          (eq, ":days_left", 1),
          (str_store_string, s5, "str_expected_back_imminently"),
        (else_try), 
          (assign, reg3, ":days_left"),
          (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
        (try_end),
      (else_try), 
        
        (troop_slot_ge, ":companion", slot_troop_current_mission, npc_mission_peace_request),
        (neg|troop_slot_ge, ":companion", slot_troop_current_mission, 8),

        (troop_get_slot, ":faction", ":companion", slot_troop_mission_object),
        (str_store_faction_name, s9, ":faction"),
        (str_store_string, s8, "str_diplomatic_embassy_to_s9"),
        (try_begin),
          (eq, ":days_left", 1),
          (str_store_string, s5, "str_expected_back_imminently"),
        (else_try), 
          (assign, reg3, ":days_left"),
          (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
        (try_end),
      (else_try),
        (eq, ":companion", "$g_player_minister"),
        (str_store_string, s8, "str_serving_as_minister"),
        (str_store_party_name, s9, "$g_player_court"),
        (is_between, "$g_player_court", centers_begin, centers_end),
        (str_store_string, s5, "str_in_your_court_at_s9"),
      (else_try),
        (eq, ":companion", "$g_player_minister"),
        (str_store_string, s8, "str_serving_as_minister"),
        (str_store_string, s5, "str_awaiting_the_capture_of_a_fortress_which_can_serve_as_your_court"),
      (else_try),
        (main_party_has_troop, ":companion"),
        (str_store_string, s8, "str_under_arms"),
        (str_store_string, s5, "str_in_your_party"),
      (try_end),  
      
      (str_store_string, s0, "str_s4_s8_s5"),
      
    (else_try),
      (str_store_string, s0, "str_whereabouts_unknown"),
    (try_end),
    
    
    (else_try),
        (is_between, ":troop_no", pretenders_begin, pretenders_end),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neq, ":troop_no", "$supported_pretender"),
#####################  debugging messages ################################
        (try_begin),    
            (eq, "$kaos_debug_mode", 1),
            (str_store_troop_name, s54, ":troop_no"),
            (troop_get_slot, ":cur_center", ":troop_no", slot_troop_cur_center),
            (str_store_party_name, s55, ":cur_center"),
            (display_log_message, "@{s54} is currently at {s55}", 0xFF0000),
        (try_end),    
#####################  debugging messages ################################
        (troop_get_slot, ":orig_faction", ":troop_no", slot_troop_original_faction),
        (try_begin),
          (faction_slot_eq, ":orig_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":orig_faction", slot_faction_has_rebellion_chance, 1),
          (try_begin),
            (eq, ":note_index", 0),
            (str_store_faction_name_link, s56, ":orig_faction"),
            (str_store_string, s0, "@{s54} is a claimant to the throne of {s56}.", 0),
            (set_trigger_result, 1),
          (try_end),
        (else_try),
          (try_begin),
            (str_clear, s0),
            (this_or_next|eq, ":note_index", 0),
            (this_or_next|eq, ":note_index", 1),
            (eq, ":note_index", 2),
            (set_trigger_result, 1),
          (try_end),
        (try_end),
    
      (else_try),
        (try_begin),
          (eq, ":note_index", 0),
          (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
          (str_store_troop_name_link, s55, ":faction_leader"),
          (str_store_faction_name_link, s56, ":troop_faction"),
          (assign, ":troop_is_player_faction", 0),
          (assign, ":troop_is_faction_leader", 0),
          (try_begin),
            (eq, ":troop_faction", "fac_player_faction"),
            (assign, ":troop_is_player_faction", 1),
          (else_try),
            (eq, ":faction_leader", ":troop_no"),
            (assign, ":troop_is_faction_leader", 1),
          (try_end),
          (assign, ":num_centers", 0),
          (str_store_string, s58, "@nowhere"),
          (try_for_range_backwards, ":cur_center", centers_begin, centers_end),                     
            (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
            (try_begin),
              (eq, ":num_centers", 0),
              (str_store_party_name_link, s58, ":cur_center"),
            (else_try),
              (eq, ":num_centers", 1),
              (str_store_party_name_link, s57, ":cur_center"),
              (str_store_string, s58, "@{s57} and {s58}"),
            (else_try),
              (str_store_party_name_link, s57, ":cur_center"),
              (str_store_string, s58, "@{!}{s57}, {s58}"),
            (try_end),
            (val_add, ":num_centers", 1),
          (try_end),
          (troop_get_type, reg3, ":troop_no"),
          (troop_get_slot, reg5, ":troop_no", slot_troop_renown),
          (troop_get_slot, reg15, ":troop_no", slot_troop_controversy),
      
          (str_clear, s59),
          (try_begin),   
            (call_script, "script_troop_get_player_relation", ":troop_no"),
            (assign, ":relation", reg0),
            (store_add, ":normalized_relation", ":relation", 100),
            (val_add, ":normalized_relation", 5),
            (store_div, ":str_offset", ":normalized_relation", 10),
            (val_clamp, ":str_offset", 0, 20),
            (store_add, ":str_id", "str_relation_mnus_100_ns",  ":str_offset"),
            (neq, ":str_id", "str_relation_plus_0_ns"),
            (str_store_string, s60, "@{reg3?She:He}"),
            (str_store_string, s59, ":str_id"),
            (str_store_string, s59, "@{!}^{s59}"),
          (try_end),
          #lord recruitment changes begin
          #This sends a bunch of political information to s47.
    
          (try_begin),
              (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
              (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
              (assign, ":relation", reg0),
              (str_clear, s61),
              (assign, reg10, 0),
              (try_begin), # update reg10
                (this_or_next|gt, ":relation", 19),
                (lt, ":relation", -19),
                (assign, reg10, ":relation"),
                (store_add, ":normalized_relation", ":relation", 100),
                (store_div, ":str_offset", ":normalized_relation", 20),
                (val_clamp, ":str_offset", 0, 10), # does 10 work ? only 10 strings in there
                (store_add, ":str_rel_id", "str_ruler_relation_mnus_100_ns",  ":str_offset"),
                (str_store_string, s61, ":str_rel_id"),
              (try_end),
          (try_end),      


          #refresh registers
          (assign, reg9, ":num_centers"),
          (troop_get_type, reg3, ":troop_no"),
          (troop_get_slot, reg5, ":troop_no", slot_troop_renown),
          (assign, reg4, ":troop_is_faction_leader"),
          (assign, reg6, ":troop_is_player_faction"),
          
          (troop_get_slot, reg17, ":troop_no", slot_troop_wealth), #DEBUGS
          (str_store_string, s0, "str_lord_info_string", 0),
          #lord recruitment changes end
          (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
          (set_trigger_result, 1),
        (try_end),
      (try_end),
     ]),


  # script_troop_set_title_according_to_faction
  # Input: arg1 = troop_no, arg2 = faction_no
  # EDITED FROM NATIVE TO ALLOW CUSTOM PLAYER KINGDOM TITLES
  ("troop_set_title_according_to_faction",
    [
        (store_script_param, ":troop_no", 1),
        (store_script_param, ":faction_no", 2),
        
        (assign, ":custom_name", 0),
        (try_begin),
            (eq, "$kaos_use_custom_name", 1),
            (eq, ":faction_no", "fac_player_supporters_faction"),
            (troop_get_type, ":gender", ":troop_no"),
            (try_begin),
              (eq, ":gender", 0), #male
              (troop_slot_eq, "trp_heroes_end", 0, 1),
              (str_store_troop_name, s0, "trp_heroes_end"),
              (str_store_troop_name_plural, s1, ":troop_no"),
              (str_store_string, s1, "str_s0_s1"),
              (assign, ":custom_name", 1),              
            (else_try),
              (troop_slot_eq, "trp_heroes_end", 1, 1),
              (str_store_troop_name_plural, s0, "trp_heroes_end"),
              (str_store_troop_name_plural, s1, ":troop_no"),
              (str_store_string, s1, "str_s0_s1"),
              (assign, ":custom_name", 1),              
            (try_end),
            (eq, ":custom_name", 1), #So if it fails, will rename normally
        (else_try),
            (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":troop_no", ":faction_no"),
      (try_end),
      ]),

  #script_game_reset_player_party_name:
  # This script is called from the game engine when the player name is changed.
  # INPUT: none
  # OUTPUT: none
  ("game_reset_player_party_name",
    [
        (try_begin),
            (eq, "$kaos_use_custom_name", 1),
           #Caba`drin Custom Player Party Name
           (try_begin),                             
               (party_slot_eq, 0, 1, 0),                
               (str_store_troop_name, s5, "trp_player"),
               (party_set_name, "p_main_party", s5),
           (try_end), 
           #Caba`drin Custom Player Party Name
        (else_try),
            # Jrider + TITLES v0.0, init new titles
            (try_for_range, ":troop_no", active_npcs_begin, kingdom_ladies_end),
                (store_troop_faction, ":faction_no", ":troop_no"),
                (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":troop_no", ":faction_no"),
            (try_end),
            # Jrider -
        (try_end),

     ]
   ),
 
  # script_change_troop_faction
  # Input: arg1 = troop_no, arg2 = faction
  ("change_troop_faction",
    [
        (store_script_param_1, ":troop_no"),
        (store_script_param_2, ":faction_no"),

        (try_begin),
          #Reactivating inactive or defeated faction
          (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
          (neg|faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
          (faction_set_slot, ":faction_no", slot_faction_state, sfs_active),
          #(call_script, "script_store_average_center_value_per_faction"),
        (try_end),

        #Political ramifications
        (store_faction_of_troop, ":orig_faction", ":troop_no"),
        
        #remove if he is marshal
        (try_begin),
        (faction_slot_eq, ":orig_faction", slot_faction_marshall, ":troop_no"),
            (call_script, "script_check_and_finish_active_army_quests_for_faction", ":orig_faction"),       

        #No current issue on the agenda
        (try_begin),
          (faction_slot_eq, ":orig_faction", slot_faction_political_issue, 0),
        
          (faction_set_slot, ":orig_faction", slot_faction_political_issue, 1), #Appointment of marshal
          (store_current_hours, ":hours"),
          (val_max, ":hours", 0),
          (faction_set_slot, ":orig_faction", slot_faction_political_issue_time, ":hours"), #Appointment of marshal
          (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
            (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
            (eq, ":active_npc_faction", ":orig_faction"),
            (troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
          (try_end),    
          (try_begin),
            (eq, "$players_kingdom", ":orig_faction"),
            (troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
          (try_end),    
        (try_end),
        
            (try_begin),
          (troop_get_slot, ":old_marshall_party", ":troop_no", slot_troop_leaded_party),
              (party_is_active, ":old_marshall_party"),
              (party_set_marshall, ":old_marshall_party", 0),
            (try_end),  

        (faction_set_slot, ":orig_faction", slot_faction_marshall, -1),
        (try_end),
        #Removal as marshal ends
        
        #Other political ramifications
        (troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":active_npc", slot_troop_stance_on_faction_issue, ":troop_no"),
        (troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
        (try_end),
        #Political ramifications end
        
        
        (try_begin),
          (ge, "$cheat_mode", 1),
          (str_store_troop_name, s4, ":troop_no"),
          (display_message, "@{!}DEBUG - {s4} faction changed in normal faction change"), 
        (try_end),
        
          (troop_set_faction, ":troop_no", ":faction_no"),
          (troop_set_slot, ":troop_no", slot_troop_recruitment_random, 0),
          (troop_set_slot, ":troop_no", slot_lord_recruitment_argument, 0),
          (troop_set_slot, ":troop_no", slot_lord_recruitment_candidate, 0),
          (troop_set_slot, ":troop_no", slot_troop_promised_fief, 0),

          # Jrider + TITLES v0.0 moving this to end of script to compute according to new holdings
          #Give new title
          #(call_script, "script_troop_set_title_according_to_faction", ":troop_no", ":faction_no"),
          # Jrider -
          
          (try_begin),
            (this_or_next|eq, ":faction_no", "$players_kingdom"),
            (eq, ":faction_no", "fac_player_supporters_faction"),
            (call_script, "script_check_concilio_calradi_achievement"),
          (try_end),

        #Takes walled centers and dependent villages with him
          (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
            (party_set_faction, ":center_no", ":faction_no"),
            (try_for_range, ":village_no", villages_begin, villages_end),
              (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
              (party_set_faction, ":village_no", ":faction_no"),
              (party_get_slot, ":farmer_party_no", ":village_no", slot_village_farmer_party),
              (try_begin),
                (gt, ":farmer_party_no", 0),
                (party_is_active, ":farmer_party_no"),
                (party_set_faction, ":farmer_party_no", ":faction_no"),
              (try_end),
              (try_begin),
                (party_get_slot, ":old_town_lord", ":village_no", slot_town_lord),
                (neq, ":old_town_lord", ":troop_no"),
                (party_set_slot, ":village_no", slot_town_lord, stl_unassigned),
              (try_end),
            (try_end),
          (try_end),
        
        
        #Remove his control over villages under another fortress
          (try_for_range, ":village_no", villages_begin, villages_end),
            (party_slot_eq, ":village_no", slot_town_lord, ":troop_no"),
            (store_faction_of_party, ":village_faction", ":village_no"),
            (try_begin),
              (neq, ":village_faction", ":faction_no"),
              (party_set_slot, ":village_no", slot_town_lord, stl_unassigned),
            (try_end),
          (try_end),
        # Jrider + TITLES v0.0 Give new title
          (call_script, "script_troop_set_title_according_to_faction", ":troop_no", ":faction_no"),
          # Jrider -
        #Dependant kingdom ladies switch faction

        (try_for_range, ":kingdom_lady", kingdom_ladies_begin, kingdom_ladies_end),
        (call_script, "script_get_kingdom_lady_social_determinants", ":kingdom_lady"),
        (assign, ":closest_male_relative", reg0),
        (assign, ":new_center", reg1),
        
        (eq, ":closest_male_relative", ":troop_no"),
        
        (try_begin),
          (ge, "$cheat_mode", 1),
          (str_store_troop_name, s4, ":kingdom_lady"),
          (display_message, "@{!}DEBUG - {s4} faction changed by guardian moving"), 
        (try_end),
        
        (troop_set_faction, ":kingdom_lady", ":faction_no"),
        # Jrider + TITLES v0.0 change ladies title
            (call_script, "script_troop_set_title_according_to_faction", ":kingdom_lady", ":faction_no"),
            # Jrider -
        (troop_slot_eq, ":kingdom_lady", slot_troop_prisoner_of_party, -1),
        (troop_set_slot, ":kingdom_lady", slot_troop_cur_center, ":new_center"),
        (try_end),
        
        #Free prisoners
          (try_begin),
            (troop_get_slot, ":leaded_party", ":troop_no", slot_troop_leaded_party),
            (gt, ":leaded_party", 0),
            (party_set_faction, ":leaded_party", ":faction_no"),
            (party_get_num_prisoner_stacks, ":num_stacks", ":leaded_party"),
            (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
              (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":leaded_party", ":troop_iterator"),
              (store_troop_faction, ":cur_faction", ":cur_troop_id"),
              (troop_is_hero, ":cur_troop_id"),
              (eq, ":cur_faction", ":faction_no"),
              (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
              (party_remove_prisoners, ":leaded_party", ":cur_troop_id", 1),
            (try_end),
          (try_end),
        
        #Annull all quests of which the lord is giver
        (try_for_range, ":quest", all_quests_begin, all_quests_end),
        (check_quest_active, ":quest"),
        (quest_slot_eq, ":quest", slot_quest_giver_troop, ":troop_no"),
        
        (str_store_troop_name, s4, ":troop_no"),
        (try_begin),
          (eq, "$cheat_mode", 1),
            (display_message, "str_s4_changing_sides_aborts_quest"),
            (try_end),
        (call_script, "script_abort_quest", ":quest", 0),
        (try_end),
        
        #Boot all lords out of centers whose faction has changed
        (try_for_range, ":lord_to_move", active_npcs_begin, active_npcs_end),
        (troop_get_slot, ":lord_led_party", ":lord_to_move", slot_troop_leaded_party),
          (party_is_active, ":lord_led_party"),
        (party_get_attached_to, ":led_party_attached", ":lord_led_party"),
        (is_between, ":led_party_attached", walled_centers_begin, walled_centers_end),
        (store_faction_of_party, ":led_party_faction", ":lord_led_party"),
        (store_faction_of_party, ":attached_party_faction", ":led_party_attached"),
        (neq, ":led_party_faction", ":attached_party_faction"),
        
        (party_detach, ":lord_led_party"),
        (try_end),
        
        #Increase relation with lord in new faction by 5
        #Or, if player kingdom, make inactive pending confirmation
        (faction_get_slot, ":faction_liege", ":faction_no", slot_faction_leader),
        (try_begin),
        (eq, ":faction_liege", "trp_player"),
        (neq, ":troop_no", "$g_talk_troop"),
          (troop_set_slot, ":troop_no", slot_troop_occupation, slto_inactive), #POSSIBLE REASON 1
        (else_try),
        (is_between, ":faction_liege", active_npcs_begin, active_npcs_end),
        (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
        (call_script, "script_troop_change_relation_with_troop", ":faction_liege", ":troop_no", 5),
        (val_add, "$total_indictment_changes", 5),
        (try_end),
        
        #Break courtship relations
        (try_begin),
          (troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
        #Already married, do nothing
        (else_try),
        (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
          (try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
          (troop_get_slot, ":courted_lady", ":troop_no", ":love_interest_slot"),
          (call_script, "script_courtship_event_lady_break_relation_with_suitor", ":courted_lady", ":troop_no"),
          (try_end),
        (call_script, "script_assign_troop_love_interests", ":troop_no"),
        (else_try), 
        (is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
          (try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
            (troop_slot_eq, ":active_npc", ":love_interest_slot", ":troop_no"),
            (call_script, "script_courtship_event_lady_break_relation_with_suitor", ":troop_no", ":active_npc"),
          (try_end),
        (try_end),
        (try_end),
        
        #Stop raidings/sieges of new faction's fief if there is any
        (troop_get_slot, ":troop_party", ":troop_no", slot_troop_leaded_party),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (party_slot_eq, ":center_no", slot_party_type, spt_village),
          (party_get_slot, ":raided_by", ":center_no", slot_village_raided_by),     
          (eq, ":raided_by", ":troop_party"),
          (party_set_slot, ":center_no", slot_village_raided_by, -1),
          (try_begin),
            (party_slot_eq, ":center_no", slot_village_state, svs_being_raided),        
            (party_set_slot, ":center_no", slot_village_state, svs_normal),
            (party_set_extra_text, ":center_no", "str_empty_string"),
          (try_end),
        (else_try),       
          (party_get_slot, ":besieged_by", ":center_no", slot_center_is_besieged_by),
          (eq, ":besieged_by", ":troop_party"),
          (party_set_slot, ":center_no", slot_center_is_besieged_by, -1),

          (try_begin),      
            (party_slot_eq, ":center_no", slot_village_state, svs_under_siege),       
            (party_set_slot, ":center_no", slot_village_state, svs_normal),
            (party_set_extra_text, ":center_no", "str_empty_string"),
          (try_end),
        (try_end),
            
          (call_script, "script_update_all_notes"),
          (call_script, "script_update_village_market_towns"),
          (assign, "$g_recalculate_ais", 1),
      ]),

    

    ("initialize_aristocracy",
    [
        #LORD OCCUPATIONS, BLOOD RELATIONSHIPS, RENOWN AND REPUTATIONS
      #King ages
      (try_for_range, ":cur_troop", kings_begin, kings_end),
          (neg|is_between, pretenders_begin, pretenders_end),
          #KAOS (POLITICAL)
          #NOTE: Possibly limit the types depeding on faction eg rodoks no debutched      
          (store_random_in_range, ":king_reputation", 0, 8),
          (try_begin),
            (lt ,":king_reputation", 1),
            (assign, ":king_reputation", lrep_martial),
          (else_try),
            (lt, ":king_reputation", 3),
            (assign, ":king_reputation", lrep_selfrighteous),
          (else_try),
            (eq, ":king_reputation", 4),
            (assign, ":king_reputation", lrep_cunning),
          (else_try),
            (eq, ":king_reputation", 5),
            (assign, ":king_reputation", lrep_debauched),
          (else_try),
            (eq, ":king_reputation", 6),
            (assign, ":king_reputation", lrep_goodnatured),
          (else_try),
            (ge, ":king_reputation", 7),
            (assign, ":king_reputation", lrep_upstanding),
          (try_end),
          (troop_set_slot, ":cur_troop", slot_lord_reputation_type, ":king_reputation"),
          #KAOS (POLITICAL)
            (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (store_random_in_range, ":age", 50, 60),
            (try_begin),
                   (this_or_next|eq, ":cur_troop", "trp_kingdom_4_pretender"),
                   (eq, ":cur_troop", "trp_kingdom_5_pretender"),
                   (store_random_in_range, ":age", 40, 47),
            (else_try),
                   (eq, ":cur_troop", "trp_kingdom_6_lord"),
                   (store_random_in_range, ":age", 30, 40),
            (try_end),   
            (call_script, "script_init_troop_age", ":cur_troop", ":age"),
      (try_end),
            
      #The first thing - family structure
      #lords 1 to 8 are patriarchs with one live-at-home son and one daughter. They come from one of six possible ancestors, thus making it likely that there will be two sets of siblings
      #lords 9 to 12 are unmarried landowners with sisters
      #lords 13 to 20 are sons who still live in their fathers' houses
      #For the sake of simplicity, we can assume that all male aristocrats in prior generations either married commoners or procured their brides from the Old Country, thus discounting intermarriage 

      (try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),
        (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
      (try_end),
      
      (assign, ":cur_lady", "trp_kingdom_1_lady_1"),

      (try_for_range, ":cur_troop", lords_begin, lords_end),  
        (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        
        (store_random_in_range, ":father_age_at_birth", 23, 26),
#        (store_random_in_range, ":mother_age_at_birth", 19, 22),
        
        (try_begin),
            (is_between, ":cur_troop", "trp_knight_1_1", "trp_knight_2_1"),
            (store_sub, ":npc_seed", ":cur_troop", "trp_knight_1_1"),
            (assign, ":ancestor_seed", 1),
            (assign, ":king", "trp_kingdom_1_lord"),
        (else_try),
            (is_between, ":cur_troop", "trp_knight_2_1", "trp_knight_3_1"),
            (store_sub, ":npc_seed", ":cur_troop", "trp_knight_2_1"),
            (assign, ":ancestor_seed", 7),
            (assign, ":king", "trp_kingdom_2_lord"),
        (else_try),
            (is_between, ":cur_troop", "trp_knight_3_1", "trp_knight_4_1"),
            (store_sub, ":npc_seed", ":cur_troop", "trp_knight_3_1"),
            (assign, ":ancestor_seed", 13),
            (assign, ":king", "trp_kingdom_3_lord"),
        (else_try),
            (is_between, ":cur_troop", "trp_knight_4_1", "trp_knight_5_1"),
            (store_sub, ":npc_seed", ":cur_troop", "trp_knight_4_1"),
            (assign, ":ancestor_seed", 19),
            (assign, ":king", "trp_kingdom_4_lord"),
        (else_try),
            (is_between, ":cur_troop", "trp_knight_5_1", "trp_knight_6_1"),
            (store_sub, ":npc_seed", ":cur_troop", "trp_knight_5_1"),
            (assign, ":ancestor_seed", 25),
            (assign, ":king", "trp_kingdom_5_lord"),
        (else_try),
            (is_between, ":cur_troop", "trp_knight_6_1", "trp_knight_1_1_wife"),
            (store_sub, ":npc_seed", ":cur_troop", "trp_knight_6_1"),
            (assign, ":ancestor_seed", 31),
            (assign, ":king", "trp_kingdom_6_lord"),
        (try_end),
        
        
        (try_begin), #NPC seed is the order in the faction
            (lt, ":npc_seed", 8), #Senior lords
            (assign, ":reputation", ":npc_seed"),
            (store_random_in_range, ":age", 45, 64),
            
            (store_random_in_range, ":father", 0, 6), #six possible fathers
            (val_add, ":father", ":ancestor_seed"),
            (troop_set_slot, ":cur_troop", slot_troop_father, ":father"), # Father is not active npc
            
            #wife
            (troop_set_slot, ":cur_troop", slot_troop_spouse, ":cur_lady"),
            (troop_set_slot, ":cur_lady", slot_troop_spouse, ":cur_troop"),
            (store_random_in_range, ":wife_reputation", 20, 26),
            (try_begin),
                (eq, ":wife_reputation", 20),
                (assign, ":wife_reputation", lrep_conventional),
      #KAOS (POLITICAL) 
      (else_try),
        (eq, ":wife_reputation", 24),
        (assign, ":wife_reputation", lrep_ambitious),
      (else_try),
        (ge, ":wife_reputation", 25),
        (assign, ":wife_reputation", lrep_moralist),
      #KAOS (POLITICAL)
            (try_end),
            (troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":wife_reputation"),
            
            (store_random_in_range, ":lady_age", 40, ":age"),
            (call_script, "script_init_troop_age", ":cur_lady", ":lady_age"),
            (call_script, "script_add_lady_items", ":cur_lady"),
            
            (val_add, ":cur_lady", 1),

            #daughter
            (troop_set_slot, ":cur_lady", slot_troop_father, ":cur_troop"),
            (store_sub, ":mother", ":cur_lady", 1),
            (store_random_in_range, ":lady_age", 17, 25),
            (val_max, ":lady_age", 19),
            (call_script, "script_init_troop_age", ":cur_lady", ":lady_age"),
            (troop_set_slot, ":cur_lady", slot_troop_mother, ":cur_lady"),
            (store_random_in_range, ":lady_reputation", lrep_conventional, 34), #33% chance of father-derived
            (try_begin),
                (le, ":lady_reputation", 25),
                (troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":lady_reputation"),
            (else_try),    
                (eq, ":lady_reputation", 26),
                (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_conventional),
            (else_try),    
                (eq, ":lady_reputation", 27),
                (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_moralist),
            (else_try),
                (assign, ":guardian_reputation", ":reputation"),
                (try_begin),
                    (this_or_next|eq, ":guardian_reputation", lrep_martial),
                        (eq, ":guardian_reputation", 0),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_conventional),
                (else_try),        
                    (eq, ":guardian_reputation", lrep_quarrelsome),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_otherworldly),
                (else_try),        
                    (eq, ":guardian_reputation", lrep_selfrighteous),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_ambitious),
                (else_try),        
                    (eq, ":guardian_reputation", lrep_cunning),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_adventurous),
                (else_try),        
                    (eq, ":guardian_reputation", lrep_goodnatured),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_adventurous),
                (else_try),        
                    (eq, ":guardian_reputation", lrep_debauched),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_ambitious),
                (else_try),        
                    (eq, ":guardian_reputation", lrep_upstanding),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_moralist),
                (try_end),
            (try_end),
            
            (call_script, "script_add_lady_items", ":cur_lady"),
            (val_add, ":cur_lady", 1),
            #high renown

        (else_try),    #Older unmarried lords
            (is_between, ":npc_seed", 8, 12), # Dunde gives sons to the kings
            (store_random_in_range, ":age", 25, 36),            
            (store_random_in_range, ":reputation", 0, 8),    
            (try_begin),
               (is_between, ":npc_seed", 8, 10),
               (this_or_next|eq, ":npc_seed", 8), (ge, ":reputation", 6),
               (troop_set_slot, ":cur_troop", slot_troop_father, ":king"),
               (val_min, ":age", 28), # we want young princes
            (try_end),        
            (try_begin),
                # No Father
        (troop_get_slot, ":tmp", ":cur_troop", slot_troop_father),
                (lt, ":tmp", 0),
                (store_random_in_range, ":sister_reputation", 20, 26),
                (try_begin),
                    (eq, ":sister_reputation", 20),
                    (assign, ":sister_reputation", lrep_conventional),
      #KAOS (POLITICAL) 
      (else_try),
        (eq, ":sister_reputation", 24),
        (assign, ":sister_reputation", lrep_ambitious),
      (else_try),
        (ge, ":sister_reputation", 25),
        (assign, ":sister_reputation", lrep_moralist),
      #KAOS (POLITICAL)
                (try_end),
                (troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":sister_reputation"),            
                (troop_set_slot, ":cur_lady", slot_troop_guardian, ":cur_troop"),
            (else_try),
                # King's son
                (try_begin), #50% chance of having father's rep
                   (store_random_in_range, ":reputation", 0, 16),
                   (gt, ":reputation", 7),
                   (troop_get_slot, ":reputation", ":king", slot_lord_reputation_type),
                (try_end),
                (troop_set_slot, ":cur_lady", slot_troop_father, ":king"),
                (store_random_in_range, ":lady_reputation", lrep_conventional, 34), #33% chance of father-derived
                (try_begin),
                    (le, ":lady_reputation", 25),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":lady_reputation"),
                (else_try),    
                    (eq, ":lady_reputation", 26),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_conventional),
                (else_try),    
                    (eq, ":lady_reputation", 27),
                    (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_moralist),
                (else_try),
                    (assign, ":guardian_reputation", ":reputation"),
                    (try_begin),
                        (this_or_next|eq, ":guardian_reputation", lrep_martial),
                            (eq, ":guardian_reputation", 0),
                        (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_conventional),
                    (else_try),        
                        (eq, ":guardian_reputation", lrep_quarrelsome),
                        (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_otherworldly),
                    (else_try),        
                        (eq, ":guardian_reputation", lrep_selfrighteous),
                        (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_ambitious),
                    (else_try),        
                        (eq, ":guardian_reputation", lrep_cunning),
                        (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_adventurous),
                    (else_try),        
                        (eq, ":guardian_reputation", lrep_goodnatured),
                        (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_adventurous),
                    (else_try),        
                        (eq, ":guardian_reputation", lrep_debauched),
                        (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_ambitious),
                    (else_try),        
                        (eq, ":guardian_reputation", lrep_upstanding),
                        (troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_moralist),
                    (try_end),
                (try_end),           
            (try_end),
            (store_random_in_range, ":lady_age", 15, 28),
            (val_max, ":lady_age", 21),
            (call_script, "script_init_troop_age", ":cur_lady", ":lady_age"),
            (call_script, "script_add_lady_items", ":cur_lady"),
            (val_add, ":cur_lady", 1),
            
        (else_try),    #Younger unmarried lords 
            #age is father's minus 20 to 25
            (store_sub, ":father", ":cur_troop", 12),
            (troop_set_slot, ":cur_troop", slot_troop_father, ":father"),
            (troop_get_slot, ":mother", ":father", slot_troop_spouse),
            (troop_set_slot, ":cur_troop", slot_troop_mother, ":mother"),
            (troop_get_slot, ":father_age", ":father", slot_troop_age),
            (store_sub, ":age", ":father_age", ":father_age_at_birth"),

            (try_begin), #50% chance of having father's rep
                (store_random_in_range, ":reputation", 0, 16),
                (gt, ":reputation", 7),
                (troop_get_slot, ":reputation", ":father", slot_lord_reputation_type),
            (try_end),
        (try_end),
        
        (try_begin),
            (eq, ":reputation", 0),
      #KAOS (POLITICAL)
      (store_random_in_range, ":reputation", 0, 8),
      (try_begin),
        (lt ,":reputation", 1),
        (assign, ":reputation", lrep_martial),
      (else_try),
        (lt, ":reputation", 3),
        (assign, ":reputation", lrep_selfrighteous),
      (else_try),
        (eq, ":reputation", 4),
        (assign, ":reputation", lrep_cunning),
      (else_try),
        (eq, ":reputation", 5),
        (assign, ":reputation", lrep_debauched),
      (else_try),
        (eq, ":reputation", 6),
        (assign, ":reputation", lrep_goodnatured),
      (else_try),
        (ge, ":reputation", 7),
        (assign, ":reputation", lrep_upstanding),
      (try_end),
      #KAOS (POLITICAL)
      (try_end),
        (troop_set_slot, ":cur_troop", slot_lord_reputation_type, ":reputation"),
        (call_script, "script_init_troop_age", ":cur_troop", ":age"),
      (try_end),
      
      (try_begin),
        (eq, "$cheat_mode", 1),
        (assign, reg3, "$cheat_mode"),
        (display_message, "@{!}DEBUG -- Assigned lord reputation and relations"),
#        (display_message, "str_assigned_lord_reputation_and_relations_cheat_mode_reg3"), #This string can be removed
      (try_end),

        (try_for_range, ":cur_troop", pretenders_begin, pretenders_end),
            (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_inactive_pretender),
            #KAOS (POLITICAL)
            (store_random_in_range, ":pretender_reputation", 0, 8),
            (try_begin),
              (lt ,":pretender_reputation", 1),
              (assign, ":pretender_reputation", lrep_martial),
            (else_try),
              (lt, ":pretender_reputation", 3),
              (assign, ":pretender_reputation", lrep_selfrighteous),
            (else_try),
              (eq, ":pretender_reputation", 4),
              (assign, ":pretender_reputation", lrep_cunning),
            (else_try),
              (eq, ":pretender_reputation", 5),
              (assign, ":pretender_reputation", lrep_debauched),
            (else_try),
              (eq, ":pretender_reputation", 6),
              (assign, ":pretender_reputation", lrep_goodnatured),
            (else_try),
              (ge, ":pretender_reputation", 7),
              (assign, ":pretender_reputation", lrep_upstanding),
            (try_end),
            (troop_set_slot, ":cur_troop", slot_lord_reputation_type, ":pretender_reputation"),
            (store_random_in_range, ":age", 25, 36),
            (try_begin),
               (this_or_next|eq, ":cur_troop", "trp_kingdom_4_pretender"),
               (eq, ":cur_troop", "trp_kingdom_5_pretender"),
               (store_random_in_range, ":age", 40, 47),
            (else_try),
               (eq, ":cur_troop", "trp_kingdom_6_pretender"),
               (store_random_in_range, ":age", 50, 60),
            (try_end),   
            (call_script, "script_init_troop_age", ":cur_troop", ":age"),
      (try_end),
    ]),
  #initialize_aristocracy
    



  ("troop_get_romantic_chemistry_with_troop", #source is lady, target is man
    [
      (store_script_param, ":source_lady", 1),
      (store_script_param, ":target_lord", 2),
      
      (store_add, ":chemistry_sum", ":source_lady", ":target_lord"),
      (val_add, ":chemistry_sum", "$romantic_attraction_seed"),      
      
      #This calculates (modula ^ 2) * 3 
      (store_mod, ":chemistry_remainder", ":chemistry_sum", 5),
      (val_mul, ":chemistry_remainder", ":chemistry_remainder"), #0, 1, 4, 9, 16
      (val_mul, ":chemistry_remainder", 3), #0, 3, 12, 27, 48
      
      (store_attribute_level, ":romantic_chemistry", ":target_lord", ca_charisma),
      (val_sub, ":romantic_chemistry", ":chemistry_remainder"),
      

      (try_begin),
          (eq, "$background_type", cb_prince),
          (eq, "$background_type", cb_king),
          (val_mul, ":romantic_chemistry", 3),
      (else_try),
          (val_mul, ":romantic_chemistry", 2),
      (try_end),

      (assign, reg0, ":romantic_chemistry"), 
      
      #examples : 
      #For a charisma of 18, yields (18 - 0) * 2 = 36, (18 - 3) * 2 = 30, (18 - 12) * 2 = 12, (18 - 27) * 2 = -18, (18 - 48) * 2 = -60
      #For a charisma of 10, yields (10 - 0) * 2 = 20, (10 - 3) * 2 = 14, (10 - 12) * 2 = -4, (10 - 27) * 2 = -34, (10 - 48) * 2 = -76
      #For a charisma of 7, yields  (7 - 0) * 2 = 14,  (7 - 3) * 2 = 8,   (7 - 12) * 2 = -10, (7 - 27) * 2 = -40,  (7 - 48) * 2 = -82
      
      #15 is high attraction, 0 is moderate attraction, -76 is lowest attraction
  ]),    
  
########################################################################################################################
#  OVER WRITING OF SCRIPTS                                                                                             #
########################################################################################################################


########################################################################################################################
#  Jrider + Begin new scripts                                                                                          #
########################################################################################################################


  # Script get_troop_specialisation
  # Assess companion current skills to find the strongest trend
  ("get_troop_specialisation",
   [
        (store_script_param, ":troop_no", 1),
        (store_script_param, ":faction_no", 2),
        (assign, ":raider", 0),
        (assign, ":slayer", 0),
        (assign, ":slaver", 0),
        (try_begin),
           (neg|eq, ":faction_no", "fac_player_supporters_faction"), # v0.2 change
           (is_between, ":troop_no", companions_begin, companions_end),
           # Other titles according to function in group

           # Scout - PathFinding, Tracking and Spotting
           (store_skill_level, ":scout", "skl_spotting", ":troop_no"),
           (store_skill_level, ":scout_skill", "skl_pathfinding", ":troop_no"),
           (val_add, ":scout", ":scout_skill"),
           (store_skill_level, ":scout_skill", "skl_tracking", ":troop_no"),
           (val_add, ":scout", ":scout_skill"),
  
           # Physician (Fisique) - Wound Treatment, Surgery, First Aid
           (store_skill_level, ":physician", "skl_wound_treatment", ":troop_no"),
           (store_skill_level, ":physician_skill", "skl_first_aid", ":troop_no"),
           (val_add, ":physician", ":physician_skill"),
           (store_skill_level, ":physician_skill", "skl_surgery", ":troop_no"),
           (val_add, ":physician", ":physician_skill"),

           # Tactician (Tassein) - Tactics, Engineer, Trainer
           (store_skill_level, ":tactician", "skl_tactics", ":troop_no"),
           (store_skill_level, ":tactician_skill", "skl_engineer", ":troop_no"),
           (val_add, ":tactician", ":tactician_skill"),
           (store_skill_level, ":tactician_skill", "skl_trainer", ":troop_no"),
           (val_add, ":tactician", ":tactician_skill"),

           # Trader (Empori) - Trade Looting, Foraging (foraging is a new skill I'm working on)
           (store_skill_level, ":trader", "skl_trade", ":troop_no"),
           (val_mul, ":trader", 3), # comment if using foraging

           #Raider  - Looting,
           (store_skill_level, ":raider", "skl_looting", ":troop_no"),
           #(val_add, ":raider", ":raider_skill"),
           (val_mul, ":raider", 3), # comment if using foraging

           # Slayer - Weapon Master Power Draw Power Strike
           (store_skill_level, ":slayer", "skl_weapon_master", ":troop_no"),
           (store_skill_level, ":slayer_skill", "skl_power_strike", ":troop_no"),
           (val_add, ":slayer", ":slayer_skill"),
           (store_skill_level, ":slayer_skill", "skl_power_draw", ":troop_no"),
           (val_add, ":slayer", ":slayer_skill"),
           (val_div, ":slayer", 2),

           #Raider  - Prisoner Management,
           (store_skill_level, ":slaver", "skl_prisoner_management", ":troop_no"),
           (val_mul, ":slaver", 3), # comment if using foraging
           #(val_div, ":slaver", 2), # comment if using foraging

           # Diplomat (Missi) - Persuasion
           (store_skill_level, ":diplomat", "skl_persuasion", ":troop_no"),
           (val_mul, ":diplomat", 3),
           #(val_div, ":diplomat", 2), # comment if using foraging

           (try_begin), # Just your basic hero
               (eq, ":diplomat", 0),
               (eq, ":tactician", 0),
               (eq, ":scout", 0),
               (eq, ":physician", 0),
               (eq, ":trader", 0),
               (eq, ":raider", 0),
               (eq, ":slayer", 0),
               (eq, ":slaver", 0),
               (assign, reg0, 0),
           (else_try), # Diplomat - skilled in Persuasion and Trainer
               (gt, ":diplomat", 0),
               (ge, ":diplomat", ":tactician"),
               (ge, ":diplomat", ":scout"),
               (ge, ":diplomat", ":physician"),
               (ge, ":diplomat", ":trader"),
               (ge, ":diplomat", ":raider"),
               (ge, ":diplomat", ":slayer"),
               (ge, ":diplomat", ":slaver"),
               (assign, reg0, 1),
           (else_try), # Tactician - skilled in Tactics and Engineer
               (gt, ":tactician", 0),
               (ge, ":tactician", ":scout"),
               (ge, ":tactician", ":physician"),
               (ge, ":tactician", ":trader"),
               (ge, ":tactician", ":raider"),
               (ge, ":tactician", ":slayer"),
               (ge, ":tactician", ":slaver"),
               (assign, reg0, 2),
           (else_try), # Scout - skilled in Spotting, Tracking and Pathfinding
               (gt, ":scout", 0),
               (ge, ":scout", ":physician"),
               (ge, ":scout", ":trader"),
               (ge, ":scout", ":raider"),
               (ge, ":scout", ":slayer"),
               (ge, ":scout", ":slaver"),
               (assign, reg0, 3),
           (else_try), # Physician - skilled in Wound Treatment, Surgery and First Aid
               (gt, ":physician", 0),
               (ge, ":physician", ":trader"),
               (ge, ":physician", ":raider"),
               (ge, ":physician", ":slayer"),
               (ge, ":physician", ":slaver"),
               (assign, reg0, 4),
           (else_try), # Trader - skilled in Trade
               (gt, ":trader", 0),
               (ge, ":trader", ":raider"),
               (ge, ":trader", ":slayer"),
               (ge, ":trader", ":slaver"),
               (assign, reg0, 5),
           (else_try), # raider - skilled in Trade
               (gt, ":raider", 0),
               (ge, ":raider", ":slayer"),
               (ge, ":raider", ":slaver"),
               (assign, reg0, 6),
           (else_try), # slayer - skilled in Trade
               (gt, ":slayer", 0),
               (ge, ":slayer", ":slaver"),
               (assign, reg0, 7),
           (else_try), # slaver - skilled in Trade
               (gt, ":slaver", 0),
               (assign, reg0, 8),
           (try_end),
        (try_end),
   ]),



  # TITLES v0.3.3 #####
  # script troop_set_title_according_to_faction_gender_and_lands
  # calculate and set new title for lords, ladies and companions
  # use s0 and s1
  # change v0.3: use s61 and reg10
  ("troop_set_title_according_to_faction_gender_and_lands",
  [        
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":faction_no", 2),

      (try_begin),
          (eq, "$kaos_title_run", 0),
          (eq, ":troop_no", "trp_player"),
          (str_store_troop_name, s10, "trp_player"),
          (troop_set_plural_name, "trp_player", s10),
          (troop_set_plural_name, "trp_dummy_player", s10),
          (troop_set_name, "trp_dummy_player", s10),
          (assign, "$kaos_title_run", 1),
      (try_end),

      (try_begin),
          (faction_get_slot, ":faction_index", ":faction_no", slot_kaoses_faction_title_type),
          (call_script, "script_troop_set_title_according_to_faction_gender_and_lands_new", ":troop_no", ":faction_no", ":faction_index"),
      (try_end),

      (try_begin),
          (store_faction_of_troop, ":plyr_faction", "trp_player"),
          (is_between, ":plyr_faction", kingdoms_begin, kingdoms_end),
          (faction_get_slot, ":faction_index", ":faction_no", slot_kaoses_faction_title_type),
          (call_script, "script_troop_set_title_according_to_faction_gender_and_lands_new", "trp_player", ":plyr_faction", ":faction_index"),

      (try_end),

  ]),
#jrider Expanded nobility title system kit (v0.3.3)

########################################################################################################################
#  Jrider + End new scripts                                                                                            #
########################################################################################################################

########################################################################################################################
#  KAOS POLITICAL                                                                                                      #
########################################################################################################################
  


  # TITLES v0.3.3 #####
  # script troop_set_title_according_to_faction_gender_and_lands_new
  # calculate and set new title for lords, ladies and companions
  # use s0 and s1
  # change v0.3: use s61 and reg10
  ("troop_set_title_according_to_faction_gender_and_lands_new",
  [        
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":faction_no", 2),
      (store_script_param, ":faction_index", 3),

      (str_store_troop_name_plural, s0, ":troop_no"),


      # Ensure we process only npcs member of a kingdom, including player
      (try_begin), # Npcs serving as lord and ladies
          # v0.1 change +
          (is_between, ":faction_no", kingdoms_begin, kingdoms_end), # normaly this one should exclude companions that are not vassals
          (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
          (neg|is_between, ":troop_no", pretenders_begin, pretenders_end), # exclude pretenders
          (this_or_next|is_between, ":troop_no", active_npcs_including_player_begin, kingdom_ladies_end), # v0.3.1 change to include player
          (eq, ":troop_no", "trp_player"), # include player player # v0.3.1 change
#          (neq, ":troop_no", "trp_player"), # exclude player # v0.3.1 commented, wasn't relevant anyway

          (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),

          # v0.1 change -
          # External computation blocks
          # Get Gender
          (troop_get_type, ":gender", ":troop_no"),
          # NPC's largest fief (works for male and female, compute spouse fief as well)
          # 1 no fief, 2 village, 3 castle, 4 town
          (assign, ":largest_fief", 0),
          (try_for_range, ":cur_center", centers_begin, centers_end),
                (troop_get_slot, ":spouse_no", ":troop_no", slot_troop_spouse),
                (neq, ":troop_no", ":faction_leader"), # exclude research for ruler
                (neq, ":spouse_no", ":faction_leader"), # exclude research for ruler's wife
                (lt, ":largest_fief", 3),
                (party_slot_ge, ":cur_center", slot_town_lord, 0),
                (this_or_next|party_slot_eq, ":cur_center", slot_town_lord, ":spouse_no"),
                (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),

                (try_begin),
                  (party_slot_eq, ":cur_center", slot_party_type, spt_town),
                  (lt, ":largest_fief", 3),
                  (assign, ":largest_fief", 3),
                (else_try),
                  (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
                  (lt, ":largest_fief", 2),
                  (assign, ":largest_fief", 2),
                (else_try),
                  (party_slot_eq, ":cur_center", slot_party_type, spt_village),
                  (lt, ":largest_fief", 1),
                  (assign, ":largest_fief", 1),
                (try_end),
          (try_end),

          # base title(s) computation blocks
          # Determine NPCs quality in order of importance
          # for male NPCs: 4 Ruler, 3 town, 2 castle, 1 village, 0 landless
          # for female NPCs: 5 unmarried (kingdom lady only), 4 queen, 3 wife or town, 2 wife or castle, 1 wife or village, 0 wife or landless
          (assign, ":quality", 0),
          (try_begin), # Male npcs
               (eq, ":gender", 0),
               (try_begin),
                   (eq, ":troop_no", ":faction_leader"), # is king
                   (assign, ":quality", 4),
               (else_try),
                   (assign, ":quality", ":largest_fief"),
               (try_end),
          (else_try), # Female npcs, a bit more complex queen, landowner, companions without a fief,
               (try_begin), # wife of faction leader
                    # v0.3.3 change +
                    (this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),
                    (eq, ":troop_no", ":faction_leader"), # is queen
                    # v0.3.3 change -
                    (assign, ":quality", 4),
               (else_try), # is a landowner - index 1 to 3
                    (gt, ":largest_fief", 0),
                    (assign, ":quality", ":largest_fief"),
               (else_try), # a companion vassal without fief
                    (is_between, ":troop_no", companions_begin, companions_end),
                    (assign, ":quality", 0),
               (else_try), # married lady whose husband has no fief
                    (troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
                    (assign, ":quality", 0),
               (else_try), # unmarried lady without fief
                    (assign, ":quality", 5),
               (try_end),
          (try_end),

          # v0.3 changes +
          # compute troop relation to ruler suffix
          (try_begin),
              (neq, ":troop_no", ":faction_leader"), # exclude from suffix if king v0.3.2 change
              (eq, "$kaos_use_suffixes", 1),
              (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
              (assign, ":relation", reg0),
              (str_clear, s61),
              (assign, reg10, 0),
              (try_begin), # update reg10
                (this_or_next|gt, ":relation", 19),
                (lt, ":relation", -19),
                (assign, reg10, ":relation"),
                (store_add, ":normalized_relation", ":relation", 100),
                (store_div, ":str_offset", ":normalized_relation", 20),
                (val_clamp, ":str_offset", 0, 10), # does 10 work ? only 10 strings in there
                (store_add, ":str_rel_id", "str_ruler_relation_mnus_100_ns",  ":str_offset"),
                (str_store_string, s61, ":str_rel_id"),
              (try_end),
          (else_try), # clear register and string
              (str_clear, s61),
              (assign, reg10, 0),      
          (try_end),
          # v0.3 changes -

          # Find title index in strings block
          #(store_sub, ":title_index", ":faction_no", kingdoms_begin), # 0 player, 1 swadian ...
          (store_sub, ":title_index", ":faction_index", kingdoms_begin), # 0 player, 1 swadian ...
          (try_begin), #male, 5 title entries
                (eq, ":gender", 0), 
                (val_mul, ":title_index", 5),
                (val_add, ":title_index", kingdom_titles_male_begin),
          (else_try), # female, 6 title entries
                (val_mul, ":title_index", 6),
                (val_add, ":title_index", kingdom_titles_female_begin),
          (try_end),

          (val_add, ":title_index", ":quality"),

          # Set title and party name block
          # assign title
          (str_store_string, s1, ":title_index"),

          (try_begin),
              (eq, "$kaos_royal_children", 1),
              (assign, ":liege", 0),
              (assign, ":mother", 0),
              (assign, ":father", 0),
              #(store_faction_of_troop, ":lord_faction", ":lord"),
              (faction_get_slot, ":liege", ":faction_no", slot_faction_leader),
              (troop_get_slot, ":mother", ":troop_no", slot_troop_mother),
              (troop_get_slot, ":father", ":troop_no", slot_troop_father),
              #(try_begin),
                (this_or_next|eq, ":mother",":liege"),   
                (eq, ":father", ":liege"),  
                (troop_get_type, ":gender", ":troop_no"),
                (try_begin),
                    (eq, ":gender", 0), #male 
                    (str_store_string, s1, "str_faction_title_male_heir"),   
                (else_try),
                    (str_store_string, s1, "str_faction_title_female_Heir"),
                (try_end),   
              #(try_end),       
          (try_end),

          (troop_set_name, ":troop_no", s1),

          (try_begin),
              (eq, ":faction_index" , "fac_player_supporters_faction"),
              (eq , "$kaos_has_custom_title", 1),
              (eq, ":gender", 0), 
              (try_begin),
                  (eq, ":quality", 4), 
                  (troop_slot_eq, "trp_dummy_5_king", 0, 1),
                  (str_store_troop_name, s0, "trp_dummy_5_king"),
                  (str_store_troop_name_plural, s1, ":troop_no"),
                  (str_store_string, s1, "str_s0_s1"),
                  (troop_set_name, ":troop_no", s1),
              (else_try),
                  (eq, ":quality", 3), 
                  (troop_slot_eq, "trp_dummy_4_town", 0, 1),
                  (str_store_troop_name, s0, "trp_dummy_4_town"),
                  (str_store_troop_name_plural, s1, ":troop_no"),
                  (str_store_string, s1, "str_s0_s1"),
                  (troop_set_name, ":troop_no", s1),
              (else_try),
                  (eq, ":quality", 2), 
                  (troop_slot_eq, "trp_dummy_3_castle", 0, 1),
                  (str_store_troop_name, s0, "trp_dummy_3_castle"),
                  (str_store_troop_name_plural, s1, ":troop_no"),
                  (str_store_string, s1, "str_s0_s1"),
                  (troop_set_name, ":troop_no", s1),
              (else_try),
                  (eq, ":quality", 1), 
                  (troop_slot_eq, "trp_dummy_2_village", 0, 1),
                  (str_store_troop_name, s0, "trp_dummy_2_village"),
                  (str_store_troop_name_plural, s1, ":troop_no"),
                  (str_store_string, s1, "str_s0_s1"),
                  (troop_set_name, ":troop_no", s1),
              (else_try),
                  (eq, ":quality", 0), 
                  (troop_slot_eq, "trp_dummy_1", 0, 1),
                  (str_store_troop_name, s0, "trp_dummy_1"),
                  (str_store_troop_name_plural, s1, ":troop_no"),
                  (str_store_string, s1, "str_s0_s1"),
                  (troop_set_name, ":troop_no", s1),
              (try_end),
          (try_end),

          # rename party
          (troop_get_slot, ":troop_party", ":troop_no", slot_troop_leaded_party),

          (try_begin), 
          # v0.2 change to prevent opcode error
            (gt, ":troop_party", 0),
            (str_store_troop_name, s5, ":troop_no"),
            (party_set_name, ":troop_party", "str_s5_s_party"),
          (try_end), # v0.2 change
      (try_end),

      # Special titles for companions not used as vassals
      (try_begin),
          (eq, "$kaos_use_custom_name", 1),
          (neg|eq, ":faction_no", "fac_player_supporters_faction"), # v0.2 change
          (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero), # v0.3 change, exclude companion if he became a kingdom lord
          (is_between, ":troop_no", companions_begin, companions_end),
          # Store the plural name
          (str_store_troop_name_plural, s0, ":troop_no"),
          # Set the title
          (try_begin), # Male npcs
               (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_player_companion),
               (str_store_string, s1, "str_hero_titles_party"),
          (else_try),
              (call_script, "script_get_troop_specialisation", ":troop_no", ":faction_no"),
              (assign, ":title_index", reg0),
              (val_add, ":title_index", hero_titles_begin),
              (str_store_string, s1, ":title_index"),
          (try_end),
          # assign title
          (troop_set_name, ":troop_no", s1),
      (try_end),

      #(troop_set_plural_name, ":troop_no", s0),
          (faction_get_slot, ":liege", ":faction_no", slot_faction_leader),

      (try_begin),
          (eq, "$background_type", cb_king),
          #(eq, "trp_player", ":troop_no"),
          (str_store_troop_name_plural, s22, "trp_player"),
          (call_script, "script_cf_kaos_update_king_titles","trp_player" , ":faction_no"),
      (try_end),

      (try_begin),
          (faction_get_slot, ":liege", ":faction_no", slot_faction_leader),
          (eq, ":troop_no", ":liege"),
          (call_script, "script_cf_kaos_update_king_titles",":troop_no" , ":faction_no"),
      (try_end),

      (call_script, "script_update_all_notes"),
  ]),


  # script_cf_kaos_update_king_titles
  # Script update kings titles to reflect the number of centers held
  # Input: 
  # Output: none
  ("cf_kaos_update_king_titles",
    [
         
        (store_script_param, ":liege", 1),
        (store_script_param, ":faction", 2),

        (eq, "$kaos_king_titles", 1),
        (eq , "$kaos_has_custom_title", 0),
        (str_clear, s1),
        (str_clear, s0),
        (assign, ":rename", 0),
        (assign, ":imperial", 0),
        (assign, ":high", 0),

        (try_begin),
              (eq, ":liege", "trp_player"),
              (str_store_troop_name_plural, s0, "trp_dummy_player"),
        (else_try),
                (str_store_troop_name_plural, s0, ":liege"),
        (try_end),


        (assign, reg0, 0),
        (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
        (neg|faction_slot_eq, ":faction", slot_faction_state, sfs_defeated),
        (try_for_range, ":cur_center", centers_begin, centers_end),
            (store_faction_of_party, ":cur_faction", ":cur_center"),
            (try_begin),
                (eq, ":cur_faction", ":faction"),
                (val_add, reg0, 1),
            (try_end),
        (try_end),

        (troop_get_type, ":gender", ":liege"),
        (try_begin),
            (ge, reg0, 120),
              (try_begin),
                  (eq, ":gender", 0), #male 
                  (str_store_string, s3, "str_kings_rank_2_male"),   
              (else_try),
                  (str_store_string, s3, "str_kings_rank_2_female"),
              (try_end),
              (assign, ":rename", 1),
              (assign, ":imperial", 1),
        (else_try),
            (gt, reg0, 80),
              (try_begin),
                  (eq, ":gender", 0), #male 
                  (str_store_string, s3, "str_kings_rank_1_male"),   
              (else_try),
                  (str_store_string, s3, "str_kings_rank_1_female"),
              (try_end),
              (assign, ":rename", 1),
              (assign, ":high", 1),
        (else_try),
            (lt, reg0, 20),
            (str_store_string, s3, "str_kings_rank_0"), 
            (assign, ":rename", 1),
        (try_end),


        (try_begin),
           (ge, reg0, 120),
           (try_begin),
              (eq, ":faction", "fac_kingdom_1"),
              (str_store_string, s4, "str_kaos_swadia_empire"),
           (else_try),
              (eq, ":faction", "fac_kingdom_2"),
              (str_store_string, s4, "str_kaos_Vaegirs_empire"),
           (else_try),
              (eq, ":faction", "fac_kingdom_3"),
              (str_store_string, s4, "str_kaos_Khergit_empire"),
           (else_try),
              (eq, ":faction", "fac_kingdom_4"),
              (str_store_string, s4, "str_kaos_Nords_empire"),
           (else_try),
              (eq, ":faction", "fac_kingdom_5"),
              (str_store_string, s4, "str_kaos_Rhodoks_empire"),
           (else_try),
              (eq, ":faction", "fac_kingdom_6"),
              (str_store_string, s4, "str_kaos_Sarranid_empire"),
           (try_end),

            (try_begin),
                (eq, ":liege", "trp_player"), 
                (eq, "$background_type", cb_king),
                 (try_begin),
                      (eq, "$kaos_kings_kingdom", 1),
                      (str_store_string, s7, "str_kaos_swadia_empire"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 2),
                      (str_store_string, s7, "str_kaos_Vaegirs_empire"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 3),
                      (str_store_string, s7, "str_kaos_Khergit_empire"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 4),
                      (str_store_string, s7, "str_kaos_Nords_empire"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 5),
                      (str_store_string, s7, "str_kaos_Rhodoks_empire"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 6),
                      (str_store_string, s7, "str_kaos_Sarranid_empire"),
                 (try_end),
            (try_end),
        (else_try),
           (gt, reg0, 80),
           (try_begin),
              (eq, ":faction", "fac_kingdom_1"),
              (str_store_string, s4, "str_kaos_swadia_king"),
           (else_try),
              (eq, ":faction", "fac_kingdom_2"),
              (str_store_string, s4, "str_kaos_Vaegirs_king"),
           (else_try),
              (eq, ":faction", "fac_kingdom_3"),
              (str_store_string, s4, "str_kaos_Khergit_king"),
           (else_try),
              (eq, ":faction", "fac_kingdom_4"),
              (str_store_string, s4, "str_kaos_Nords_king"),
           (else_try),
              (eq, ":faction", "fac_kingdom_5"),
              (str_store_string, s4, "str_kaos_Rhodoks_king"),
           (else_try),
              (eq, ":faction", "fac_kingdom_6"),
              (str_store_string, s4, "str_kaos_Sarranid_king"),
           (try_end),

            (try_begin),
                (eq, ":liege", "trp_player"), 
                (eq, "$background_type", cb_king),
                 (try_begin),
                      (eq, "$kaos_kings_kingdom", 1),
                      (str_store_string, s7, "str_kaos_swadia_king"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 2),
                      (str_store_string, s7, "str_kaos_Vaegirs_king"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 3),
                      (str_store_string, s7, "str_kaos_Khergit_king"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 4),
                      (str_store_string, s7, "str_kaos_Nords_king"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 5),
                      (str_store_string, s7, "str_kaos_Rhodoks_king"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 6),
                      (str_store_string, s7, "str_kaos_Sarranid_king"),
                 (try_end),
            (try_end),
        (else_try),
           (lt, reg0, 20),
           (try_begin),
              (eq, ":faction", "fac_kingdom_1"),
              (str_store_string, s4, "str_kaos_swadia_king_20"),
           (else_try),
              (eq, ":faction", "fac_kingdom_2"),
              (str_store_string, s4, "str_kaos_Vaegirs_king_20"),
           (else_try),
              (eq, ":faction", "fac_kingdom_3"),
              (str_store_string, s4, "str_kaos_Khergit_king_20"),
           (else_try),
              (eq, ":faction", "fac_kingdom_4"),
              (str_store_string, s4, "str_kaos_Nords_king_20"),
           (else_try),
              (eq, ":faction", "fac_kingdom_5"),
              (str_store_string, s4, "str_kaos_Rhodoks_king_20"),
           (else_try),
              (eq, ":faction", "fac_kingdom_6"),
              (str_store_string, s4, "str_kaos_Sarranid_king_20"),
           (try_end),

            (try_begin),
                (eq, ":liege", "trp_player"), 
                (eq, "$background_type", cb_king),
                 (try_begin),
                      (eq, "$kaos_kings_kingdom", 1),
                      (str_store_string, s7, "str_kaos_swadia_king_20"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 2),
                      (str_store_string, s7, "str_kaos_Vaegirs_king_20"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 3),
                      (str_store_string, s7, "str_kaos_Khergit_king_20"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 4),
                      (str_store_string, s7, "str_kaos_Nords_king_20"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 5),
                      (str_store_string, s7, "str_kaos_Rhodoks_king_20"),
                 (else_try),
                      (eq, "$kaos_kings_kingdom", 6),
                      (str_store_string, s7, "str_kaos_Sarranid_king_20"),
                 (try_end),
            (try_end),
        (try_end),

        (try_begin),
                (eq, ":rename", 1), 
                (troop_set_name, ":liege", s3),
                # rename party
                (faction_set_name, ":faction", s4),
                (troop_get_slot, ":troop_party", ":liege", slot_troop_leaded_party),
                (try_begin), 
                # v0.2 change to prevent opcode error
                  (gt, ":troop_party", 0),
                  (str_store_troop_name, s5, ":liege"),
                  (party_set_name, ":troop_party", "str_s5_s_party"),
                (try_end), # v0.2 change
        (try_end),

        (try_begin),
              (eq, ":liege", "trp_player"), 
              (eq, ":rename", 1), 
              (display_log_message, "@{!} DEBUG plyr - s1 {s1}", 0xFF0000),  
              (troop_set_name, ":liege", s3),
                (faction_set_name, "fac_player_supporters_faction", s7),
                # rename party
                (troop_get_slot, ":troop_party", "trp_player", slot_troop_leaded_party),
                (try_begin), 
                # v0.2 change to prevent opcode error
                  (gt, ":troop_party", 0),
                  (str_store_troop_name, s5, "trp_player"),
                  (party_set_name, ":troop_party", "str_s5_s_party"),
                (try_end), # v0.2 change
        (try_end),



          (try_begin),
              (eq, "$kaos_royal_children", 1),
              (assign, ":liege", 0),
              (assign, ":mother", 0),
              (assign, ":father", 0),
              (try_for_range, ":npc_no", active_npcs_begin, kingdom_ladies_end),
                  (store_faction_of_troop, ":npc_faction", ":npc_no"),
                  (try_begin),
                      (eq, ":npc_faction", ":faction"),
                      (troop_get_slot, ":mother", ":npc_no", slot_troop_mother),
                      (troop_get_slot, ":father", ":npc_no", slot_troop_father),
                      (this_or_next|eq, ":mother",":liege"),   
                      (eq, ":father", ":liege"),  
                      (str_store_troop_name_plural, s0, ":npc_no"),
                      (troop_get_type, ":gender", ":npc_no"),
                      (try_begin),
                          (eq, ":imperial", 1),
                          (try_begin),
                              (eq, ":gender", 0), #male 
                              (str_store_string, s11, "str_faction_title_male_heir_empire"),   
                          (else_try),
                              (str_store_string, s11, "str_faction_title_female_Heir_empire"),
                          (try_end),
                      (else_try),
                          (eq, ":high", 1),
                          (try_begin),
                              (eq, ":gender", 0), #male 
                              (str_store_string, s11, "str_faction_title_male_heir_high"),   
                          (else_try),
                              (str_store_string, s11, "str_faction_title_female_Heir_high"),
                          (try_end),
                      (try_end),
                      (troop_set_name, ":npc_no", s11),
                      # rename party
                      (troop_get_slot, ":troop_party", ":npc_no", slot_troop_leaded_party),
                      (try_begin), 
                      # v0.2 change to prevent opcode error
                        (gt, ":troop_party", 0),
                        (str_store_troop_name, s5, ":npc_no"),
                        (party_set_name, ":troop_party", "str_s5_s_party"),
                      (try_end), # v0.2 change
                  (try_end),
              (try_end),
          (try_end),


    ]
  ), 



  # script_kaos_update_titles
  # Script update lords titles
  # Input: arg1 = faction_id
  # Output: none
  ("kaos_update_titles",
    [
        (try_for_range, ":cur_troop", active_npcs_including_player_begin, kingdom_ladies_end),
              (this_or_next|troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
              (this_or_next|troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
              (eq, ),
              (store_faction_of_troop, ":cur_faction", ":cur_troop"),
              (is_between, ":cur_faction", kingdoms_begin, kingdoms_end),
              (store_faction_of_troop, ":cur_faction", ":cur_troop"),

              (call_script, "script_troop_set_title_according_to_faction", ":cur_troop", ":cur_faction"), 
        (try_end),
        (call_script, "script_update_all_notes"),
    ]
  ), 





  # script_rebelion_assesment
  # Script Assess the faction for revolt 
  # Input: arg1 = faction
  # Output: none
  ("rebelion_assesment",
   [
        (store_script_param_1, ":orig_faction"),

        (assign, ":at_war_count", 0),
        (assign, ":rebellion_chance", 0),

        (call_script, "script_evaluate_realm_stability", ":orig_faction"),
        (assign, ":instability_index", reg0),
        (val_add, ":instability_index", reg0),
        (val_add, ":instability_index", reg1),                                           
        (try_begin),
            (gt, ":instability_index", 60),
            # HEAVY FACTION FRACTURING  #
            (assign, ":rebellion_chance", 4),
        (else_try), 
            (is_between, ":instability_index", 40, 60),
            # MODERATE FACTION FRACTURING   #   
            (assign, ":rebellion_chance", 3),
        (else_try), 
            (is_between, ":instability_index", 20, 40),
            # LIGHT FACTION FRACTURING  #   
            (assign, ":rebellion_chance", 2),
        (else_try), 
            (lt, ":instability_index", 20),
            # NO FACTION FRACTURING     #
            (assign, ":rebellion_chance", 1),
        (try_end),
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
          (neq, ":orig_faction", ":faction_no"),
          (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":orig_faction", ":faction_no"),
          (assign, ":global_diplomatic_status", reg0),
          (try_begin), # War
              (eq, ":global_diplomatic_status", -2),
              (val_add, ":at_war_count", 1),
              (val_add, ":rebellion_chance", 1),
          (try_end),            
        (try_end),

        (faction_set_slot, ":orig_faction", slot_faction_instability, ":instability_index"),
        (faction_set_slot, ":orig_faction", slot_faction_has_rebellion_chance, ":rebellion_chance"),
   ]
  ),

  # script_kaos_get_lord_highest_controversy_in_faction
  # Script Get the lord of the specified faction with the highest contraversy 
  # Input: arg1 = orig_faction
  # Output: reg0 = lord_no
  ("kaos_get_lord_highest_controversy_in_faction",
    [
        (store_script_param_1, ":orig_faction"),
        (assign, ":controversy", 0),
        (assign, ":lord_no", 0),
        (assign, ":troop_no", 0),
        (try_for_range, ":troop_no", lords_begin, lords_end),
            (store_troop_faction, ":lord_faction", ":troop_no"),
            (eq , ":lord_faction", ":orig_faction"),
            (troop_get_slot, ":lord_controversy", ":troop_no", slot_troop_controversy),
            (try_begin),
                (gt, ":lord_controversy", ":controversy"),
                (assign, ":controversy", ":lord_controversy"),
                (assign, ":lord_no", ":troop_no"),
            (try_end),
        (try_end),
        (troop_set_slot, ":lord_no", slot_troop_controversy, 15),
        (assign, reg0, ":lord_no"),
    ]
  ),

  # script_kaos_get_lord_lowest_relation_in_faction
  # Script Get the lord of the specified faction with the lowest relation to their liege   
  # Input: arg1 = orig_faction
  # Output: reg0 = lord_no
  ("kaos_get_lord_lowest_relation_in_faction",
    [
        (store_script_param_1, ":orig_faction"),
        (assign, ":relation", 100),
        (assign, ":troop_no", 0),
        (faction_get_slot, ":faction_king", ":orig_faction", slot_faction_leader),
        (try_for_range, ":troop_no", lords_begin, lords_end),
            (store_troop_faction, ":lord_faction", ":troop_no"),
            (eq , ":lord_faction", ":orig_faction"),
            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_king"),
            (assign, ":relation_with_king", reg0),  
            (try_begin),
                (eq , ":orig_faction", ":lord_faction"),
                (le, ":relation_with_king", ":relation"),
                (assign, ":relation", ":relation_with_king"),
                (assign, ":lord_no", ":troop_no"),
            (try_end),
        (try_end),
        (assign, reg0, ":lord_no"),
    ]
  ),

  # script_rebellion_get_lord_highest_controversy_in_faction
  # Script Get the lord of the specified faction with the highest contraversy 
  # Input: arg1 = orig_faction, arg2 = rebel_faction
  # Output: reg0 = lord_no
  ("rebellion_get_lord_highest_controversy_in_faction",
    [
        (store_script_param_1, ":orig_faction"),
        (store_script_param_2, ":rebel_faction"),
        (assign, ":controversy", 0),
        (assign, ":lord_no", 0),
        (assign, ":troop_no", 0),
        (assign, ":was_marshall", 0),
        (try_for_range, ":troop_no", lords_begin, lords_end),
            (store_troop_faction, ":lord_faction", ":troop_no"),
            (eq , ":lord_faction", ":orig_faction"),
            (troop_get_slot, ":lord_controversy", ":troop_no", slot_troop_controversy),
            (try_begin),
                (gt, ":lord_controversy", ":controversy"),
                (assign, ":controversy", ":lord_controversy"),
                (assign, ":lord_no", ":troop_no"),
            (try_end),
        (try_end),
        (try_begin),
            (try_begin),
                (faction_slot_eq, ":orig_faction", slot_faction_marshall, ":lord_no"),
                (assign, ":was_marshall", 1),
            (try_end),
            (neq, ":lord_no", "trp_player"),
            (call_script, "script_change_troop_faction", ":lord_no", ":rebel_faction"),
            (faction_get_slot, ":party_no", ":rebel_faction", slot_faction_number_of_parties),
            (val_add, ":party_no", 1),
            (faction_set_slot, ":rebel_faction", slot_faction_number_of_parties, ":party_no"),
            (try_begin),
                (eq, ":was_marshall", 1),
                (troop_get_type, reg4, ":lord_no"),
                (str_store_troop_name, s1, ":lord_no"),
                (str_store_faction_name, s2, ":rebel_faction"), 
                (str_store_faction_name, s3, ":orig_faction"),
                (str_store_string, s4, "str_lord_defects_marshall", 0xFF0000),
                #(display_log_message, "@{!}{s4}"),
            (else_try),
                (troop_get_type, reg4, ":lord_no"),
                (str_store_troop_name, s1, ":lord_no"),
                (str_store_faction_name, s2, ":rebel_faction"), 
                (str_store_faction_name, s3, ":orig_faction"),
                (str_store_string, s4, "str_lord_defects_ordinary"),
                #(display_log_message, "@{!}{s4}"),
            (try_end),
            
            (faction_get_slot, ":faction_king", ":orig_faction", slot_faction_leader),  
            (call_script, "script_troop_change_relation_with_troop", ":lord_no", ":faction_king", -10), 
            (call_script, "script_troop_change_relation_with_troop", ":faction_king", ":lord_no", -20),
            
            (faction_get_slot, ":rebel_king", ":rebel_faction", slot_faction_leader),   
            (call_script, "script_troop_change_relation_with_troop", ":lord_no", ":rebel_king", 10),    
            (call_script, "script_troop_change_relation_with_troop", ":rebel_king", ":lord_no", 20),
        (try_end),
        (troop_set_slot, ":lord_no", slot_troop_controversy, 15),
        (assign, reg0, ":lord_no"),
    ]
  ),

  # script_rebellion_get_lord_lowest_relation_in_faction
  # Script Get the lord of the specified faction with the lowest relation to their liege   
  # Input: arg1 = orig_faction, arg2 = rebel_faction
  # Output: reg0 = lord_no
  ("rebellion_get_lord_lowest_relation_in_faction",
    [
        (store_script_param_1, ":orig_faction"),
        (store_script_param_2, ":rebel_faction"),
        (assign, ":relation", 100),
        (assign, ":troop_no", 0),
        (faction_get_slot, ":faction_king", ":orig_faction", slot_faction_leader),
        (try_for_range, ":troop_no", lords_begin, lords_end),
            (store_troop_faction, ":lord_faction", ":troop_no"),
            (eq , ":lord_faction", ":orig_faction"),
            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_king"),
            (assign, ":relation_with_king", reg0),  
            (try_begin),
                (eq , ":orig_faction", ":lord_faction"),
                (le, ":relation_with_king", ":relation"),
                (assign, ":relation", ":relation_with_king"),
                (assign, ":lord_no", ":troop_no"),
            (try_end),
        (try_end),

        (try_begin),        
            (neq, ":lord_no", "trp_player"),
            (try_begin),
                (faction_slot_eq, ":orig_faction", slot_faction_marshall, ":lord_no"),
                (assign, ":was_marshall", 1),
            (try_end),
            (call_script, "script_change_troop_faction", ":lord_no", ":rebel_faction"),
            (faction_get_slot, ":party_no", ":rebel_faction", slot_faction_number_of_parties),
            (val_add, ":party_no", 1),
            (faction_set_slot, ":rebel_faction", slot_faction_number_of_parties, ":party_no"),
            
            (try_begin),
                (eq, ":was_marshall", 1),
                (troop_get_type, reg4, ":lord_no"),
                (str_store_troop_name, s1, ":lord_no"),
                (str_store_faction_name, s2, ":rebel_faction"), 
                (str_store_faction_name, s3, ":orig_faction"),
                (str_store_string, s4, "str_lord_defects_marshall", 0xFF0000),
                #(display_log_message, "@{!}{s4}"),
            (else_try),
                (troop_get_type, reg4, ":lord_no"),
                (str_store_troop_name, s1, ":lord_no"),
                (str_store_faction_name, s2, ":rebel_faction"), 
                (str_store_faction_name, s3, ":orig_faction"),
                (str_store_string, s4, "str_lord_defects_ordinary"),
                #(display_log_message, "@{!}{s4}"),
            (try_end),
            
            (faction_get_slot, ":faction_king", ":orig_faction", slot_faction_leader),  
            (call_script, "script_troop_change_relation_with_troop", ":lord_no", ":faction_king", -10), 
            (call_script, "script_troop_change_relation_with_troop", ":faction_king", ":lord_no", -20),
            
            (faction_get_slot, ":rebel_king", ":rebel_faction", slot_faction_leader),   
            (call_script, "script_troop_change_relation_with_troop", ":lord_no", ":rebel_king", 10),    
            (call_script, "script_troop_change_relation_with_troop", ":rebel_king", ":lord_no", 20),
        (try_end),
        (troop_set_slot, ":lord_no", slot_troop_controversy, 15),
        (assign, reg0, ":lord_no"),
    ]
  ),

  # script_rebellion_clianment_revolt_start
  # Script starts the rebellion for claimant
  # Input: arg1 = orig_faction, arg2 = rebel_center, arg3 = rebel_lord, arg5 = rebel_faction, arg6 = rebel_claimed
  # Output: none
  ("rebellion_clianment_revolt_start",
   [
        (store_script_param_1, ":orig_faction"),
        (store_script_param_2, ":rebel_center"),
        (store_script_param, ":rebel_lord", 3),
        (store_script_param, ":rebel_faction", 4),
        (store_script_param, ":rebel_claimed", 5),

        (troop_set_slot, ":rebel_lord", slot_troop_home, ":rebel_center"),
        (troop_set_slot, ":rebel_lord", slot_troop_wealth, 100000),
        (store_random_in_range, ":renown", 850, 1200),
        (troop_set_slot, ":rebel_lord", slot_troop_renown, ":renown"),

        (faction_set_slot, ":rebel_faction", slot_faction_state, sfs_active),
        (faction_set_slot, ":rebel_faction", slot_faction_number_of_parties, 1),
        (troop_set_slot, ":rebel_lord", slot_troop_occupation, slto_kingdom_hero),
        (faction_set_slot, ":rebel_faction",  slot_faction_leader, ":rebel_lord"),
        (troop_set_slot, ":rebel_lord", slot_troop_cur_center, ":rebel_center"), 
        (faction_set_note_available, ":rebel_faction", 1),
        (call_script, "script_change_troop_faction", ":rebel_lord", ":rebel_faction"),

        (call_script, "script_create_kingdom_hero_party", ":rebel_lord", ":rebel_center"),
        (call_script, "script_diplomacy_start_war_between_kingdoms", ":rebel_faction", ":orig_faction", 1),
        
        (faction_get_slot, ":faction_king", ":orig_faction", slot_faction_leader),
        (store_random_in_range, ":relation", -30, -5),
        (call_script, "script_troop_change_relation_with_troop", ":rebel_lord", ":faction_king", ":relation"),  
        (call_script, "script_troop_change_relation_with_troop", ":faction_king", ":rebel_lord", ":relation"),  
        (call_script, "script_rebellion_set_faction_leader_title", ":rebel_lord", ":rebel_faction"),
        (call_script, "script_give_center_to_lord", ":rebel_center",  ":rebel_lord", 0),

        #(troop_set_slot, ":orig_pretender", slot_troop_cur_center, -1),
        #(troop_set_note_available, ":orig_pretender", 0),

        (party_set_slot, ":rebel_claimed", slot_center_ex_faction, ":rebel_faction"), #Sets a rebel claim on another center in the old faction
        (call_script, "script_rebellion_start", ":orig_faction", ":rebel_faction", ":rebel_center"),    
   ]
  ),

  # script_rebellion_start
  # Script starts the rebellion for the supplied rebel faction   
  # Input: arg1 = orig_faction, arg2 = rebel_faction, arg3 = rebel_center
  # Output: none
  ("rebellion_start",
   [
        (store_script_param, ":orig_faction", 1),
        (store_script_param, ":rebel_faction", 2),
        (store_script_param, ":rebel_center", 3),

       (faction_get_slot, ":faction_instability", ":orig_faction", slot_faction_instability),
       (assign, ":no_of_faction_lords", 0),
       
       (try_for_range, ":troop_no", lords_begin, lords_end),
            (store_troop_faction, ":lord_faction", ":troop_no"),
            (eq , ":lord_faction", ":orig_faction"),
            (val_add, ":no_of_faction_lords", 1),
       (try_end),
       
       (try_begin),
            (ge, ":faction_instability", 50),
            (store_div, ":lord_defection_no", ":no_of_faction_lords", 2),
            (store_div, ":lord_defection_contraversy", ":lord_defection_no", 2),
            (store_sub, ":lord_defection_relation", ":lord_defection_no", ":lord_defection_contraversy"),#  
       (else_try),
            (le, ":faction_instability", 49),
            (store_div, ":lord_defection_no", ":no_of_faction_lords", 3),
            (store_div, ":lord_defection_contraversy", ":lord_defection_no", 2),
            (store_sub, ":lord_defection_relation", ":lord_defection_no", ":lord_defection_contraversy"),
       (try_end),
       
       ## BEGIN LORD DEFECTIONS TO REBELS
       (try_for_range, ":defected_count", 0, ":lord_defection_contraversy"),
            (call_script, "script_rebellion_get_lord_highest_controversy_in_faction", ":orig_faction", ":rebel_faction"),
            (val_add, ":defected_count", 1),
       (try_end),
       
       (assign, ":defected_count", 0),
       (try_for_range, ":defected_count", 0, ":lord_defection_relation"),
            (call_script, "script_rebellion_get_lord_lowest_relation_in_faction", ":orig_faction", ":rebel_faction"),
            (val_add, ":defected_count", 1),
       (try_end),
       ## END LORD DEFECTIONS TO REBELS 

       (call_script, "script_recalculate_ais", ":rebel_faction"),
       
        (faction_get_slot, ":rebel_king", ":rebel_faction", slot_faction_leader),   
        (str_store_faction_name, s52, ":rebel_faction"),
        (assign, reg52, ":lord_defection_no"),
        (str_store_troop_name, s53, ":rebel_king"),
        (str_store_party_name, s54, ":rebel_center"),
        (dialog_box, "@A messenger finds you and informs you that {s53} has rebelled and the loyal city of {s54} is now the new capital of {s52}. The rebellion is strengthened by {reg52} lords who defecteed and joined {s52} .", "@{s52}: REBELLION"),
        (call_script, "script_appoint_faction_marshall", ":rebel_faction", ":rebel_king"),
     ]),

  # script_rebellion_faction_call
  # Script starts the rebellion for the supplied rebel faction   
  # Input: arg1 = faction_id
  # Output: none
  ("rebellion_faction_call",
   [
        (store_script_param, ":orig_faction", 1), 
        (store_script_param, ":rebel_center", 2),  
        (store_script_param, ":rebel_lord", 3),  
        (store_script_param, ":rebel_faction", 4),  
        (store_script_param, ":rebel_claimed", 5),   

        (troop_set_name, ":rebel_lord", s1),
        (party_set_name, ":rebel_lord", "str_s5_s_party"),
        (call_script, "script_rebellion_clianment_revolt_start", ":orig_faction", ":rebel_center", ":rebel_lord", ":rebel_faction", ":rebel_claimed"),

     ]),

  # script_rebellion_set_faction_leader_title
  # Script set the correct faction title to the troop
  # Input: arg1 = faction_id, arg2 = lord_no
  # Output: none
  ("rebellion_set_faction_leader_title",
   [
          (store_script_param, ":faction_id", 1), 
          (store_script_param, ":lord_no", 2), 
          (faction_get_slot, ":faction_index", ":faction_id", slot_kaoses_faction_title_type),
          (troop_get_type, ":gender", ":lord_no"),
          (try_begin),
              (this_or_next|eq, ":faction_index", "fac_kingdom_1"),
              (this_or_next|eq, ":faction_index", "fac_kingdom_7"),
              (eq, ":faction_index", "fac_kingdom_13"),
              (try_begin),
                  (eq, ":gender", 0),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_1_leader_male"),
                  (str_store_troop_name, s5, ":lord_no"),
              (else_try),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_1_leader_female"),
                  (str_store_troop_name, s5, ":lord_no"),
              (try_end),
          (else_try),
              (this_or_next|eq, ":faction_index", "fac_kingdom_2"),
              (this_or_next|eq, ":faction_index", "fac_kingdom_8"),
              (eq, ":faction_index", "fac_kingdom_14"),
              (try_begin),
                  (eq, ":gender", 0),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_2_leader_male"),
                  (str_store_troop_name, s5, ":lord_no"),
              (else_try),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_2_leader_female"),
                  (str_store_troop_name, s5, ":lord_no"),
              (try_end),
          (else_try),
              (this_or_next|eq, ":faction_index", "fac_kingdom_3"),
              (this_or_next|eq, ":faction_index", "fac_kingdom_9"),
              (eq, ":faction_index", "fac_kingdom_15"),
              (try_begin),
                  (eq, ":gender", 0),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_3_leader_male"),
                  (str_store_troop_name, s5, ":lord_no"),
              (else_try),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_3_leader_female"),
                  (str_store_troop_name, s5, ":lord_no"),
              (try_end),
          (else_try),
              (this_or_next|eq, ":faction_index", "fac_kingdom_4"),
              (this_or_next|eq, ":faction_index", "fac_kingdom_10"),
              (eq, ":faction_index", "fac_kingdom_16"),
              (try_begin),
                  (eq, ":gender", 0),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_4_leader_male"),
                  (str_store_troop_name, s5, ":lord_no"),
              (else_try),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_4_leader_female"),
                  (str_store_troop_name, s5, ":lord_no"),
              (try_end),
          (else_try),
              (this_or_next|eq, ":faction_index", "fac_kingdom_5"),
              (this_or_next|eq, ":faction_index", "fac_kingdom_11"),
              (eq, ":faction_index", "fac_kingdom_17"),
              (try_begin),
                  (eq, ":gender", 0),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_5_leader_male"),
                  (str_store_troop_name, s5, ":lord_no"),
              (else_try),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_5_leader_female"),
                  (str_store_troop_name, s5, ":lord_no"),
              (try_end),
          (else_try),
              (this_or_next|eq, ":faction_index", "fac_kingdom_6"),
              (this_or_next|eq, ":faction_index", "fac_kingdom_12"),
              (eq, ":faction_index", "fac_kingdom_18"),
              (try_begin),
                  (eq, ":gender", 0),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_6_leader_male"),
                  (str_store_troop_name, s5, ":lord_no"),
              (else_try),
                  (str_store_troop_name_plural, s0, ":lord_no"),
                  (str_store_string, s1, "str_kingdom_6_leader_female"),
                  (str_store_troop_name, s5, ":lord_no"),
              (try_end),
          (else_try),
              (eq, ":faction_index", "fac_player_supporters_faction"),
              (try_begin),
                  (eq , "$kaos_has_custom_title", 1),
                  (try_begin),
                      (eq, ":gender", 0),
                      (str_store_troop_name_plural, s0, ":lord_no"),
                      (str_store_troop_name, s1, "trp_dummy_5_king"),
                      (str_store_troop_name, s5, ":lord_no"),
                  (else_try),
                      (str_store_troop_name_plural, s0, ":lord_no"),
                      (str_store_troop_name_plural, s1, "trp_dummy_5_king"),
                      (str_store_troop_name, s5, ":lord_no"),
                  (try_end),
              (else_try),
                  (try_begin),
                      (eq, ":gender", 0),
                      (str_store_troop_name_plural, s0, ":lord_no"),
                      (str_store_string, s1, "str_new_faction_title_male_player_king"),
                      (str_store_troop_name, s5, ":lord_no"),
                  (else_try),
                      (str_store_troop_name_plural, s0, ":lord_no"),
                      (str_store_string, s1, "str_new_faction_title_female_player_queen"),
                      (str_store_troop_name, s5, ":lord_no"),
                  (try_end),
              (try_end),
          (try_end),
          (troop_set_name, ":lord_no", s1),
          (party_set_name, ":lord_no", "str_s5_s_party"),
   ]
  ),

  # script_rebellion_faction_civil_war
  # Script starts civial war for the specified faction 
  # Input: arg1 = faction_id
  # Output: none
  ("rebellion_faction_civil_war",
    [
        (store_script_param, ":orig_faction", 1), 

        (assign, ":total_lords", 0),
        (assign, ":total_disgruntled_lords", 0),
        (assign, ":renown", 0),
        (assign, ":lord_no", 0),

        (try_begin),
            (eq, ":orig_faction", "fac_kingdom_1"),
            (assign, ":faction_id", "fac_kingdom_13"),
        (else_try),
            (eq, ":orig_faction", "fac_kingdom_2"),
            (assign, ":faction_id", "fac_kingdom_14"),
        (else_try),
            (eq, ":orig_faction", "fac_kingdom_3"),
            (assign, ":faction_id", "fac_kingdom_15"),
        (else_try),
            (eq, ":orig_faction", "fac_kingdom_4"),
            (assign, ":faction_id", "fac_kingdom_16"),
        (else_try),
            (eq, ":orig_faction", "fac_kingdom_5"),
            (assign, ":faction_id", "fac_kingdom_17"),
        (else_try),
            (eq, ":orig_faction", "fac_kingdom_6"),
            (assign, ":faction_id", "fac_kingdom_18"),
        (else_try),
            (eq,"$background_answer_3",cb_king),
            (eq, ":orig_faction", "fac_player_supporters_faction"),
            (try_begin),
              (eq, "$kaos_kings_kingdom", 1),
              (assign, ":faction_id", "fac_kingdom_13"),
            (else_try),
              (eq, "$kaos_kings_kingdom", 2),
              (assign, ":faction_id", "fac_kingdom_14"),
            (else_try),
              (eq, "$kaos_kings_kingdom", 3),
              (assign, ":faction_id", "fac_kingdom_15"),
            (else_try),
              (eq, "$kaos_kings_kingdom", 4),
              (assign, ":faction_id", "fac_kingdom_16"),
            (else_try),
              (eq, "$kaos_kings_kingdom", 5),
              (assign, ":faction_id", "fac_kingdom_17"),
            (else_try),
              (eq, "$kaos_kings_kingdom", 6),
              (assign, ":faction_id", "fac_kingdom_18"),
            (try_end),
        (try_end),

        (faction_set_slot, ":faction_id", slot_faction_state, sfs_active),
        (faction_set_note_available, ":faction_id", 1),

        (try_for_range, ":lord", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
            (store_troop_faction, ":lord_faction", ":lord"),
            (eq, ":lord_faction", ":orig_faction"),
            (val_add, ":total_lords", 1),
            (faction_get_slot, ":liege", ":orig_faction", slot_faction_leader), 
            (call_script, "script_calculate_troop_political_factors_for_liege", ":lord", ":liege"),
            (try_begin),
                (le, reg3, -10),
                #(le, reg3, 10),# TEST LINE
                (val_add, ":total_disgruntled_lords", 1),
                (troop_get_slot, ":troop_renown", ":lord", slot_troop_renown),
                (try_begin),
                    (gt, ":troop_renown", ":renown"),
                    (assign, ":renown", ":troop_renown"),
                    (assign, ":lord_no", ":lord"),
                (try_end),
                (faction_get_slot, ":party_no", ":faction_id", slot_faction_number_of_parties),
                (val_add, ":party_no", 1),
                (faction_set_slot, ":faction_id", slot_faction_number_of_parties, ":party_no"),
                (call_script, "script_change_troop_faction", ":lord", ":faction_id"),

            (try_end),
           #####################  debugging messages ################################
           (try_begin),    
              (eq, "$kaos_debug_mode", 1),  
              (str_store_faction_name, s52, ":faction_id"),
              (assign, reg54, ":total_disgruntled_lords"),
              (str_store_troop_name, s55, ":lord"),
              (display_log_message, "@{!} {s55} would be part of the civil war {reg54}", 0xFF0000),
           (try_end),    
           #####################  debugging messages ################################  
        (try_end),
        (faction_set_slot, ":faction_id",  slot_faction_leader, ":lord_no"),
        (call_script, "script_diplomacy_start_war_between_kingdoms", ":faction_id", ":orig_faction", 1),
        (call_script, "script_rebellion_set_faction_leader_title" , ":lord_no", ":faction_id"),
  ]), 
   

#KAOS (START)
  ("set_player_kingdom_init",
  [
    (set_show_messages, 0),
    (store_script_param, ":orginal_faction", 1),
    (store_script_param, ":capital", 2),
    (store_script_param, ":culture", 3),
    (store_script_param, ":troop_start", 4),
    (store_script_param, ":troop_end", 5),
    (store_script_param, ":liege", 6),
    (store_script_param, ":scene", 7),
    (remove_troop_from_site,":liege",":scene"),

    (str_store_troop_name, s10, "trp_player"),

    (call_script, "script_activate_player_faction", "trp_player"),
    (call_script, "script_give_center_to_faction_aux", ":capital", "fac_player_supporters_faction"),
    (call_script, "script_give_center_to_lord", ":capital", "trp_player", 1),
    (troop_set_slot, "trp_player", slot_troop_leaded_party, 1),
    (troop_set_slot, "trp_player", slot_troop_cur_center, ":capital"),
    (troop_set_slot, "trp_player", slot_troop_home, ":capital"),

    #####Removing the active King 
     #(call_script,"script_change_troop_faction",":liege","fac_player_supporters_faction"),
     (troop_get_slot, ":king_party", ":liege", slot_troop_leaded_party),
     (remove_party,":king_party"),
     (troop_set_slot, ":liege", slot_troop_leaded_party, -1),
     (troop_set_slot, ":liege", slot_troop_occupation, slto_inactive),
     (troop_set_slot, ":liege", slot_troop_cur_center, -1),
     (troop_set_slot, ":liege", slot_troop_home, -1),
     (troop_set_note_available, ":liege", 0),
    #####King remove end

     (try_for_range,":cur_village",villages_begin,villages_end),
     (party_slot_eq, ":cur_village", slot_village_bound_center, ":capital"),
     (party_set_faction, ":cur_village", "fac_player_supporters_faction"),
     (try_end),
     (assign, "$g_player_court", ":capital"),
    ###capitol transfer end
   
    ##culture the player faction will have. (The recruit type for your kingdoms villages) 
         (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, ":culture"),
         (faction_set_slot, "fac_player_faction",  slot_faction_culture, ":culture"),
    ##culture end

         (assign, "$players_kingdom", "fac_player_supporters_faction"),
    ##knights/npc lords Transferring to the players kingdom
        (try_for_range,":npc",":troop_start",":troop_end"),      
            (call_script,"script_change_troop_faction",":npc","fac_player_supporters_faction"),
            (troop_set_slot, ":npc", slot_troop_occupation, slto_kingdom_hero),    
            (store_random_in_range,":new_relation",0,35),
            (call_script, "script_troop_change_relation_with_troop", "trp_player", ":npc", ":new_relation"),
        (try_end),  
    
        (try_for_range,":npc_lady",kingdom_ladies_begin,kingdom_ladies_end),   
            (store_faction_of_troop, ":lady_faction", ":npc_lady"),
            (eq, ":lady_faction", ":orginal_faction"),
            (call_script,"script_change_troop_faction",":npc_lady","fac_player_supporters_faction"),
        (try_end),  

    #####Knights/NPC lord end    
       (faction_set_note_available,"fac_player_supporters_faction",1),
       (call_script, "script_update_faction_notes","fac_player_supporters_faction"),
       (call_script, "script_change_player_right_to_rule", 25),


    ##Set old king as player parent
     (troop_set_slot, "trp_player", slot_troop_father, ":liege"),

     (assign, "$players_kingdom_name_set", 1),
     (faction_set_slot, ":orginal_faction", slot_faction_state, sfs_inactive),  
     (store_random_in_range,":new_controversy",0,45),
     (troop_set_slot, "trp_player", slot_troop_controversy, ":new_controversy"), 
     (call_script, "script_update_all_notes"), 
     
     (try_begin),
          (eq, ":orginal_faction", "fac_kingdom_1"),
          (assign, "$kaos_kings_kingdom", 1),
          (str_store_string, s1, "str_kaos_swadia_king"),
          (faction_set_name, "fac_player_supporters_faction", s1),
          (faction_set_color, "fac_player_supporters_faction", 0xEE7744),      
          (faction_set_slot, "fac_player_supporters_faction", slot_kaoses_faction_title_type, "fac_kingdom_1"),
     (else_try),
          (eq, ":orginal_faction", "fac_kingdom_2"),
          (assign, "$kaos_kings_kingdom", 2),
          (str_store_string, s1, "str_kaos_Vaegirs_king"),
          (faction_set_name, "fac_player_supporters_faction", s1),
          (faction_set_color, "fac_player_supporters_faction", 0xCCBB99),
          (faction_set_slot, "fac_player_supporters_faction", slot_kaoses_faction_title_type, "fac_kingdom_2"),
     (else_try),
          (eq, ":orginal_faction", "fac_kingdom_3"),
          (assign, "$kaos_kings_kingdom", 3),
          (str_store_string, s1, "str_kaos_Khergit_king"),
          (faction_set_name, "fac_player_supporters_faction", s1),
          (faction_set_color, "fac_player_supporters_faction", 0xCC99FF),
          (faction_set_slot, "fac_player_supporters_faction", slot_kaoses_faction_title_type, "fac_kingdom_3"),
     (else_try),
          (eq, ":orginal_faction", "fac_kingdom_4"),
          (assign, "$kaos_kings_kingdom", 4),
          (str_store_string, s1, "str_kaos_Nords_king"),
          (faction_set_name, "fac_player_supporters_faction", s1),
          (faction_set_color, "fac_player_supporters_faction", 0x33DDDD),
          (faction_set_slot, "fac_player_supporters_faction", slot_kaoses_faction_title_type, "fac_kingdom_4"),
     (else_try),
          (eq, ":orginal_faction", "fac_kingdom_5"),
          (assign, "$kaos_kings_kingdom", 5),
          (str_store_string, s1, "str_kaos_Rhodoks_king"),
          (faction_set_name, "fac_player_supporters_faction", s1),
          (faction_set_color, "fac_player_supporters_faction", 0x33DD33),
          (faction_set_slot, "fac_player_supporters_faction", slot_kaoses_faction_title_type, "fac_kingdom_5"),
     (else_try),
          (eq, ":orginal_faction", "fac_kingdom_6"),
          (assign, "$kaos_kings_kingdom", 6),
          (str_store_string, s1, "str_kaos_Sarranid_king"),
          (faction_set_name, "fac_player_supporters_faction", s1),
          (faction_set_color, "fac_player_supporters_faction", 0xDDDD33),
          (faction_set_slot, "fac_player_supporters_faction", slot_kaoses_faction_title_type, "fac_kingdom_6"),
     (try_end),


     (faction_set_slot, "fac_player_supporters_faction",  slot_faction_leader, "trp_player"),
     (troop_set_name, "trp_player", s10),
     (troop_set_plural_name, "trp_player", s10),
     (assign, "$kaos_title_run", 1),

     (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", "trp_player", "fac_player_supporters_faction"),  
     (troop_get_slot, ":troop_party", "trp_player", slot_troop_leaded_party),
     (str_store_troop_name, s5, "trp_player"),
     (party_set_name, ":troop_party", "str_s5_s_party"),
     (troop_set_plural_name, "trp_player", s5),

     (assign, "$g_player_minister", "trp_temporary_minister"),
     (troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),


    (set_show_messages, 1),
    ]),





#KAOS (START)
  ("set_player_prince_init",
  [
    (set_show_messages, 0),

    (store_script_param, ":orginal_faction", 1),
    (store_script_param, ":troop_start", 2),
    (store_script_param, ":troop_end", 3),
    (store_script_param, ":liege", 4),

    (assign, ":town_lord", 0),
    (assign, ":center", 0),

    (str_store_troop_name, s10, "trp_player"),

    (call_script, "script_player_join_faction", ":orginal_faction"),

    (assign, "$player_has_homage" ,1),
    (assign, "$g_player_banner_granted", 1),
    (assign, "$g_invite_faction", 1),
    (assign, "$g_invite_faction_lord", 1),

    (store_random_in_range,":new_relation",22,44),
    (call_script, "script_troop_change_relation_with_troop", "trp_player", ":liege", ":new_relation"),


    ##knights/npc lords Transferring to the players kingdom
    (try_for_range,":npc",":troop_start",":troop_end"),      
        (store_random_in_range,":new_relation",-22,39),
        (call_script, "script_troop_change_relation_with_troop", "trp_player", ":npc", ":new_relation"),
    (try_end),  

    (try_for_range,":npc_lady",kingdom_ladies_begin,kingdom_ladies_end),   
        (store_faction_of_troop, ":lady_faction", ":npc_lady"),
        (eq, ":lady_faction", ":orginal_faction"),
        (store_random_in_range,":new_relation",-2,18),
        (call_script, "script_troop_change_relation_with_troop", "trp_player", ":npc_lady", ":new_relation"),
    (try_end),  

    (call_script, "script_change_player_right_to_rule", 22),
    (troop_set_slot, "trp_player", slot_troop_father, ":liege"),

    (store_random_in_range,":new_controversy",10,45),
    (troop_set_slot, "trp_player", slot_troop_controversy, ":new_controversy"), 

    (call_script, "script_kaos_get_lord_highest_controversy_in_faction", ":orginal_faction"),
    (assign, ":lord_no", reg0),
    (try_for_range, ":center_no", towns_begin, castles_end),#lords_begin lords_end
        (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
        (eq , ":town_lord", ":lord_no"),
        (assign, ":center", ":center_no"),
    (try_end),

    (try_begin),
        (eq, ":center", 0),
        (call_script, "script_kaos_get_lord_lowest_relation_in_faction", ":orginal_faction"),
        (assign, ":lord_no", reg0),
        (try_for_range, ":center_no", towns_begin, castles_end),#lords_begin lords_end
            (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
            (eq , ":town_lord", ":lord_no"),
            (assign, ":center", ":center_no"),
        (try_end),
    (try_end),


    #Fallback position if no center found before
    (try_begin),
        (eq, ":center", 0),
        (try_begin),
            (eq, ":orginal_faction", "fac_kingdom_1"),
            (assign, ":center", "p_castle_6"),
            (party_get_slot, ":town_lord", "p_castle_6", slot_town_lord),
        (else_try),
            (eq, ":orginal_faction", "fac_kingdom_2"),
            (assign, ":center", "p_castle_37"),
            (party_get_slot, ":town_lord", "p_castle_37", slot_town_lord),
        (else_try),
            (eq, ":orginal_faction", "fac_kingdom_3"),
            (assign, ":center", "p_castle_22"),
            (party_get_slot, ":town_lord", "p_castle_22", slot_town_lord),
        (else_try),
            (eq, ":orginal_faction", "fac_kingdom_4"),
            (assign, ":center", "p_castle_32"),
            (party_get_slot, ":town_lord", "p_castle_32", slot_town_lord),
        (else_try),
            (eq, ":orginal_faction", "fac_kingdom_5"),
            (assign, ":center", "p_castle_16"),
            (party_get_slot, ":town_lord", "p_castle_16", slot_town_lord),
        (else_try),
            (eq, ":orginal_faction", "fac_kingdom_6"),
            (assign, ":center", "p_castle_41"),
            (party_get_slot, ":town_lord", "p_castle_41", slot_town_lord),
        (try_end),
    (try_end),

    (call_script, "script_get_poorest_village_of_faction", ":orginal_faction"),
    (assign, ":new_center", reg0),
    (call_script, "script_give_center_to_lord", ":new_center", ":town_lord", 0),

    (call_script, "script_troop_change_relation_with_troop", "trp_player", ":town_lord", -30),

    (call_script, "script_give_center_to_lord", ":center", "trp_player", 0),
    (assign, "$g_invite_offered_center", ":center"),
    (assign, "$kaos_prince_start", ":center"),
    (assign, reg0, ":center"),

    (assign,"$background_answer_2", cb2_page),
    (try_begin),
          (eq,"$character_gender",tf_female),
          (assign,"$background_answer_3",cb3_lady_in_waiting),
    (else_try),
         (assign,"$background_answer_3",cb3_squire),
    (try_end),

    (troop_set_name, "trp_player", s10),
    (troop_set_plural_name, "trp_player", s10),
    (assign, "$kaos_title_run", 1),

    (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", "trp_player", ":orginal_faction"),  
    (troop_get_slot, ":troop_party", "trp_player", slot_troop_leaded_party),
    (str_store_troop_name, s5, "trp_player"),
    (party_set_name, ":troop_party", "str_s5_s_party"),

    (call_script, "script_update_all_notes"), 

    (set_show_messages, 1),
  ]
  ),



#KAOS (START)
  ("set_player_vassal_init",
  [
    (set_show_messages, 0),
    (store_script_param, ":orginal_faction", 1),
    (store_script_param, ":troop_start", 2),
    (store_script_param, ":troop_end", 3),
    (store_script_param, ":liege", 4),

    (str_store_troop_name, s10, "trp_player"),
    (call_script, "script_player_join_faction", ":orginal_faction"),

    (assign, "$player_has_homage" ,1),
    (assign, "$g_player_banner_granted", 1),
    (assign, "$g_invite_faction", 1),
    (assign, "$g_invite_faction_lord", 1),

    (call_script, "script_get_poorest_village_of_faction", "fac_kingdom_1"),
    (assign, ":center", reg0),
    (call_script, "script_give_center_to_lord", ":center", "trp_player", 0),
    (assign, "$g_invite_offered_center", ":center"),
    (assign, "$kaos_vasal_start", ":center"),


    (store_random_in_range,":new_relation",15,35),
    (call_script, "script_troop_change_relation_with_troop", "trp_player", ":liege", ":new_relation"),


    ##knights/npc lords Transferring to the players kingdom
    (try_for_range,":npc",":troop_start",":troop_end"),      
        (store_random_in_range,":new_relation",-15,35),
        (call_script, "script_troop_change_relation_with_troop", "trp_player", ":npc", ":new_relation"),
    (try_end),  

    (try_for_range,":npc_lady",kingdom_ladies_begin,kingdom_ladies_end),   
        (store_faction_of_troop, ":lady_faction", ":npc_lady"),
        (eq, ":lady_faction", ":orginal_faction"),
        (store_random_in_range,":new_relation",-1,15),
        (call_script, "script_troop_change_relation_with_troop", "trp_player", ":npc_lady", ":new_relation"),
    (try_end),  

    (call_script, "script_change_player_right_to_rule", 15),

    (store_random_in_range,":new_controversy",20,45),
    (troop_set_slot, "trp_player", slot_troop_controversy, ":new_controversy"), 


    (troop_set_name, "trp_player", s10),
    (troop_set_plural_name, "trp_player", s10),
    (assign, "$kaos_title_run", 1),

    (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", "trp_player", ":orginal_faction"),  
    (troop_get_slot, ":troop_party", "trp_player", slot_troop_leaded_party),
    (str_store_troop_name, s5, "trp_player"),
    (party_set_name, ":troop_party", "str_s5_s_party"),

    (call_script, "script_update_all_notes"), 

    (set_show_messages, 1),
  ]
  ),







########################################################################################################################
#  KAOS POLITICAL                                                                                                      #
########################################################################################################################


########################################################################################################################
#  Lav modifications                                                                                                   #
########################################################################################################################
  # Lav modifications start (custom lord notes)
    # This script is taken from Companions Overseer, remove it if you are already using Companions Overseer in your mod.
    ("lco_create_mesh",
        [
            (store_script_param, ":mesh", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (store_script_param, ":x_ratio", 4),
            (store_script_param, ":y_ratio", 5),
            (set_fixed_point_multiplier, 1000),
            (create_mesh_overlay, reg0, ":mesh"),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos61, ":x_ratio"),
            (position_set_y, pos61, ":y_ratio"),
            (overlay_set_size, reg0, pos61),
        ]
    ),

    # This script is taken from Companions Overseer, remove it if you are already using Companions Overseer in your mod.
    ("lco_create_button",
        [
            (store_script_param, ":caption", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (store_script_param, ":x_size", 4),
            (store_script_param, ":y_size", 5),
            (set_fixed_point_multiplier, 1000),
            (create_game_button_overlay, reg0, ":caption"),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos61, ":x_size"),
            (position_set_y, pos61, ":y_size"),
            (overlay_set_size, reg0, pos61),
        ]
    ),

    # This script is taken from Companions Overseer, remove it if you are already using Companions Overseer in your mod.
    ("lco_create_label",
        [
            (store_script_param, ":caption", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (store_script_param, ":scale", 4),
            (store_script_param, ":alignment", 5),
            (set_fixed_point_multiplier, 1000),
            (create_text_overlay, reg0, ":caption", ":alignment"),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos62, ":scale"),
            (position_set_y, pos62, ":scale"),
            (overlay_set_size, reg0, pos62),
        ]
    ),

    # This script is taken from Companions Overseer, remove it if you are already using Companions Overseer in your mod.
    ("lco_create_container",
        [
            (store_script_param, ":x", 1),
            (store_script_param, ":y", 2),
            (store_script_param, ":width", 3),
            (store_script_param, ":height", 4),
            (store_script_param, ":auto_start", 5),
            (set_fixed_point_multiplier, 1000),
            (str_clear, s40),
            (create_text_overlay, reg0, s40, 0x00002000),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos61, ":width"),
            (position_set_y, pos61, ":height"),
            (overlay_set_area_size, reg0, pos61),
            (try_begin),
                (neq, ":auto_start", 0),
                (set_container_overlay, reg0),
            (try_end),
        ]
    ),

    ("lco_create_troop_portrait",
        [
            (store_script_param, ":troop_id", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (store_script_param, ":x_scale", 4),
            (store_script_param, ":y_scale", 5),
            (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_troop_note_mesh", ":troop_id"),
            (set_fixed_point_multiplier, 1000),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos61, ":x_scale"),
            (position_set_y, pos61, ":y_scale"),
            (overlay_set_size, reg0, pos61),
        ]
    ),

    ("lco_create_textbox",
        [
            (store_script_param, ":x", 1),
            (store_script_param, ":y", 2),
            (store_script_param, ":width", 3),
            (store_script_param, ":height", 4),
            (set_fixed_point_multiplier, 1000),
            (create_simple_text_box_overlay, reg0),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos61, ":width"),
            (position_set_y, pos61, ":height"),
            (overlay_set_size, reg0, pos61),
        ]
    ),

########################################################################################################################
#  Lav modifications                                                                                                   #
########################################################################################################################

    ("get_dest_color_from_rgb",
      [
        (store_script_param, ":red", 1),
        (store_script_param, ":green", 2),
        (store_script_param, ":blue", 3),
        
        (assign, ":cur_color", 0xFF000000),
        (val_mul, ":green", 0x100),
        (val_mul, ":red", 0x10000),
        (val_add, ":cur_color", ":blue"),
        (val_add, ":cur_color", ":green"),
        (val_add, ":cur_color", ":red"),
        (assign, reg0, ":cur_color"),
    ]),
    
    ("convert_rgb_code_to_html_code",
      [
        (store_script_param, ":red", 1),
        (store_script_param, ":green", 2),
        (store_script_param, ":blue", 3),
        
        (str_store_string, s0, "@#"),
          
          (store_div, ":r_1", ":red", 0x10),
          (store_add, ":dest_string", "str_key_0", ":r_1"),
          (str_store_string, s1, ":dest_string"),
          (str_store_string, s0, "@{s0}{s1}"),
          
          (store_mod, ":r_2", ":red", 0x10),
          (store_add, ":dest_string", "str_key_0", ":r_2"),
          (str_store_string, s1, ":dest_string"),
          (str_store_string, s0, "@{s0}{s1}"),
          
          (store_div, ":g_1", ":green", 0x10),
          (store_add, ":dest_string", "str_key_0", ":g_1"),
          (str_store_string, s1, ":dest_string"),
          (str_store_string, s0, "@{s0}{s1}"),
          
          (store_mod, ":g_2", ":green", 0x10),
          (store_add, ":dest_string", "str_key_0", ":g_2"),
          (str_store_string, s1, ":dest_string"),
          (str_store_string, s0, "@{s0}{s1}"),
          
          (store_div, ":b_1", ":blue", 0x10),
          (store_add, ":dest_string", "str_key_0", ":b_1"),
          (str_store_string, s1, ":dest_string"),
          (str_store_string, s0, "@{s0}{s1}"),
          
          (store_mod, ":b_2", ":blue", 0x10),
          (store_add, ":dest_string", "str_key_0", ":b_2"),
          (str_store_string, s1, ":dest_string"),
          (str_store_string, s0, "@{s0}{s1}"),
      ]),
      
      ("convert_slot_no_to_color",
        [
          (store_script_param, ":cur_color", 1),
          
          (store_mod, ":blue", ":cur_color", 6),
          (val_div, ":cur_color", 6),
          (store_mod, ":green", ":cur_color", 6),
          (val_div, ":cur_color", 6),
          (store_mod, ":red", ":cur_color", 6),
          (val_mul, ":blue", 0x33),
          (val_mul, ":green", 0x33),
          (val_mul, ":red", 0x33),
          (assign, ":dest_color", 0xFF000000),
          (val_mul, ":green", 0x100),
          (val_mul, ":red", 0x10000),
          (val_add, ":dest_color", ":blue"),
          (val_add, ":dest_color", ":green"),
          (val_add, ":dest_color", ":red"),
          (assign, reg0, ":dest_color"),
      ]),
                          



] # scripts

# Manualy add these to module_scripts search for "process_sieges"
# add the lines in `process_sieges` insert after (ge, ":besieger_party", 0)
update_game_start = [
         #KAOS  (POLITICAL)
         (try_for_range, ":rebels", rebel_factions_begin, civil_factions_end),
            (faction_set_slot, ":rebels", slot_faction_state, sfs_inactive),
            (faction_set_note_available, ":rebels", 0),
         (try_end),

         (assign, "$kaos_civil_war", 1),
         (assign, "$kaos_royal_children", 1),
         (assign, "$kaos_restore", 1),
         (assign, "$kaos_debug_mode", 0),
         (assign, "$kaos_use_custom_name", 0),
         (assign, "$kaos_rebellion_home", 0),
         (assign, "$kaos_use_custom_title", 0),
         (assign, "$kaos_has_custom_title", 0),
         (assign, "$kaos_disabled", 1),
         (assign, "$kaos_kings_kingdom", 0),
         (assign, "$kaos_kings_vassal", 0),
         (assign, "$kaos_kings_prince", 0),
         (assign, "$kaos_title_run", 0),
         (assign, "$kaos_use_suffixes", 0),

         #KAOS  (POLITICAL)

         # Jrider + TITLES v0.0, init new titles
         (try_for_range, ":troop_no", active_npcs_begin, kingdom_ladies_end),
            (store_troop_faction, ":faction_no", ":troop_no"),
            (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":troop_no", ":faction_no"),
         (try_end),
          # Jrider -
]

# Manualy add these to module_scripts search for "process_sieges"
# add the lines in `process_sieges` insert after (ge, ":besieger_party", 0)
update_game_start2 = [
        #KAOS  (POLITICAL)
        (try_begin),
            (neg|is_between, ":center_lord", pretenders_begin, pretenders_end),
            (call_script, "script_create_kingdom_hero_party", ":center_lord", ":center_no"),
            (assign, ":lords_party", "$pout_party"),
            (party_attach_to_party, ":lords_party", ":center_no"),
            (party_set_slot, ":center_no", slot_town_player_odds, 1000),
        (try_end),    
        #KAOS  (POLITICAL)
]
update_game_start3 = [
         #KAOS  (POLITICAL)
         (store_random_in_range, ":swadian_date", 15, 100),
         (faction_set_slot, "fac_kingdom_7",  slot_rebellion_date, ":swadian_date"),
         (store_random_in_range, ":vaegir_date", 10, 85),
         (faction_set_slot, "fac_kingdom_8",  slot_rebellion_date, ":vaegir_date"),
         (store_random_in_range, ":khergit_date", 2, 70),
         (faction_set_slot, "fac_kingdom_9",  slot_rebellion_date, ":khergit_date"),
         (store_random_in_range, ":nord_date", 17, 79),
         (faction_set_slot, "fac_kingdom_10",  slot_rebellion_date, ":nord_date"),
         (store_random_in_range, ":rhodok_date", 8, 87),
         (faction_set_slot, "fac_kingdom_11",  slot_rebellion_date, ":rhodok_date"),
         (store_random_in_range, ":sarranid_date", 0, 90),
         (faction_set_slot, "fac_kingdom_12",  slot_rebellion_date, ":sarranid_date"),
         #KAOS  (POLITICAL)
]
update_game_start4 = [
      #KAOS  (POLITICAL) 
      (faction_set_slot, "fac_kingdom_7",  slot_faction_culture, "fac_culture_1"),
      (faction_set_slot, "fac_kingdom_8",  slot_faction_culture, "fac_culture_2"),
      (faction_set_slot, "fac_kingdom_9",  slot_faction_culture, "fac_culture_3"),
      (faction_set_slot, "fac_kingdom_10",  slot_faction_culture, "fac_culture_4"),
      (faction_set_slot, "fac_kingdom_11",  slot_faction_culture, "fac_culture_5"),
      (faction_set_slot, "fac_kingdom_12",  slot_faction_culture, "fac_culture_6"),

      (faction_set_slot, "fac_kingdom_13",  slot_faction_culture, "fac_culture_1"),
      (faction_set_slot, "fac_kingdom_14",  slot_faction_culture, "fac_culture_2"),
      (faction_set_slot, "fac_kingdom_15",  slot_faction_culture, "fac_culture_3"),
      (faction_set_slot, "fac_kingdom_16",  slot_faction_culture, "fac_culture_4"),
      (faction_set_slot, "fac_kingdom_17",  slot_faction_culture, "fac_culture_5"),
      (faction_set_slot, "fac_kingdom_18",  slot_faction_culture, "fac_culture_6"),

      (faction_set_slot, "fac_kingdom_7", slot_faction_banner, "mesh_banner_kingdom_e"),
      (faction_set_slot, "fac_kingdom_8", slot_faction_banner, "mesh_banner_kingdom_d"),
      (faction_set_slot, "fac_kingdom_9", slot_faction_banner, "mesh_banner_kingdom_f"),
      (faction_set_slot, "fac_kingdom_10", slot_faction_banner, "mesh_banner_kingdom_b"),
      (faction_set_slot, "fac_kingdom_11", slot_faction_banner, "mesh_banner_kingdom_a"),
      (faction_set_slot, "fac_kingdom_12", slot_faction_banner, "mesh_banner_kingdom_c"),

      (faction_set_slot, "fac_kingdom_13", slot_faction_banner, "mesh_banner_kingdom_a"),
      (faction_set_slot, "fac_kingdom_14", slot_faction_banner, "mesh_banner_kingdom_f"),
      (faction_set_slot, "fac_kingdom_15", slot_faction_banner, "mesh_banner_kingdom_c"),
      (faction_set_slot, "fac_kingdom_16", slot_faction_banner, "mesh_banner_kingdom_e"),
      (faction_set_slot, "fac_kingdom_17", slot_faction_banner, "mesh_banner_kingdom_b"),
      (faction_set_slot, "fac_kingdom_18", slot_faction_banner, "mesh_banner_kingdom_d"),

      (faction_set_slot, "fac_player_supporters_faction", slot_kaoses_faction_title_type, "fac_player_supporters_faction"),
      (faction_set_slot, "fac_kingdom_1", slot_kaoses_faction_title_type, "fac_kingdom_1"),
      (faction_set_slot, "fac_kingdom_2", slot_kaoses_faction_title_type, "fac_kingdom_2"),
      (faction_set_slot, "fac_kingdom_3", slot_kaoses_faction_title_type, "fac_kingdom_3"),
      (faction_set_slot, "fac_kingdom_4", slot_kaoses_faction_title_type, "fac_kingdom_4"),
      (faction_set_slot, "fac_kingdom_5", slot_kaoses_faction_title_type, "fac_kingdom_5"),
      (faction_set_slot, "fac_kingdom_6", slot_kaoses_faction_title_type, "fac_kingdom_6"),

      (faction_set_slot, "fac_kingdom_7", slot_kaoses_faction_title_type, "fac_kingdom_1"),
      (faction_set_slot, "fac_kingdom_8", slot_kaoses_faction_title_type, "fac_kingdom_2"),
      (faction_set_slot, "fac_kingdom_9", slot_kaoses_faction_title_type, "fac_kingdom_3"),
      (faction_set_slot, "fac_kingdom_10", slot_kaoses_faction_title_type, "fac_kingdom_4"),
      (faction_set_slot, "fac_kingdom_11", slot_kaoses_faction_title_type, "fac_kingdom_5"),
      (faction_set_slot, "fac_kingdom_12", slot_kaoses_faction_title_type, "fac_kingdom_6"),

      (faction_set_slot, "fac_kingdom_13", slot_kaoses_faction_title_type, "fac_kingdom_1"),
      (faction_set_slot, "fac_kingdom_14", slot_kaoses_faction_title_type, "fac_kingdom_2"),
      (faction_set_slot, "fac_kingdom_15", slot_kaoses_faction_title_type, "fac_kingdom_3"),
      (faction_set_slot, "fac_kingdom_16", slot_kaoses_faction_title_type, "fac_kingdom_4"),
      (faction_set_slot, "fac_kingdom_17", slot_kaoses_faction_title_type, "fac_kingdom_5"),
      (faction_set_slot, "fac_kingdom_18", slot_kaoses_faction_title_type, "fac_kingdom_6"),

      #KAOS  (POLITICAL)
]
#jrider Expanded nobility title system kit (v0.3.3)
update_give_center_to_lord = [
       # Jrider + TITLES v0.3.3 update title, fixed opcode error for spouse when you don't assign the center
       (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":lord_troop_id", ":lord_troop_faction"),
       # Update his wife/husband too if the lord has one
       (try_begin),
         (ge, ":lord_troop_id", 0), # v0.3.3 fix
         (troop_slot_ge, ":lord_troop_id", slot_troop_spouse, 0),
         (troop_get_slot, ":lord_spouse_troop_id", ":lord_troop_id", slot_troop_spouse),
         (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":lord_spouse_troop_id", ":lord_troop_faction"),
       (try_end),        
       # Jrider -      
]

update_change_player_relation_with_troop = [
        # Jrider + TITLES v0.3.2 update both player and troop titles
        (try_begin),
            (store_troop_faction, ":troop_faction", ":troop_no"),
            (eq, ":troop_faction", "$players_kingdom"),
            (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", "trp_player", "$players_kingdom"),
            (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":troop_no", "$players_kingdom"),
        (try_end),
        # Jrider -    
]

update_recruit_troop_as_companion = [
        # Jrider + TITLES v0.0 change companion title
        
        #(store_troop_faction, ":faction_no", ":troop_no"),
        #(call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":troop_no", ":faction_no"),
        
        # Jrider - 
]

update_player_join_faction = [
        # Jrider + TITLES v 0.3.1 change spouse title according to new faction
        (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":spouse", "$players_kingdom"),
        # Jrider - 
]
update_player_join_faction_2 = [
      #(call_script, "script_store_average_center_value_per_faction"),
      # Jrider + TITLES v 0.3.1 set player new title
      (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", "trp_player", "$players_kingdom"),
      # Jrider -
]

update_player_leave_faction = [
        # Jrider + TITLES v 0.3.1 change spouse title according to new faction
        (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":spouse", "fac_player_supporters_faction"),
        # Jrider -
]
update_player_leave_faction_2 = [
      # Jrider + TITLES v 0.3.1 set player new title
      (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", "trp_player", "fac_player_supporters_faction"),
      # Jrider -
]
update_activate_player_faction = [
    ## Jrider + TITLES v0.3.2 set new player faction liege title
    (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":liege", "fac_player_supporters_faction"),
    ## Jrider -
]


update_courtship_event_bride_marry_groom = [
        # Jrider + TITLES v0.0 change title of bride, according to player faction
        (call_script, "script_troop_set_title_according_to_faction", ":bride", "$players_kingdom"),
        # Jrider -
]


update_courtship_event_bride_marry_groom_2 = [
        # Jrider + TITLES v0.0 change title of groom and bride, according to player faction
        (call_script, "script_troop_set_title_according_to_faction", ":groom", ":groom_faction"),
        (call_script, "script_troop_set_title_according_to_faction", ":bride", ":groom_faction"),
        # Jrider -
]

update_troop_change_relation_with_troop = [
        # Jrider + TITLES v0.3.2 update title for relation suffix
        (try_begin),
            (store_troop_faction, ":troop1_faction", ":troop1"),
            (store_troop_faction, ":troop2_faction", ":troop2"),
            (faction_get_slot, ":troop1_faction_leader", ":troop1_faction", slot_faction_leader),
            (eq, ":troop1_faction", ":troop2_faction"),
            (eq, ":troop2", ":troop1_faction_leader"),
            (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":troop1", ":troop1_faction"),
        (try_end),
        # Jrider -  
  (try_begin),
    (eq, "$cheat_mode", 4),
]
#jrider Expanded nobility title system kit (v0.3.3)
#Zsar Fix the indictment death Spiral
indict_lord_for_treason = [
    (troop_set_slot, ":troop_no", slot_troop_controversy, 0),
]
indict_lord_for_treason_2 = [
      (party_set_faction, ":led_party", ":new_faction"),
      # addition to minimal: detaches lord's party from anything it is currently attached to, increases chance of flight
      (party_get_attached_to, ":anything", ":led_party"),
]
indict_lord_for_treason_3 = [
      #KAOS  (POLITICAL)
      (ge, ":anything", 0), # center, fight, whatever else one can be attached to; assumes "nothing" be '-1'
      (party_detach, ":led_party"),
      #KAOS  (POLITICAL)
]
#Zsar Fix the indictment death Spiral

#Lav Custom Lord Notes OSP
update_game_context_menu_get_buttons = [
     # Lav modifications start (custom lord notes)
       (context_menu_add_item, "@Add custom note", 3),
     # Lav modifications end (custom lord notes)
]

update_game_event_context_menu_button_clicked = [
# Lav modifications start (custom lord notes)
    (else_try),
      (eq, ":button_value", 3),
      (party_stack_get_troop_id, "$g_cln_troop", ":party_no", 0),
      (start_presentation, "prsnt_custom_lord_notes"),
# Lav modifications end (custom lord notes)
]

update_add_rumor_string_to_troop_notes = [
# Lav modifications start (custom lord notes)
          (neg|is_between, ":current_rumor_note", 3, 15), # Was 16 in original Native, thus using notes slot #15 as well. Now it will leave notes slot #15 for custom notes.
# Lav modifications end (custom lord notes)
]
update_add_rumor_string_to_troop_notes_2 = [
# Lav modifications start (custom lord notes)
          (neg|is_between, ":current_rumor_note", 3, 15), # Was 16 in original Native, thus using notes slot #15 as well. Now it will leave notes slot #15 for custom notes.
# Lav modifications end (custom lord notes)
]
#Lav Custom Lord Notes OSP

update_activate_player_faction = [
    (try_begin),
        (eq, "$background_answer_3", cb_king),
    (else_try),
         (call_script, "script_add_notification_menu", "mnu_notification_player_faction_active", 0, 0),
    (try_end),

]

update_game_get_troop_note = [
      #KAOS  (POLITICAL)
      (this_or_next|is_between, ":troop_no", active_npcs_begin, kingdom_ladies_end),
      #KAOS  (POLITICAL)
]

update_game_get_troop_note_family = [
        (this_or_next|troop_slot_eq, ":aristocrat", slot_troop_occupation, slto_kingdom_hero),
        (troop_slot_eq, ":aristocrat", slot_troop_occupation, slto_kingdom_lady),
]

update_npc_decision_checklist_male_guardian_assess_suitor = [
  (try_begin),
      (eq, ":suitor", "trp_player"),
      (eq, "$background_type", cb_king),
      (val_add, ":suitor_renown", 200),
  (else_try),
      (eq, ":suitor", "trp_player"),
      (eq, "$background_type", cb_prince),
      (val_add, ":suitor_renown", 100),
  (try_end),
]

from util_wrappers import *
from util_scripts import *

# Manualy add these to module_scripts search for "game_start"
# add the lines in at the start of the script block
scripts_directives = [
   [SD_OP_BLOCK_INSERT, "game_start", D_SEARCH_FROM_TOP | D_SEARCH_LINENUMBER | D_INSERT_BEFORE, 0, 0, update_game_start4], #ADD TO START.
   [SD_OP_BLOCK_INSERT, "game_start", D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_BEFORE, 0, 0, update_game_start], #ADD TO END.
   #[SD_OP_BLOCK_INSERT, "game_start", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(assign, "$g_there_is_no_avaliable_centers", 0),0,update_game_start2],
   [SD_OP_BLOCK_INSERT, "game_start", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (faction_set_note_available, "fac_neutral", 0),0,update_game_start3],

   #[SD_OP_BLOCK_REPLACE, "initialize_aristocracy", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE, (is_between, ":cur_troop", "trp_knight_6_1", "trp_kingdom_1_pretender"), 0 , [(is_between, ":cur_troop", "trp_knight_6_1", "trp_knight_1_1_wife")], 1],

   [SD_OP_BLOCK_INSERT, "give_center_to_lord", D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_BEFORE, 0, 0, update_give_center_to_lord], #ADD TO END.
   [SD_OP_BLOCK_INSERT, "change_player_relation_with_troop", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (assign, reg2, ":new_effective_relation"),0,update_change_player_relation_with_troop],
   [SD_OP_BLOCK_INSERT, "recruit_troop_as_companion", D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_BEFORE, 0, 0, update_recruit_troop_as_companion], #ADD TO END.
   [SD_OP_BLOCK_INSERT, "player_join_faction", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (troop_set_faction, ":spouse", "$players_kingdom"),0,update_player_join_faction],
   [SD_OP_BLOCK_INSERT, "player_join_faction", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (call_script, "script_update_all_notes"),0,update_player_join_faction_2],
   [SD_OP_BLOCK_INSERT, "player_leave_faction", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (troop_set_faction, ":spouse", "fac_player_supporters_faction"),0,update_player_leave_faction],
   [SD_OP_BLOCK_INSERT, "player_leave_faction", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (call_script, "script_update_all_notes"),0,update_player_leave_faction_2],
   [SD_OP_BLOCK_INSERT, "activate_player_faction", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (call_script, "script_update_all_notes"),0,update_activate_player_faction],

   [SD_OP_BLOCK_INSERT, "courtship_event_bride_marry_groom", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (troop_set_faction, ":bride", "$players_kingdom"),0,update_courtship_event_bride_marry_groom],
   [SD_OP_BLOCK_INSERT, "courtship_event_bride_marry_groom", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (troop_set_faction, ":bride", ":groom_faction"),0,update_courtship_event_bride_marry_groom_2],

   [SD_OP_BLOCK_REPLACE, "troop_change_relation_with_troop", D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE, (eq, "$cheat_mode", 4), 0 , update_troop_change_relation_with_troop],

   [SD_OP_BLOCK_INSERT, "indict_lord_for_treason", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),0, indict_lord_for_treason],

   [SD_OP_BLOCK_REPLACE, "indict_lord_for_treason", D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE, (remove_party, ":led_party"), 0 , indict_lord_for_treason_2],
   [SD_OP_BLOCK_REPLACE, "indict_lord_for_treason", D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE, (troop_set_slot, ":troop_no", slot_troop_leaded_party, -1), 0 , indict_lord_for_treason_3],


   [SD_OP_BLOCK_INSERT, "game_context_menu_get_buttons", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (context_menu_add_item, "@View notes", 2),0,update_game_context_menu_get_buttons],
   [SD_OP_BLOCK_INSERT, "game_event_context_menu_button_clicked", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (change_screen_notes, 1, ":troop_no"),0,update_game_event_context_menu_button_clicked],
   [SD_OP_BLOCK_INSERT, "add_rumor_string_to_troop_notes", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (assign, ":current_rumor_note", 3),0,update_add_rumor_string_to_troop_notes],
   [SD_OP_BLOCK_INSERT, "add_rumor_string_to_troop_notes", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (neg|is_between, ":current_rumor_note", 3, 16),0,update_add_rumor_string_to_troop_notes_2],


   #[SD_OP_BLOCK_REPLACE, "game_get_troop_note", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE, (this_or_next|is_between, ":troop_no", lords_begin, kingdom_ladies_end), 0 , update_game_get_troop_note],

   [SD_OP_BLOCK_REPLACE, "activate_player_faction", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE, (call_script, "script_add_notification_menu", "mnu_notification_player_faction_active", 0, 0), 0 , update_activate_player_faction],


   #[SD_OP_BLOCK_INSERT, "game_get_troop_note", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (try_for_range, ":aristocrat", active_npcs_begin, kingdom_ladies_end),0,update_game_get_troop_note_family],
   #[SD_OP_BLOCK_INSERT, "game_get_troop_note", D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (try_for_range, ":aristocrat", active_npcs_begin, kingdom_ladies_end),0,update_game_get_troop_note_family],

   [SD_OP_BLOCK_INSERT, "npc_decision_checklist_male_guardian_assess_suitor", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (troop_get_slot, ":suitor_renown", ":suitor", slot_troop_renown),0, update_npc_decision_checklist_male_guardian_assess_suitor],

]


# the following is a generic function expected by modmerger
# If not defined, it will only do the basic merging of adding the scripts in "scripts" to the orignal "scripts" in module_scripts.py
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1] # this is the ORIGINAL scripts from module_scripts.py

        # START do your own stuff to do merging

        # modify existing scripts according to script_directives above
        process_script_directives(orig_scripts, scripts_directives)

        add_objects(orig_scripts, scripts) # add new scripts, by default, scripts with same name will be replaced

        # END do your own stuff

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
	