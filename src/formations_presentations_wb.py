# Formations AI for Warband by Motomataru
# rel. 12/26/10

from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations = [
] # presentations


# the following code block is to be inserted into "battle" presentation's trigger for ti_on_presentation_event_state_change
# just before the line (call_script, "script_update_order_flags_on_map"),
code_block1=[
# formations by motomataru
		  (assign, ":fixed_point_multiplier", 1),
		  (convert_to_fixed_point, ":fixed_point_multiplier"),
		  (set_fixed_point_multiplier, 100),
		  (call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
		  (try_begin),
			(eq, "$g_formation_group0_selected", 1),
			(neq, "$infantry_formation_type", formation_none),
			(copy_position, pos1, pos3),
			(call_script, "script_point_y_toward_position", pos1, pos60),
			(call_script, "script_set_formation_position", "$fplayer_team_no", grc_infantry, pos1),
			(call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_infantry),
			(assign, ":troop_count", reg0),
			(call_script, "script_get_centering_amount", "$infantry_formation_type", ":troop_count", "$infantry_space"),
			(position_move_x, pos1, reg0),
			(call_script, "script_form_infantry", "$fplayer_team_no", "$fplayer_agent_no", "$infantry_space", "$infantry_formation_type"),
			(assign, "$infantry_formation_move_order", mordr_hold),
		  (try_end),
		  (try_begin),
			(eq, "$g_formation_group1_selected", 1),
			(neq, "$archer_formation_type", formation_none),
			(copy_position, pos1, pos3),
			(call_script, "script_point_y_toward_position", pos1, pos60),
			(call_script, "script_set_formation_position", "$fplayer_team_no", grc_archers, pos1),
			(call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_archers),
			(assign, ":troop_count", reg0),
			(call_script, "script_get_centering_amount", formation_default, ":troop_count", "$archer_space"),
			(val_mul, reg0, -1),
			(position_move_x, pos1, reg0),
			(call_script, "script_form_archers", "$fplayer_team_no", "$fplayer_agent_no", "$archer_space", "$archer_formation_type"),
			(assign, "$archer_formation_move_order", mordr_hold),
		  (try_end),
		  (try_begin),
			(eq, "$g_formation_group2_selected", 1),
			(neq, "$cavalry_formation_type", formation_none),
			(copy_position, pos1, pos3),
			(call_script, "script_point_y_toward_position", pos1, pos60),
			(call_script, "script_set_formation_position", "$fplayer_team_no", grc_cavalry, pos1),
			(call_script, "script_form_cavalry", "$fplayer_team_no", "$fplayer_agent_no", "$cavalry_space"),
			(assign, "$cavalry_formation_move_order", mordr_hold),
		  (try_end),
		  (set_fixed_point_multiplier, ":fixed_point_multiplier"),
# end formations
          (call_script, "script_update_order_flags_on_map"),
]



from util_wrappers import *
from util_presentations import *

def modmerge_formations_presentations(orig_presentations):

    # inject code into battle presentation
    try:
        find_i = list_find_first_match_i( orig_presentations, "battle" )
        battlep = PresentationWrapper(orig_presentations[find_i])
        codeblock = battlep.FindTrigger(ti_on_presentation_event_state_change).GetOpBlock()
        pos = codeblock.FindLineMatching( (call_script, "script_update_order_flags_on_map") )
        codeblock.InsertBefore(pos, code_block1)			
    except:
        import sys
        print "Injecton 1 failed:", sys.exc_info()[1]
        raise
    # add remaining presentations
    add_presentations(orig_presentations, presentations, True)

