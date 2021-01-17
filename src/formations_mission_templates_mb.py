# Formations for Mount & Blade by Motomataru
# rel. 01/03/11

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *

# Formations triggers v3 by motomataru
# Global variables	*_formation_type holds type of formation: see "Formation modes" in module_constants
#					*_formation_move_order hold the current move order for the formation
#					*_space hold the multiplier of extra space ordered into formation by the player

formations_triggers = [
	(ti_before_mission_start, 0, 0, [], [
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

#charge ends formation
	(0, 0, 1, [(game_key_clicked, gk_order_charge)], [
		(assign, "$fclock", 1),
		(call_script, "script_player_order_formations", mordr_charge)
	]),

#dismount ends formation
	(0, 0, 1, [(game_key_clicked, gk_order_dismount)], [
		(assign, "$fclock", 1),
		(call_script, "script_player_order_formations", mordr_dismount),
	]),
		
#On hold, any formations reform in new location		
	(0, 0, 1, [(game_key_clicked, gk_order_halt)], [
		(assign, "$fclock", 1),
		(call_script, "script_player_order_formations", mordr_hold)
	]),
		
#Follow is hold	repeated frequently
	(0, 0, 1, [(game_key_clicked, gk_order_follow)], [
		(assign, "$fclock", 1),
		(call_script, "script_player_order_formations", mordr_follow)
	]),

	(1, 0, 0, [	#attempt to avoid simultaneous formations function calls
		(call_script, "script_store_battlegroup_data"),
		(neg|key_is_down, key_for_ranks),
		(neg|key_is_down, key_for_shieldwall),
		(neg|key_is_down, key_for_wedge),
		(neg|key_is_down, key_for_square),
		(neg|key_is_down, key_for_undo),
		(neg|game_key_is_down, gk_order_charge),
		(neg|game_key_is_down, gk_order_dismount),
		(neg|game_key_is_down, gk_order_halt),
		(neg|game_key_is_down, gk_order_follow),
		(neg|game_key_is_down, gk_order_advance),
		(neg|game_key_is_down, gk_order_fall_back),
		(neg|game_key_is_down, gk_order_spread_out),
		(neg|game_key_is_down, gk_order_stand_closer)
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
		
	(0, 0, 0, [(game_key_clicked, gk_order_advance)], [(call_script, "script_player_order_formations", mordr_advance)]),
		
	(0, 0, 0, [(game_key_clicked, gk_order_fall_back)], [(call_script, "script_player_order_formations", mordr_fall_back)]),
		
	(0, 0, 0, [(game_key_clicked, gk_order_spread_out)], [(call_script, "script_player_order_formations", mordr_spread_out)]),
		
	(0, 0, 0, [(game_key_clicked, gk_order_stand_closer)], [(call_script, "script_player_order_formations", mordr_stand_closer)]),

]
#end formations triggers


def modmerge_formations_mission_templates(orig_mission_templates):
	# brute force add formation triggers to all mission templates with mtf_battle_mode
	for i in range (0,len(orig_mission_templates)):
		if( orig_mission_templates[i][1] & mtf_battle_mode ):
			orig_mission_templates[i][5].extend(formations_triggers)
