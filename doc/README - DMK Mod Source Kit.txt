--------------------------------
DMK Mod Source Kit Package - OSP
--------------------------------

For: Mount & Blade Warband (Might work for WFAS also)
Modulesystem: 1.171
-------------------------
Creators: Davee & Flanged
-------------------------

Edited by Bronzeca & Iceqatius (2020.11.14)

Since this source kit is difficult to find
we decided to make this little package and 
add some more information about how to get
it into other mods. Needless to say is that you
need the sourcecode for whatever mod you are
altering. Unless you are a master textedit
expert its nearly impossible to add it with
only text files.

The most important thing is to read the mod
creators statements in the py files and follow
them to the letter. Step by step.

The difficult thing for newbie modders
is found in the module_mission_templates 
where the placement of triggers can cause 
some problems. 

It is quite simple, place the big text package
as instructed above the multiplayer_server_check_belfry_movement
in the file then you place the mod triggers with other triggers in the
different missions. These other triggers usually have names like common_music_situation_update
and common_battle_init_banner.

The mod triggers are: 

dismemberment_mod_decap,
dismemberment_mod_hands1,
dismemberment_mod_hands2,
dismemberment_mod_arms1,
dismemberment_mod_arms2,
dismemberment_mod_hotkeys, 

Use the search function and place them with the other triggers:

"quick_battle_battle" - Just above - common_music_situation_update,
"quick_battle_siege" - Just above - common_custom_battle_tab_press,
"lead_charge" - Just above - common_battle_init_banner,
"village_attack_bandits" - Just above common_music_situation_update,
"village_raid" - Just above - common_battle_tab_press,
"besiege_inner_battle_castle" - Just above - common_battle_tab_press,
"besiege_inner_battle_town_center" - Just above common_battle_tab_press,
"castle_attack_walls_defenders_sally" - Just above - common_battle_tab_press,
"castle_attack_walls_belfry" - Just above - common_battle_mission_start,
"castle_attack_walls_ladder" - Just above - common_battle_mission_start,

As you can see its alot..the important ones for singleplayer is: "lead charge"
and all below it. Lead charge is the main field battles and the rest is villages 
and sieges.

--------------------------------------------
Files included:

module_animation.py
module_items.py
module_mission_templates.py
module_particle_systems.py
module_scene_props.py
module_sounds.py
module_troops.py

Resource folder with needed files
Texture folder with needed files
Soundfolder with optional files

Readme.txt

--------------------------------------------

Some mod-related testing and debug hotkeys:


K + Right Ctrl: Spawn dismemeberable (hand and arms) enemies in front of you

J + Right Ctrl: Spawn superweapons at your feet (including decapitation crossbow)

M + Right Ctrl: Decap deug mode on/off (makes it much easier to cause decaps)


Have fun!