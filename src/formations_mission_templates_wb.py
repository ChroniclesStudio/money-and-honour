# Formations for Warband by Motomataru
# rel. 06/08/11

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *

# Formations triggers v3 by motomataru, Warband port
# Global variables	*_formation_type holds type of formation: see "Formation modes" in module_constants
#					*_formation_move_order hold the current move order for the formation
#					*_space hold the multiplier of extra space ordered into formation by the player

formations_triggers = [
	(ti_before_mission_start, 0, 0, [], [
		(assign, "$gk_order", 0),
		(assign, "$gk_order_hold_over_there", 0),
		(assign, "$autorotate_at_player", formation_autorotate_at_player),
		(assign, "$infantry_formation_type", formation_default),	#type set by first call; depends on faction
		(assign, "$archer_formation_type", formation_default),
		(assign, "$cavalry_formation_type", formation_wedge),
		(assign, "$infantry_space", formation_start_spread_out),	#give a little extra space for ease of forming up
		(assign, "$archer_space", formation_start_spread_out),
		(assign, "$cavalry_space", 0),
		(assign, "$fclock", 1)
	]),

# Start troops in formation
	(0, formation_delay_for_spawn, ti_once, [], [
		(get_player_agent_no, "$fplayer_agent_no"),
		(agent_get_team, "$fplayer_team_no", "$fplayer_agent_no"),
		(call_script, "script_store_battlegroup_data"),
		
		#get team fixed data
		(assign, ":team0_avg_faction", 0),
		(assign, ":team1_avg_faction", 0),
		(assign, ":team2_avg_faction", 0),
		(assign, ":team3_avg_faction", 0),
		(try_for_agents, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(agent_get_team, ":cur_team", ":cur_agent"),
			(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			(store_troop_faction, ":cur_faction", ":cur_troop"),
			(try_begin),
				(eq, ":cur_team", 0),
				(val_add, ":team0_avg_faction", ":cur_faction"),
			(else_try),
				(eq, ":cur_team", 1),
				(val_add, ":team1_avg_faction", ":cur_faction"),
			(else_try),
				(eq, ":cur_team", 2),
				(val_add, ":team2_avg_faction", ":cur_faction"),
			(else_try),
				(eq, ":cur_team", 3),
				(val_add, ":team3_avg_faction", ":cur_faction"),
			(try_end),
		(try_end),
		(try_begin),
			(gt, "$team0_size", 0),
			(team_get_leader, ":fleader", 0),
			(try_begin),
				(ge, ":fleader", 0),
				(agent_get_troop_id, ":fleader_troop", ":fleader"),
				(store_troop_faction, "$team0_faction", ":fleader_troop"),
			(else_try),
				(store_mul, "$team0_faction", ":team0_avg_faction", 10),
				(val_div, "$team0_faction", "$team0_size"),
				(val_add, "$team0_faction", 5),
				(val_div, "$team0_faction", 10),
			(try_end),
		(try_end),
		(try_begin),
			(gt, "$team1_size", 0),
			(team_get_leader, ":fleader", 1),
			(try_begin),
				(ge, ":fleader", 0),
				(agent_get_troop_id, ":fleader_troop", ":fleader"),
				(store_troop_faction, "$team1_faction", ":fleader_troop"),
			(else_try),
				(store_mul, "$team1_faction", ":team1_avg_faction", 10),
				(val_div, "$team1_faction", "$team1_size"),
				(val_add, "$team1_faction", 5),
				(val_div, "$team1_faction", 10),
			(try_end),
		(try_end),
		(try_begin),
			(gt, "$team2_size", 0),
			(team_get_leader, ":fleader", 2),
			(try_begin),
				(ge, ":fleader", 0),
				(agent_get_troop_id, ":fleader_troop", ":fleader"),
				(store_troop_faction, "$team2_faction", ":fleader_troop"),
			(else_try),
				(store_mul, "$team2_faction", ":team2_avg_faction", 10),
				(val_div, "$team2_faction", "$team2_size"),
				(val_add, "$team2_faction", 5),
				(val_div, "$team2_faction", 10),
			(try_end),
		(try_end),
		(try_begin),
			(gt, "$team3_size", 0),
			(team_get_leader, ":fleader", 3),
			(try_begin),
				(ge, ":fleader", 0),
				(agent_get_troop_id, ":fleader_troop", ":fleader"),
				(store_troop_faction, "$team3_faction", ":fleader_troop"),
			(else_try),
				(store_mul, "$team3_faction", ":team3_avg_faction", 10),
				(val_div, "$team3_faction", "$team3_size"),
				(val_add, "$team3_faction", 5),
				(val_div, "$team3_faction", 10),
			(try_end),
		(try_end),
		
		(display_message, "@Forming ranks."),
		#keep cavalry on the map
		(call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_cavalry),
		(val_mul, reg0, 2),
		(convert_to_fixed_point, reg0),
		(store_sqrt, ":depth_cavalry", reg0),
		(convert_from_fixed_point, ":depth_cavalry"),
		(val_sub, ":depth_cavalry", 1),
		(store_mul, reg0, "$cavalry_space", 50),
		(val_add, reg0, 250),
		(val_mul, ":depth_cavalry", reg0),
		(store_mul, reg0, "$infantry_space", 50),
		(val_add, reg0, formation_minimum_spacing),
		(val_mul, reg0, 2),
		(val_sub, ":depth_cavalry", reg0),
		(try_begin),
			(gt, ":depth_cavalry", 0),
			(agent_get_position, pos49, "$fplayer_agent_no"),
			(copy_position, pos2, pos49),
			(call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
			(call_script, "script_point_y_toward_position", pos2, pos60),
			(position_move_y, pos2, ":depth_cavalry"),
			(agent_set_position, "$fplayer_agent_no", pos2),	#fake out script_cf_formation
		(try_end),

		(call_script, "script_get_default_formation", "$fplayer_team_no"),
		(call_script, "script_player_attempt_formation", grc_infantry, reg0),
		(call_script, "script_player_attempt_formation", grc_cavalry, formation_wedge),
		(call_script, "script_player_attempt_formation", grc_archers, formation_default),
		(try_begin),
			(gt, ":depth_cavalry", 0),
			(agent_set_position, "$fplayer_agent_no", pos49),
		(try_end),

		(set_show_messages, 0),
		(try_for_range, reg0, 3, 9),
			(team_give_order, "$fplayer_team_no", reg0, mordr_hold),
		(try_end),

		#init troops for when formation ends
		(try_for_range, reg0, 0, "$infantry_space"),
			(team_give_order, "$fplayer_team_no", grc_infantry, mordr_spread_out),
		(try_end),
		(try_for_range, reg0, 0, "$archer_space"),
			(team_give_order, "$fplayer_team_no", grc_archers, mordr_spread_out),
		(try_end),
		(try_for_range, reg0, 0, "$cavalry_space"),
			(team_give_order, "$fplayer_team_no", grc_cavalry, mordr_spread_out),
		(try_end),
		(set_show_messages, 1),
	]),

#form ranks command
	(0, 0, 1, [(key_clicked, key_for_ranks)], [
		(assign, "$fclock", 1),
		(call_script, "script_player_attempt_formation", grc_infantry, formation_ranks),
		(call_script, "script_player_attempt_formation", grc_archers, formation_ranks)
	]),

#form shield wall command
	(0, 0, 1, [(key_clicked, key_for_shieldwall)], [
		(assign, "$fclock", 1),
		(call_script, "script_player_attempt_formation", grc_infantry, formation_shield)
	]),

#form wedge command
	(0, 0, 1, [(key_clicked, key_for_wedge)], [
		(assign, "$fclock", 1),
		(call_script, "script_player_attempt_formation", grc_infantry, formation_wedge),
		(call_script, "script_player_attempt_formation", grc_cavalry, formation_wedge)
	]),

#form square command
	(0, 0, 1, [(key_clicked, key_for_square)], [
		(assign, "$fclock", 1),
		(call_script, "script_player_attempt_formation", grc_infantry, formation_square)
	]),

#end formation command
	(0, 0, 1, [(key_clicked, key_for_undo)], [
		(assign, "$fclock", 1),
		(call_script, "script_player_order_formations", mordr_charge)
	]),

	(0, .3, 0, [(game_key_clicked, gk_order_1)], [
		(eq, "$gk_order", gk_order_1),	#next trigger set MOVE menu?
		(game_key_is_down, gk_order_1),	#BUT player is holding down key?
		(assign, "$gk_order_hold_over_there", 1),
		(assign, "$gk_order", 0),
	]),

	(0, 0, 0, [(game_key_clicked, gk_order_1)], [
		(try_begin),
			(eq, "$gk_order", 0),
			(assign, "$gk_order", gk_order_1),
		(else_try),
			(eq, "$gk_order", gk_order_1),	#HOLD		
			(assign, "$fclock", 1),
			(call_script, "script_player_order_formations", mordr_hold),
			(assign, "$gk_order", 0),
		(else_try),
			(eq, "$gk_order", gk_order_2),	#ADVANCE
			(assign, "$fclock", 1),
			(call_script, "script_player_order_formations", mordr_advance),
			(assign, "$gk_order", 0),
		(else_try),
			(eq, "$gk_order", gk_order_3),	#HOLD FIRE
			(assign, "$gk_order", 0),
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_2)], [
		(try_begin),
			(eq, "$gk_order", 0),
			(assign, "$gk_order", gk_order_2),
		(else_try),
			(eq, "$gk_order", gk_order_1),	#FOLLOW
			(assign, "$fclock", 1),
			(call_script, "script_player_order_formations", mordr_follow),
			(assign, "$gk_order", 0),
		(else_try),
			(eq, "$gk_order", gk_order_2),	#FALL BACK
			(assign, "$fclock", 1),
			(call_script, "script_player_order_formations", mordr_fall_back),
			(assign, "$gk_order", 0),
		(else_try),
			(eq, "$gk_order", gk_order_3),	#FIRE AT WILL
			(assign, "$gk_order", 0),
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_3)], [
		(try_begin),
			(eq, "$gk_order", 0),
			(assign, "$gk_order", gk_order_3),
		(else_try),
			(eq, "$gk_order", gk_order_1),	#CHARGE
			(assign, "$fclock", 1),
			(call_script, "script_player_order_formations", mordr_charge),
			(assign, "$gk_order", 0),
		(else_try),
			(eq, "$gk_order", gk_order_2),	#SPREAD OUT
			(assign, "$fclock", 1),
			(call_script, "script_player_order_formations", mordr_spread_out),
			(assign, "$gk_order", 0),
		(else_try),
			(eq, "$gk_order", gk_order_3),	#BLUNT WEAPONS
			(assign, "$gk_order", 0),
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_4)], [
		(try_begin),
			(eq, "$gk_order", gk_order_1),	#STAND GROUND
			(assign, "$fclock", 1),
			(call_script, "script_player_order_formations", mordr_stand_ground),			
			(assign, "$gk_order", 0),
		(else_try),
			(eq, "$gk_order", gk_order_2),	#STAND CLOSER
			(assign, "$fclock", 1),
			(call_script, "script_player_order_formations", mordr_stand_closer),
			(assign, "$gk_order", 0),
		(else_try),
			(eq, "$gk_order", gk_order_3),	#ANY WEAPON
			(assign, "$gk_order", 0),
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_5)], [
		(try_begin),
			(eq, "$gk_order", gk_order_1),	#RETREAT
			(assign, "$fclock", 1),
			(call_script, "script_player_order_formations", mordr_retreat),
			(assign, "$gk_order", 0),
		(else_try),
			(eq, "$gk_order", gk_order_2),	#MOUNT
			(assign, "$gk_order", 0),
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_6)], [
		(eq, "$gk_order", gk_order_2),	#DISMOUNT
		(assign, "$fclock", 1),
		(call_script, "script_player_order_formations", mordr_dismount),
		(assign, "$gk_order", 0),
	]),

	(0, 0, 0, [
		(this_or_next|game_key_clicked, gk_group0_hear),
		(this_or_next|game_key_clicked, gk_group1_hear),
		(this_or_next|game_key_clicked, gk_group2_hear),
		(this_or_next|game_key_clicked, gk_group3_hear),
		(this_or_next|game_key_clicked, gk_group4_hear),
		(this_or_next|game_key_clicked, gk_group5_hear),
		(this_or_next|game_key_clicked, gk_group6_hear),
		(this_or_next|game_key_clicked, gk_group7_hear),
		(this_or_next|game_key_clicked, gk_group8_hear),
		(this_or_next|game_key_clicked, gk_reverse_order_group),	#shows up as "unknown 6" on Native screen
		(this_or_next|game_key_clicked, gk_everyone_around_hear),
		(this_or_next|game_key_clicked, gk_everyone_hear),
		(key_clicked, key_escape)	#doesn't work because ESC is omitted during command selection
	], [
		(assign, "$gk_order", 0)
	]),

#implement HOLD OVER THERE when player lets go of key
	(.5, 0, 0, [(eq, "$gk_order_hold_over_there", 1),(neg|game_key_is_down, gk_order_1)], [
		(set_fixed_point_multiplier, 100),
		(assign, "$fclock", 1),
		(call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
		(assign, ":num_bgroups", 0),
		(try_for_range, ":battle_group", 0, 9),
			(class_is_listening_order, "$fplayer_team_no", ":battle_group"),
			(call_script, "script_battlegroup_get_size", "$fplayer_team_no", ":battle_group"),
			(gt, reg0, 0),
			(val_add, ":num_bgroups", 1),
		(try_end),		
		(agent_get_position, pos49, "$fplayer_agent_no"),		
		(try_begin),
			(neq, "$infantry_formation_type", formation_none),
			(class_is_listening_order, "$fplayer_team_no", grc_infantry),
			(team_get_order_position, pos2, "$fplayer_team_no", grc_infantry),
			(call_script, "script_point_y_toward_position", pos2, pos60),
			(try_begin),
				(gt, ":num_bgroups", 1),
				(agent_set_position, "$fplayer_agent_no", pos2),	#fake out script_cf_formation
				(try_begin),	#ignore script failure
					(call_script, "script_cf_formation", "$fplayer_team_no", grc_infantry, "$infantry_space", "$infantry_formation_type"),
				(try_end),
			(else_try),
				(call_script, "script_set_formation_position", "$fplayer_team_no", grc_infantry, pos2),
				(call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_infantry),
				(assign, ":troop_count", reg0),
				(call_script, "script_get_centering_amount", "$infantry_formation_type", ":troop_count", "$infantry_space"),
				(position_move_x, pos2, reg0),
				(copy_position, pos1, pos2),
				(call_script, "script_form_infantry", "$fplayer_team_no", "$fplayer_agent_no", "$infantry_space", "$infantry_formation_type"),		
			(try_end),
			(assign, "$infantry_formation_move_order", mordr_hold),
		(try_end),
		(try_begin),
			(neq, "$cavalry_formation_type", formation_none),
			(class_is_listening_order, "$fplayer_team_no", grc_cavalry),
			(team_get_order_position, pos2, "$fplayer_team_no", grc_cavalry),
			(call_script, "script_point_y_toward_position", pos2, pos60),
			(try_begin),
				(gt, ":num_bgroups", 1),
				(agent_set_position, "$fplayer_agent_no", pos2),	#fake out script_cf_formation
				(try_begin),	#ignore script failure
					(call_script, "script_cf_formation", "$fplayer_team_no", grc_cavalry, "$cavalry_space", "$cavalry_formation_type"),
				(try_end),
			(else_try),
				(call_script, "script_set_formation_position", "$fplayer_team_no", grc_cavalry, pos2),
				# (call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_cavalry),
				# (assign, ":troop_count", reg0),
				# (call_script, "script_get_centering_amount", "$cavalry_formation_type", ":troop_count", "$cavalry_space"),
				# (position_move_x, pos2, reg0),
				(copy_position, pos1, pos2),
				(call_script, "script_form_cavalry", "$fplayer_team_no", "$fplayer_agent_no", "$cavalry_space"),		
			(try_end),
			(assign, "$cavalry_formation_move_order", mordr_hold),
		(try_end),
		(try_begin),
			(neq, "$archer_formation_type", formation_none),
			(class_is_listening_order, "$fplayer_team_no", grc_archers),
			(team_get_order_position, pos2, "$fplayer_team_no", grc_archers),
			(call_script, "script_point_y_toward_position", pos2, pos60),
			(try_begin),
				(gt, ":num_bgroups", 1),
				(agent_set_position, "$fplayer_agent_no", pos2),	#fake out script_cf_formation
				(try_begin),	#ignore script failure
					(call_script, "script_cf_formation", "$fplayer_team_no", grc_archers, "$archer_space", "$archer_formation_type"),
				(try_end),
			(else_try),
				(call_script, "script_set_formation_position", "$fplayer_team_no", grc_archers, pos2),
				(call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_archers),
				(assign, ":troop_count", reg0),
				(call_script, "script_get_centering_amount", formation_default, ":troop_count", "$archer_space"),
				(val_mul, reg0, -1),
				(position_move_x, pos2, reg0),
				(copy_position, pos1, pos2),
				(call_script, "script_form_archers", "$fplayer_team_no", "$fplayer_agent_no", "$archer_space", "$archer_formation_type"),		
			(try_end),
			(assign, "$archer_formation_move_order", mordr_hold),
		(try_end),
		(agent_set_position, "$fplayer_agent_no", pos49),
		(assign, "$gk_order_hold_over_there", 0)
	]),

	(1, 0, 0, [	#attempt to avoid simultaneous formations function calls
		(call_script, "script_store_battlegroup_data"),
		(neg|key_is_down, key_for_ranks),
		(neg|key_is_down, key_for_shieldwall),
		(neg|key_is_down, key_for_wedge),
		(neg|key_is_down, key_for_square),
		(neg|key_is_down, key_for_undo),
		(neg|game_key_is_down, gk_order_1),
		(neg|game_key_is_down, gk_order_2),
		(neg|game_key_is_down, gk_order_3),
		(neg|game_key_is_down, gk_order_4),
		(neg|game_key_is_down, gk_order_5),
		(neg|game_key_is_down, gk_order_6)
	  ], [
		(set_fixed_point_multiplier, 100),
		(store_mod, ":fifth_second", "$fclock", 5),
		(call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
		(try_begin),
			(eq, reg0, 0),	#no more enemies?
			(call_script, "script_formation_end", "$fplayer_team_no", grc_everyone),
		(else_try),
			(assign, "$autorotate_at_player", 0),
			(try_begin),
				(neq, "$infantry_formation_type", formation_none),
				(try_begin),
					(eq, "$infantry_formation_move_order", mordr_follow),
					(call_script, "script_cf_formation", "$fplayer_team_no", grc_infantry, "$infantry_space", "$infantry_formation_type"),
				(else_try),	#periodically reform
					(eq, ":fifth_second", 0),
					(team_get_movement_order, reg0, "$fplayer_team_no", grc_infantry),
					(neq, reg0, mordr_stand_ground),
					(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", grc_infantry),
					(position_move_y, pos1, -2000),
					(call_script, "script_point_y_toward_position", pos1, pos60),
					(position_move_y, pos1, 2000),
					(call_script, "script_set_formation_position", "$fplayer_team_no", grc_infantry, pos1),					
					(call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_infantry),
					(assign, ":troop_count", reg0),
					(call_script, "script_get_centering_amount", "$infantry_formation_type", ":troop_count", "$infantry_space"),
					(position_move_x, pos1, reg0),
					(call_script, "script_form_infantry", "$fplayer_team_no", "$fplayer_agent_no", "$infantry_space", "$infantry_formation_type"),		
				(try_end),
			(try_end),
			(try_begin),
				(neq, "$cavalry_formation_type", formation_none),
				(try_begin),
					(eq, "$cavalry_formation_move_order", mordr_follow),
					(call_script, "script_cf_formation", "$fplayer_team_no", grc_cavalry, "$cavalry_space", "$cavalry_formation_type"),
				(else_try),	#periodically reform
					(eq, ":fifth_second", 0),
					(team_get_movement_order, reg0, "$fplayer_team_no", grc_cavalry),
					(neq, reg0, mordr_stand_ground),
					(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", grc_cavalry),
					(call_script, "script_point_y_toward_position", pos1, pos60),
					(call_script, "script_set_formation_position", "$fplayer_team_no", grc_cavalry, pos1),
					(call_script, "script_form_cavalry", "$fplayer_team_no", "$fplayer_agent_no", "$cavalry_space"),
				(try_end),
			(try_end),
			(try_begin),
				(neq, "$archer_formation_type", formation_none),
				(try_begin),
					(eq, "$archer_formation_move_order", mordr_follow),
					(call_script, "script_cf_formation", "$fplayer_team_no", grc_archers, "$archer_space", "$archer_formation_type"),
				(else_try),	#periodically reform
					(eq, ":fifth_second", 0),
					(team_get_movement_order, reg0, "$fplayer_team_no", grc_archers),
					(neq, reg0, mordr_stand_ground),
					(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", grc_archers),
					(position_move_y, pos1, -2000),
					(call_script, "script_point_y_toward_position", pos1, pos60),
					(position_move_y, pos1, 2000),
					(call_script, "script_set_formation_position", "$fplayer_team_no", grc_archers, pos1),
					(call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_archers),
					(assign, ":troop_count", reg0),
					(call_script, "script_get_centering_amount", formation_default, ":troop_count", "$archer_space"),
					(val_mul, reg0, -1),
					(position_move_x, pos1, reg0),
					(call_script, "script_form_archers", "$fplayer_team_no", "$fplayer_agent_no", "$archer_space", "$archer_formation_type"),		
				(try_end),
			(try_end),
			(assign, "$autorotate_at_player", formation_autorotate_at_player),
		(try_end),
		(val_add, "$fclock", 1),
	]),
]
#end formations triggers


def modmerge_formations_mission_templates(orig_mission_templates):
	# brute force add formation triggers to all mission templates with mtf_battle_mode
	for i in range (0,len(orig_mission_templates)):
		if( orig_mission_templates[i][1] & mtf_battle_mode ):
			orig_mission_templates[i][5].extend(formations_triggers)
