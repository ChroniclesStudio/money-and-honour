# Formations AI by Motomataru
# rel. 12/26/10

from formations_constants import formation_delay_for_spawn

#AI variables
AI_long_range	= 13000	#do not put over 130m if you want archers to always fire
AI_firing_distance	= AI_long_range / 2
AI_charge_distance	= 2000
AI_for_kingdoms_only	= 0
Far_Away	= 1000000
Percentage_Cav_For_New_Dest	= 40
Hold_Point	= 100	#archer hold if outnumbered
Advance_More_Point	= 100 - Hold_Point * 100 / (Hold_Point + 100)	#advance 'cause expect other side is holding
AI_Delay_For_Spawn	= formation_delay_for_spawn + .1	#fire AFTER formations init

#Battle Phases
BP_Setup	= 1
BP_Jockey	= 2
BP_Fight	= 3

#positions used in a script, named for convenience
Nearest_Enemy_Troop_Pos	= 46	#pos46
Nearest_Non_Cav_Enemy_Troop_Pos	= 47	#pos47
Nearest_Threat_Pos	= 48	#pos48
Nearest_Target_Pos	= 49	#pos49
Infantry_Pos	= 50	#pos50
Archers_Pos	= 51	#pos51
Cavalry_Pos	= 52	#pos52
Enemy_Team_Pos	= 53	#pos53
Nearest_Enemy_Battlegroup_Pos	= 54	#pos54

#positions used through battle
Team0_Cavalry_Destination	= 56	#pos56
Team1_Cavalry_Destination	= 57	#pos57
Team2_Cavalry_Destination	= 58	#pos58
Team3_Cavalry_Destination	= 59	#pos59
Team0_Starting_Point	= 12	#pos12
Team1_Starting_Point	= 13	#pos13
Team2_Starting_Point	= 14	#pos14
Team3_Starting_Point	= 16	#pos16