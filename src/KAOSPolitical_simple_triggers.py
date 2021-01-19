# POLITICAL (1.2) by Lazeras
# Released 1 December 2014
from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
from module_constants import *
from module_game_menus import *

# Manualy all lines under the `simple_triggers` into the bottom of the module_simple_triggers at the bottom of the file
simple_triggers=[
	#KAOS  (POLITICAL)
	#########################################################################################################################
	#Start Faction Rebellion triggers																						#
	#########################################################################################################################  
	#
	# Simple trigger to check the rebel faction and initiate rebellion if 
	# the required paramaters of date and rebellion chance 
	# NOTE: maybe change it to once a week. 
	#
	(24,
	[   
		(assign, ":random_chance", 0),
		(try_for_range, ":faction_id", rebel_factions_begin, rebel_factions_end),
		    (faction_slot_eq, ":faction_id", slot_faction_state, sfs_inactive),
		    (neg|faction_slot_eq, ":faction_id", slot_faction_state, sfs_defeated),
	        (faction_get_slot,  ":rebellion_date", ":faction_id", slot_rebellion_date),
	        (store_current_day, ":cur_day"),

 
	        (try_begin),
	            (eq, ":faction_id", "fac_kingdom_7"),
	            (assign, ":rebel_lord", "trp_kingdom_1_pretender"),
	            (assign, ":orig_faction", "fac_kingdom_1"),
		     	(try_begin),
		      		(eq, "$kaos_rebellion_home", 1),
		      		(assign, ":rebel_center", "p_town_4"), #SUNO
		      		(assign, ":rebel_claimed", "p_town_6"),#Praven
		     	(else_try),
		      		(assign, ":rebel_center", "p_town_7"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_town_4"),#Suno
		 		(try_end),
	        (else_try),
	            (eq, ":faction_id", "fac_kingdom_8"),
	            (assign, ":rebel_lord", "trp_kingdom_2_pretender"),
	            (assign, ":orig_faction", "fac_kingdom_2"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_13"),#Rivacheg
					(assign, ":rebel_claimed", "p_town_8"),#Reyvadin
				(else_try),
					(assign, ":rebel_center", "p_town_11"),#Curaw
					(assign, ":rebel_claimed", "p_town_13"),#Rivacheg
				(try_end),
	        (else_try),
	            (eq, ":faction_id", "fac_kingdom_9"),
	            (assign, ":rebel_lord", "trp_kingdom_3_pretender"),
	            (assign, ":orig_faction", "fac_kingdom_3"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_17"), #Ichamur
					(assign, ":rebel_claimed", "p_town_10"),#Tulga
				(else_try),
					(assign, ":rebel_center", "p_town_14"),#Halmar
					(assign, ":rebel_claimed", "p_town_17"),#Ichamur
				(try_end),
	        (else_try),
	            (eq, ":faction_id", "fac_kingdom_10"),
	            (assign, ":rebel_lord", "trp_kingdom_4_pretender"),
	            (assign, ":orig_faction", "fac_kingdom_4"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_2"), #Tihr
					(assign, ":rebel_claimed", "p_town_1"),#Sargoth
				(else_try),
					(assign, ":rebel_center", "p_town_12"),#Wercheg
					(assign, ":rebel_claimed", "p_town_2"),#Tihr
				(try_end),
	        (else_try),
	            (eq, ":faction_id", "fac_kingdom_11"),
	            (assign, ":rebel_lord", "trp_kingdom_5_pretender"),
	            (assign, ":orig_faction", "fac_kingdom_5"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_15"), #Yalen
					(assign, ":rebel_claimed", "p_town_5"),#Jelkala
				(else_try),
					(assign, ":rebel_center", "p_town_3"),#Veluca
					(assign, ":rebel_claimed", "p_town_15"),#Yalen
				(try_end),
	        (else_try),
	            (eq, ":faction_id", "fac_kingdom_12"),
	            (assign, ":rebel_lord", "trp_kingdom_6_pretender"),
	            (assign, ":orig_faction", "fac_kingdom_6"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_20"), #Durquba
					(assign, ":rebel_claimed", "p_town_19"),#Shariz
				(else_try),
					(assign, ":rebel_center", "p_town_21"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_20"),#Durquba
				(try_end),
	        (try_end),

	        (try_begin),
	        	(eq, "$background_answer_3", cb_king),
	            (assign, ":orig_faction", "fac_player_supporters_faction"),
	        (try_end),


	        #Check that the current date is greater than the minimum day for rebellion to start
	        (ge, ":cur_day", ":rebellion_date"), 
	        (try_begin),
	        	(neg|main_party_has_troop, ":rebel_lord"), 
		        (call_script, "script_rebelion_assesment", ":orig_faction"),
		        (faction_get_slot,  ":rebellion_chance", ":orig_faction", slot_faction_has_rebellion_chance),
		        #Modify the random chance generation so that low fracturing makes it harder for a rebellion
				(store_sub, ":lower_limit", 9, ":rebellion_chance"),
				(store_random_in_range, ":random_chance", ":lower_limit", 9),     
		        (try_begin),
		            #Could change this conditional check to ge for a easier activation of rebellion
		            (gt, ":rebellion_chance", ":random_chance"),
		            (call_script, "script_rebellion_faction_call", ":orig_faction", ":rebel_center", ":rebel_lord", ":faction_id", ":rebel_claimed"),
		        (try_end),
	        (try_end),
	        #####################  debugging messages ################################
	        (try_begin),    
	          (eq, "$kaos_debug_mode", 1),  
	          (str_store_faction_name, s52, ":orig_faction"),
	          (assign, reg53, ":random_chance"),
	          (assign, reg54, ":rebellion_chance"),
	          (faction_get_slot, ":leader_no", ":faction_id", slot_faction_leader),
	          (str_store_troop_name, s55, ":leader_no"),
	          (display_log_message, "@{!} {s52} has a rebelion chance of {reg54} must be gt than {reg53} for rebel leader {s55}", 0xFF0000),
	        (try_end),    
	        #####################  debugging messages ################################
		(try_end),
	]
	),
	
	#########################################################################################################################
	#Faction Rebellion trigger for multiple claimants in the one center 													#
	#########################################################################################################################  
	#
	# Simple trigger for multiple claimants in the one center 
	# NOTE: maybe change it to once a week. 
	#
	(72,
	[   
		(store_current_day, ":cur_day"),
		(assign, ":main_faction", 0),
		(assign, ":main_center", 0),
		(assign, ":sub_faction", 0),
		(assign, ":sub_center", 0),

		(assign, ":bonus", 3),
		(try_for_range, ":main_npc", pretenders_begin, pretenders_end),
            (troop_get_slot, ":main_center", ":main_npc", slot_troop_cur_center),
			(str_store_faction_name, ":main_faction", ":main_npc"),
			(try_for_range, ":sub_npc", pretenders_begin, pretenders_end),
	            (troop_get_slot, ":sub_center", ":sub_npc", slot_troop_cur_center),   
				(str_store_faction_name, ":sub_faction", ":sub_npc"),
	            (neq, ":main_npc", ":sub_npc"), 
	            (eq, ":main_center", ":sub_center"),
	            (try_begin),
				    (faction_slot_eq, ":main_faction", slot_faction_state, sfs_inactive),
				    (neg|faction_slot_eq, ":main_faction", slot_faction_state, sfs_defeated),
			        (faction_get_slot,  ":main_date", ":main_faction", slot_rebellion_date),
			        #Check that the current date is greater than the minimum day for rebellion to start
			        (ge, ":cur_day", ":main_date"), 
		        	(neg|main_party_has_troop, ":main_npc"), 
			        (call_script, "script_rebelion_assesment", ":main_faction"),
			        (faction_get_slot,  ":main_chance", ":main_faction", slot_faction_has_rebellion_chance),
			        #Modify the random chance generation so that low fracturing makes it harder for a rebellion
			        (val_add, ":main_chance", ":bonus"),
					(store_sub, ":lower_limit", 9, ":main_chance"),   
					(store_random_in_range, ":main_random_chance", ":lower_limit", 9), 
			        (try_begin),
			            #Could change this conditional check to ge for a easier activation of rebellion
			            (gt, ":main_chance", ":main_random_chance"),
			            (call_script, "script_rebellion_faction_call", ":main_faction"),
			        (try_end),
	            (try_end),
	        #####################  debugging messages ################################
	        (try_begin),    
	          (eq, "$kaos_debug_mode", 1),  
	          (str_store_faction_name, s52, ":main_faction"),
	          (assign, reg53, ":main_random_chance"),
	          (assign, reg54, ":main_chance"),
	          (faction_get_slot, ":main_leader_no", ":main_faction", slot_faction_leader),
	          (str_store_troop_name, s55, ":main_leader_no"),
	          (display_log_message, "@{!} {s52} has a rebelion chance of {reg54} must be gt than {reg53} for rebel leader {s55}", 0xFF0000),
	        (try_end),    
	        #####################  debugging messages ################################
	            (try_begin),
				    (faction_slot_eq, ":sub_faction", slot_faction_state, sfs_inactive),
				    (neg|faction_slot_eq, ":sub_faction", slot_faction_state, sfs_defeated),
			        (faction_get_slot,  ":sub_date", ":sub_faction", slot_rebellion_date),
			        #Check that the current date is greater than the minimum day for rebellion to start
			        (ge, ":cur_day", ":sub_date"), 
		        	(neg|main_party_has_troop, ":sub_npc"), 
			        (call_script, "script_rebelion_assesment", ":sub_faction"),
			        (faction_get_slot,  ":sub_chance", ":sub_faction", slot_faction_has_rebellion_chance),
			        #Modify the random chance generation so that low fracturing makes it harder for a rebellion
			        (val_add, ":sub_chance", ":bonus"),
					(store_sub, ":lower_limit", 9, ":sub_chance"),   
					(store_random_in_range, ":sub_random_chance", ":lower_limit", 9), 
			        (try_begin),
			            #Could change this conditional check to ge for a easier activation of rebellion
			            (gt, ":sub_chance", ":sub_random_chance"),
			            (call_script, "script_rebellion_faction_call", ":sub_faction"),
			        (try_end),
	            (try_end),
	        #####################  debugging messages ################################
	        (try_begin),    
	          (eq, "$kaos_debug_mode", 1),  
	          (str_store_faction_name, s52, ":sub_faction"),
	          (assign, reg53, ":sub_random_chance"),
	          (assign, reg54, ":sub_chance"),
	          (faction_get_slot, ":sub_leader_no", ":sub_faction", slot_faction_leader),
	          (str_store_troop_name, s55, ":sub_leader_no"),
	          (display_log_message, "@{!} {s52} has a rebelion chance of {reg54} must be gt than {reg53} for rebel leader {s55}", 0xFF0000),
	        (try_end),    
	        #####################  debugging messages ################################
			(try_end),    
		(try_end),
	]
	),	

	#########################################################################################################################
	#Start Faction Civil war triggers																						#
	#########################################################################################################################  
	#
	# Simple trigger to check for civil war paramaters
	# NOTE: maybe change it to once a week. 
	#
	(24,
	[   
	  (try_begin),
		  (eq, "$kaos_civil_war", 1),
	      (try_for_range, ":faction_id", kingdoms_begin, "fac_kingdom_7"),
		      (faction_slot_eq, ":faction_id", slot_faction_state, sfs_active),
		      (neg|faction_slot_eq, ":faction_id", slot_faction_state, sfs_defeated),
		      (assign, ":total_lords", 0),
		      (assign, ":total_disgruntled_lords", 0),
			  (call_script, "script_evaluate_realm_stability", ":faction_id"),
		        #####################  debugging messages ################################
		        (try_begin),    
		          (eq, "$kaos_debug_mode", 1),  
		          (str_store_faction_name, s52, ":faction_id"),
		          (assign, reg53, ":total_lords"),
		          (assign, reg54, ":total_disgruntled_lords"),
		          (faction_get_slot, ":liege", ":faction_id", slot_faction_leader),
		          (str_store_troop_name, s55, ":liege"),
		          (display_log_message, "@{!} {s52} leader {s55} tottal lords {reg53} total_disgruntled_lords {reg54}", 0xFF0000),
		        (try_end),    
		        #####################  debugging messages ################################  
		      (try_begin),
		          (ge, reg0, 40),
		          (call_script, "script_rebellion_faction_civil_war", ":faction_id"),
		      (try_end),
	      (try_end),
	  (try_end),
	]
	),	

	# Rename Rebell factions to original faction name if the original faction is defeated
	(24,
		[   
	        
			(try_for_range, ":faction_id", rebel_factions_begin, rebel_factions_end),
			    #(faction_slot_eq, ":faction_id", slot_faction_state, sfs_inactive),
			    (faction_slot_eq, ":faction_id", slot_faction_state, sfs_defeated),
		        (try_begin),
		        	(eq, ":faction_id", "fac_kingdom_1"),
				    (faction_slot_eq, "fac_kingdom_7", slot_faction_state, sfs_active),
				    (neg|faction_slot_eq, "fac_kingdom_7", slot_faction_state, sfs_defeated),
				    (str_store_string, s1, "str_kaos_swadia_king"),
				    (faction_set_name, "fac_kingdom_7", s1),
		        (else_try),
		        	(eq, ":faction_id", "fac_kingdom_2"),
				    (faction_slot_eq, "fac_kingdom_8", slot_faction_state, sfs_active),
				    (neg|faction_slot_eq, "fac_kingdom_8", slot_faction_state, sfs_defeated),
				    (str_store_string, s1, "str_kaos_Vaegirs_king"),
				    (faction_set_name, "fac_kingdom_8", s1),
		        (else_try),
		        	(eq, ":faction_id", "fac_kingdom_3"),
				    (faction_slot_eq, "fac_kingdom_9", slot_faction_state, sfs_active),
				    (neg|faction_slot_eq, "fac_kingdom_9", slot_faction_state, sfs_defeated),
				    (str_store_string, s1, "str_kaos_Khergit_king"),
				    (faction_set_name, "fac_kingdom_9", s1),
		        (else_try),
		        	(eq, ":faction_id", "fac_kingdom_4"),
				    (faction_slot_eq, "fac_kingdom_10", slot_faction_state, sfs_active),
				    (neg|faction_slot_eq, "fac_kingdom_10", slot_faction_state, sfs_defeated),
				    (str_store_string, s1, "str_kaos_Nords_king"),
				    (faction_set_name, "fac_kingdom_10", s1),
		        (else_try),
		        	(eq, ":faction_id", "fac_kingdom_5"),
				    (faction_slot_eq, "fac_kingdom_11", slot_faction_state, sfs_active),
				    (neg|faction_slot_eq, "fac_kingdom_11", slot_faction_state, sfs_defeated),
				    (str_store_string, s1, "str_kaos_Rhodoks_king"),
				    (faction_set_name, "fac_kingdom_11", s1),
		        (else_try),
		        	(eq, ":faction_id", "fac_kingdom_6"),
				    (faction_slot_eq, "fac_kingdom_12", slot_faction_state, sfs_active),
				    (neg|faction_slot_eq, "fac_kingdom_12", slot_faction_state, sfs_defeated),
				    (str_store_string, s1, "str_kaos_Sarranid_king"),
				    (faction_set_name, "fac_kingdom_12", s1),
		        (try_end),

			(try_end),
		]
	),	

#rubik Source code of Restoration
# restoration begin
  # Note: make sure there is a comma in the entry behind this one
  (24,
    [
	  (try_begin),
		  (eq, "$kaos_restore", 1),
		  (assign, ":continue", 1),
		  (try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
	        (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
	        (troop_get_slot, ":original_faction", ":cur_troop", slot_troop_original_faction),
	        (neg|faction_slot_eq, ":original_faction", slot_faction_state, sfs_active),
	        (try_begin),
            	(eq,"$background_answer_3",cb_king),
			     (try_begin),
			          (eq, ":original_faction", "fac_kingdom_1"),
			          (eq, "$kaos_kings_kingdom", 1),
			  		  (assign, ":continue", 0),
			     (else_try),
			          (eq, ":original_faction", "fac_kingdom_2"),
			          (eq, "$kaos_kings_kingdom", 2),
			  		  (assign, ":continue", 0),
			     (else_try),
			          (eq, ":original_faction", "fac_kingdom_3"),
			          (eq, "$kaos_kings_kingdom", 3),
			  		  (assign, ":continue", 0),
			     (else_try),
			          (eq, ":original_faction", "fac_kingdom_4"),
			          (eq, "$kaos_kings_kingdom", 4),
			  		  (assign, ":continue", 0),
			     (else_try),
			          (eq, ":original_faction", "fac_kingdom_5"),
			          (eq, "$kaos_kings_kingdom", 5),
			  		  (assign, ":continue", 0),
			     (else_try),
			          (eq, ":original_faction", "fac_kingdom_6"),
			          (eq, "$kaos_kings_kingdom", 6),
			  		  (assign, ":continue", 0),
			     (try_end),
	        (else_try),
	        	(is_between, ":original_faction", kingdoms_begin, "fac_kingdom_7"),
	        	(assign, ":continue", 1),
	        (try_end),

			(try_begin),
				(eq, ":continue", 1),
		        (store_troop_faction, ":faction_no", ":cur_troop"),
		        (neq, ":faction_no", ":original_faction"),
		       
		        (assign, ":num_walled_centers", 0),
		        (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
		          (party_slot_eq, ":walled_center", slot_town_lord, ":cur_troop"),
		          (val_add, ":num_walled_centers", 1),
		        (try_end),
		        (gt, ":num_walled_centers", 0), ## has a walled center
		       
		        (store_sub, ":original_king", ":original_faction", fac_kingdom_1),
		        (val_add, ":original_king", "trp_kingdom_1_lord"),
		        (faction_set_slot, ":original_faction", slot_faction_leader, ":original_king"),
		       
		        (call_script, "script_change_troop_faction", ":cur_troop", ":original_faction"),
		        (try_for_range, ":cur_troop_2", active_npcs_begin, active_npcs_end),
		          (troop_slot_eq, ":cur_troop_2", slot_troop_occupation, slto_kingdom_hero),
		          (neg|is_between, ":cur_troop_2", pretenders_begin, pretenders_end),
		          (neq, ":cur_troop_2", ":cur_troop"),
		          (troop_get_slot, ":original_faction_2", ":cur_troop_2", slot_troop_original_faction),
		          (store_troop_faction, ":faction_no_2", ":cur_troop_2"),
		          (eq, ":original_faction_2", ":original_faction"),
		          (neq, ":faction_no_2", ":original_faction"),
		          (troop_set_slot, ":cur_troop_2", slot_troop_change_to_faction, ":original_faction"),
		        (try_end),
		        (call_script, "script_add_notification_menu", "mnu_notification_kingdom_restoration", ":cur_troop", ":faction_no"),
		      (try_end),
			(try_end),



	  (try_end),
    ]),
  ## restoration end
#rubik Source code of Restoration


]



from util_common import *
def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "simple_triggers"
		orig_simple_triggers = var_set[var_name_1]
		
		add_objects(orig_simple_triggers, simple_triggers, False)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)