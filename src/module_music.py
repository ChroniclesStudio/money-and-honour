# -*- coding: utf-8 -*-
from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
##  ("losing_battle", "alosingbattle.mp3", sit_calm|sit_action),
##  ("reluctant_hero", "reluctanthero.mp3", sit_action),
##  ("the_great_hall", "thegreathall.mp3", sit_calm),
##  ("requiem", "requiem.mp3", sit_calm),
##  ("silent_intruder", "silentintruder.mp3", sit_calm|sit_action),
##  ("the_pilgrimage", "thepilgrimage.mp3", sit_calm),
##  ("ambushed", "ambushed.mp3", sit_action),
##  ("triumph", "triumph.mp3", sit_action),

##  ("losing_battle", "alosingbattle.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("reluctant_hero", "reluctanthero.mp3", mtf_sit_attack),
##  ("the_great_hall", "thegreathall.mp3", mtf_sit_map_travel),
##  ("requiem", "requiem.mp3", mtf_sit_map_travel),
##  ("silent_intruder", "silentintruder.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("the_pilgrimage", "thepilgrimage.mp3", mtf_sit_map_travel),
##  ("ambushed", "ambushed.mp3", mtf_sit_attack),
##  ("triumph", "triumph.mp3", mtf_sit_attack),

##mtf_culture_1|法兰克文化
##mtf_culture_2|罗斯斯拉夫文化
##mtf_culture_3|契丹及突厥西亚文化
##mtf_culture_4|斯堪的纳维亚文化及不列颠文化
##mtf_culture_5|伊比利亚及南意大利文化
##mtf_culture_6|阿拉伯及北非文化



##Europa Universalis IV|欧陆风云4
##Main Theme
##Battle Of Breitenfeld
##Battle Of Lepanto
##Kings in the North
##Night Time
##Ride Forth Victoriously
##The End Of An Era
##The Snow Is Coming
##The Sound Of Summer
##The Stage Is Set
##Discovery
##Commerce In The Peninsula
##Eire
##In The Streets
##King's Court
##Land In Sight

##Alatriste|佣兵传奇
##Asalto al Galeón
##Duelo
##La Playa
##Batalla
##Cuenta lo que fuimos (full listening)
##Fanfarre y Créditos

  ("bogus", "cant_find_this.ogg", 0, 0),
  
  #这首无用，不要修改
  ("bogus", "cant_find_this.mp3", 0, 0),
  #开始音乐
  ("Main_Theme", "Main_Theme.flac", mtf_sit_main_title|mtf_start_immediately, 0),
# ("Loading_screen", "Loading_screen.mp3", mtf_looping|mtf_start_immediately, 0),
## This can't be achieved!!!
  
  #遭遇战音乐
  ("ambushed_by_neutral", "ambushed_by_neutral.mp3", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight),
  #("ambushed_by_khergit", "ambushed_by_khergit.mp3", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  #("ambushed_by_nord",    "ambushed_by_nord.mp3", mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  #("ambushed_by_rhodok",  "ambushed_by_rhodok.mp3", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  #("ambushed_by_swadian", "ambushed_by_swadian.mp3", mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  #("ambushed_by_vaegir",  "ambushed_by_vaegir.mp3", mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  #("ambushed_by_sarranid", "middle_eastern_action.mp3", mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  
  #竞技场音乐
  #("arena_1", "arena_1.mp3", mtf_sit_arena, 0),
#  ("arena_2", "arena_2.mp3", mtf_looping|mtf_sit_arena, 0),
  #("armorer", "armorer.mp3", mtf_sit_travel, 0),
  #("bandit_fight", "bandit_fight.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  
  #大地图开场音乐
  ("Discovery", "Discovery.flac", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("Commerce_In_The_Peninsula", "Commerce_In_The_Peninsula.flac", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  
  #大地图音乐
  ("Night_Time", "Night_Time.flac", mtf_sit_night, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("The_Snow_Is_Coming", "The_Snow_Is_Coming.flac", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("The_Sound_Of_Summer", "The_Sound_Of_Summer.flac", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("Eire", "Eire.flac", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("In_The_Streets", "In_The_Streets.flac", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("King's_Court", "King's_Court.flac", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  
  #大地图结束曲
  ("The_End_Of_An_Era", "The_End_Of_An_Era.flac", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  
  #各阵营大地图音乐
  ("travel_Spain", "travel_Spain.mp3", mtf_culture_1|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_khergit", "travel_khergit.mp3", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_neutral", "travel_neutral.mp3", mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("travel_Sweden",   "travel_Sweden.flac",    mtf_culture_4|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok",  "travel_rhodok.mp3",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  
  ("travel_vaegir",  "travel_vaegir.mp3",  mtf_culture_2|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_sarranid",  "middle_eastern_travel.mp3",  mtf_culture_6|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  
  #被俘虏音乐
  ("captured", "capture.mp3", mtf_persist_until_finished, 0),
  ("defeated_by_neutral", "defeated_by_neutral.mp3",mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_2", "defeated_by_neutral_2.mp3", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_3", "defeated_by_neutral_3.mp3", mtf_persist_until_finished|mtf_sit_killed, 0),

  #乡村音乐
  ("empty_village", "empty_village.mp3", mtf_persist_until_finished, 0),
  ("encounter_hostile_nords", "encounter_hostile_nords.mp3", mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),
  ("escape", "escape.mp3", mtf_persist_until_finished, 0),
  
  #战斗音乐
  ("fight_1", "fight_1.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_2", "fight_2.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_3", "fight_3.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_4", "fight_4.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),  
  ("fight_5", "fight_5.flac", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),  
  
  ("Battle_Of_Breitenfeld", "Battle_Of_Breitenfeld.flac", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),  
  ("Battle_Of_Lepanto", "Battle_Of_Lepanto.flac", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),  
  
  #各阵营战斗音乐
  ("fight_as_Spain", "fight_as_swadian.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight, mtf_culture_all),
  
  ("fight_as_khergit", "fight_as_khergit.mp3", mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_as_nord", "fight_as_nord.mp3", mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_as_rhodok", "fight_as_rhodok.mp3", mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
#  ("fight_as_swadian", "fight_as_swadian.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight, mtf_culture_all),
  ("fight_as_vaegir", "fight_as_vaegir.mp3", mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_while_mounted_1", "fight_while_mounted_1.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_while_mounted_2", "fight_while_mounted_2.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_while_mounted_3", "warband_action.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  
  ("infiltration_khergit", "infiltration_khergit.mp3", mtf_culture_3|mtf_sit_town_infiltrate, mtf_culture_all),
  
  #被击败音乐
  ("killed_by_khergit", "killed_by_khergit.mp3", mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed, 0),
#  ("killed_by_neutral", "killed_by_neutral.ogg", mtf_persist_until_finished|mtf_culture_6|mtf_sit_killed, 0),
#  ("killed_by_nord", "killed_by_nord.ogg", mtf_persist_until_finished|mtf_culture_4|mtf_sit_killed, 0),
#  ("killed_by_rhodok", "killed_by_rhodok.ogg", mtf_persist_until_finished|mtf_culture_5|mtf_sit_killed, 0),
  ("killed_by_swadian", "killed_by_swadian.mp3", mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed, 0),
#  ("killed_by_vaegir", "killed_by_vaegir.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_killed, 0),
  
  #各阵营领主大厅音乐（本质大地图音乐）
  ("lords_hall_khergit", "lords_hall_khergit.mp3", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),
  ("lords_hall_nord", "lords_hall_nord.mp3", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_swadian", "lords_hall_swadian.mp3", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_rhodok", "lords_hall_rhodok.mp3", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_vaegir", "lords_hall_vaegir.mp3", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  
  ("neutral_infiltration", "neutral_infiltration.mp3", mtf_sit_town_infiltrate, 0),
  
  ("retreat", "retreat.mp3", mtf_persist_until_finished|mtf_sit_killed, 0),
 
  #攻城音乐
  ("seige_neutral", "seige_neutral.flac", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  ("enter_the_juggernaut", "enter_the_juggernaut.mp3", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("siege_attempt", "siege_attempt.mp3", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("crazy_battle_music", "crazy_battle_music.mp3", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  
  #酒馆及盛宴音乐
  ("tavern_1", "tavern_1.mp3", mtf_sit_tavern|mtf_sit_feast, 0),
  ("tavern_2", "tavern_2.mp3", mtf_sit_tavern|mtf_sit_feast, 0),
 
  #各阵营城镇音乐（本质大地图音乐）
  ("town_neutral", "town_neutral.mp3", mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("town_khergit", "town_khergit.mp3", mtf_culture_3|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_nord", "town_nord.mp3", mtf_culture_4|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_rhodok", "town_rhodok.mp3", mtf_culture_5|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_swadian", "town_swadian.mp3", mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_vaegir", "town_vaegir.mp3", mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  #通用胜利音乐
  ("victorious_evil", "victorious_evil.mp3", mtf_persist_until_finished, 0),
  ("victorious_neutral_1", "victorious_neutral_1.flac", mtf_sit_victorious, 0),
  ("victorious_neutral_2", "victorious_neutral_2.mp3", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_3", "victorious_neutral_3.mp3", mtf_persist_until_finished|mtf_sit_victorious, 0),

  #各阵营胜利音乐
  ("victorious_swadian", "victorious_swadian.mp3", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir", "victorious_vaegir.mp3", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir_2", "victorious_vaegir_2.mp3", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("wedding", "wedding.mp3", mtf_persist_until_finished, 0),

  ("coronation", "coronation.mp3", mtf_persist_until_finished, 0),



  
]