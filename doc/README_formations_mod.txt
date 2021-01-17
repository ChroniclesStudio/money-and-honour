Formations and AI Mods by Motomataru
06/08/11

This kit contains two minimods by motomataru. It is presented in source code for addition to larger mods.

1. A formations mod, contained in files formations_*.py
2. An extension mod to replace Native AI, contained in files formAI_*.py

The formations mod is an extensive reworking of the original simple interface by Mirathei. At a command, infantry can form in ranks by level, ranks by shield/weapon, wedge by level, or square. Cavalry can form a wedge. Formations follow all battlefield commands, including from the battle panel. Native AI is given the ability to make the same formations.

The formations AI replaces Native AI. It makes decisions based primarily on army size rather than army composition. Each type of unit has different objectives. The intent was to make the AI smarter AND more proactive.


INSTALLATION:
The source files here are prepped for use with modmerger by sphere. I provide alternative instructions in case a modder wishes to install by manual edit.

Modmerger
1. If you wish to start using modmerger, obtain if from http://www.mbrepository.com/file.php?id=2151. Install it according to the directions in its readme file.
2. Copy the formations_*.py and formAI_*.py files to the compile directory (where you installed modmerger).
3. Update the modmerger_options.py file as follows:
	- change "version" to 1011 ONLY IF you are installing for M&B 1.011
	- add "formations" and (if desired) "formAI" to the mods_active list. See included version of this file for a sample mods_active list.
4. Comment out Native AI from module_mission_templates if you are using formAI. See notes at start of formAI_missions_templates_*.py files. Plans now are to install an in-game switch to do this, but for now, you must edit.
5. Run build_module!

For updates to either mod, simply replace the formations_*.py or formAI_*.py files.


Manual Install
1. Append the constants listed in form*_constants.py files to module.constants.py.
2. Add the scripts from form*_scripts.py to module_scripts.py.

For the two battle_tactic* functions listed, you'll have to change the name of the originals by prefixing them with "orig_". That, is, they should end up named "orig_battle_tactic_init_aux" and "orig_battle_tactic_apply_aux".

Then add the line
(call_script, "script_player_order_formations", ":order"),	#for formations
before the last command of the existing team_give_order_from_order_panel script (i.e. before the set_show_messages call).

5. For formations_presentations, place the contents of code_block1 before the call to script_update_order_flags_on_map for the "battle" presentation. As of version 1.127, this was line 9990.
6. Add the lists of triggers from form*_mission_templates.py to module_mission_templates.py right before the list of mission templates (i.e., right above where it says "mission_templates = [").

The formations triggers can be added to any mission template by "adding" them to the end of the triggers list for that template, like so:
"    ] + formations_triggers + AI_triggers	"

7. If you use the AI in a mission template, comment out any competing Native AI triggers. In the lead_charge template, for example, there are two of them, but DO NOT comment out the morale/courage triggers inserted between them! See top of formAI_mission_templates_*.py for example.

For updates to either mod, you'll have to manually replace these code sections.


KNOWN CONFLICTS WITH OTHER MODS:
Player's initial formation conflicts with Caba'drin's prebattle orders. Comment out the section starting with message "Forming Ranks" in formations_mission_templates.


TWEAKS:
The constants source files conveniently have a number of settings that you can tweak. I recommend SAVING a copy of your tweaks against having them overwritten by a mod update.

formations_constants.py
formation_minimum_spacing: minimum number of centimeters between troops in formation
formation_start_spread_out: number of half-meters to add between troops in a NEW formation (for ease of maneuvering). Set to 0, all spreading out and coming together must be done by the player
formation_min_foot_troops: minimum number of troops for anything but cavalry formation
formation_min_cavalry_troops: minimum number of troops for cavalry formation
formation_autorotate_at_player: set to 1 to autorotate toward enemy, 0 to form in direction player is facing
formation_native_ai_use_formation: set to 1 for Native AI to use formations, 0 otherwise
formation_delay_for_spawn: lower if troops charge too long before initial forming up, raise if troops arrive too late to form up
command keys: keys for specifying each formation (or none/unform)

formAI_constants.py
AI_firing_distance: centimeters archers will try to maintain to target
AI_charge_distance: centimeters under which melee troops consider themselves under attack
AI_for_kingdoms_only: set to 1 for AI for kingdoms and deserters only, 0 otherwise
Percentage_Cav_For_New_Dest: percent of formation at destination required to select a new one. The higher you make this, the more cavalry will wait to form up before next action.
Hold_Point: ratio compared to largest team under which AI will take defensive
positions: chosen for lack of use in Native scripts, but you may want to double-check that the longer-term ones don't conflict with any others in your specific mod.

In formations_scripts.py, you may want to change the switch in script_get_default_formation to change default formations (or add new ones for mod factions)


QUICK PLAY GUIDE:
Any time in-game that you have a formation form or "Hold," it will set up near the position that the player had when the command was issued: infantry to the left, cavalry to the right, and archers up front. Additionally, the formations may maintain the same FACING that the player had (depending on mod design).

Whenever a unit first forms a particular formation, troops may spread out for ease of forming up (depending on mod design).

Player troops start every battle in formation.

Unless changed by mod design, formation key bindings are:
"J" for ranks
"K" for weapon-based ranks (shieldwall, phalanx)
"L" for wedge (the player ought to reassign the "L" for "Log" mapping)
";" for square
"U" for no formation (undo formation)

The "ranks" command for archers puts them in a staggered line.

Cavalry will not make any formation other than the wedge.

Charge (and Dismount for cavalry) will undo a formation. The player may Advance multiple times to have a formation move toward the average position of the enemy. Or use the order panel or hold-F1 to place them (or sweep them across the enemy for the cavalry wedge).


DETAILS:
Order tracking is problemmatic in Warband (see http://forums.taleworlds.com/index.php/topic,34685.msg2899385.html#msg2899385). Since ESC cannot be tracked mid-command, the player must re-identify the battle group rather than ESC out of the command menu.

For more, see the forum http://forums.taleworlds.com/index.php/topic,34685.480.html starting around p.33

v1 of the AI was developed for StarWars Conquest. I still recommend it for mods in which warfare is primarily with ranged weapons (like blasters!). See http://mbx.streetofeyes.com/index.php/topic,2143.msg50910.html#msg50910


Formations v. 4 (ETD Jan. 1, 2010?)
1. Make level a multiplier rather than a bump?
2. Test if all cavalry unhorsed at start of mission
3. Complete design and implementation of battlegroup globals
4. Infantry during setup move directly to destination
5. Implement sphere's auto-options page
6. Improve infantry stand under cavalry attack
7. Infantry does not move on if # in melee a significant % of #infantry
8. Look into setting stab-only in close formations
9. Have player Charge use AI functions for attacking other battlegroups (w/o target acquisition for Cavalry)
10. Have Hold-F1 select a target battlegroup over that spot
11. Back to Mirathei formation implementation for aesthetics (continual form-up (sep trigger) around form leader (but keep rot), who alone has dest)
12. Expand formations to all battlegroups
13. Add formations to battle menu
14. Bind formations to F4 key


ACKNOWLEDGEMENTS:
Mirathei - for original concept and code
Sphere - modmerger installation system and suggestions
Idibil - for enthusiastically cracking the whip in order to use these mods in Brytenwalda
Othr, Dunde, Treebeard - for understanding my code well enough to fix it
Brytenwalda betatesters, including Rad, Harper2010, Trinkof
HokieBT - hosting AI prototype in SWC


CHANGE LOG:
6/25/2010
--Fix Native AI use of formations
--Implement new RETREAT order (add OR to CHARGE section of script_player_order_formations and call from formations_triggers in module_mission_templates)
7/14/2010 
-- Attempt to peg fixed point multiplier
-- Move important developer constants to module_constants
-- New script to switch default formation (for developers)
7/19/2010
-- Split constants for minimum troops for formation
7/26/2010
-- Fixed FPM in module_presentations
-- Added morale flag
-- Replace agent_get_class with agent_get_division
7/31/2010
-- Added optional autorotate of formations at player position
8/1/2010
-- Resolve class/division issue
8/2/2010
-- Improve get_default_formation
8/6/2010
-- Place spawn delay in constants
-- AI: add special consideration for horse archers
-- AI: close up infantry on attack
-- Center solo formations on Hold-F1 placement
-- AI: fix cavalry behavior at scene boundaries
-- Rotate player formations to face enemy on reform
-- Shut off messages for size 0 battlegroups
8/13/2010
-- Correct player formation rotation on reform
-- AI: decrease range if "archers" use thrown weapons
-- AI: make sure infantry and cavalry charge on outnumber
-- AI: fix infantry unform against isolated troops
-- AI: use square and wedge formations under certain conditions
-- AI: prevent rotation swings near enemy units
-- AI: fix formation distance from enemy formation
-- AI: mitigate formations' tendency to rotate left in combat
8/22/2010
-- Migrate to modmerger 2.3
8/27/2010
-- AI: react to player charge earlier
-- AI: hold if outnumbered, period (used to attack at 1:2 odds)
-- AI: put Hold figure in tweak section of constants
-- AI: increase odds required to "mop up" from 4:1 to 6:1
-- AI: make battle phases explicit
-- AI: add Jockey battle phase to counter player pre-battle maneuvers
-- AI: improve behavior at reinforcement
-- AI: will advance in lull in fighting only when superior
-- AI: archer reposition during fighting if enemy too far or too close
-- AI: have archers reposition toward entry
-- AI: keep archers from outstripping infantry advance
-- AI: variable shot distance related to number of throwers
-- AI: infantry will only attempt to whelm nearby isolated troops
-- AI: melee refs to archers test if there ARE any
-- AI: cavalry revert to standard charge if nearest target too close to nearest threat
-- Fix position conflict in Hold-F1 trigger
-- Take player troops out of formation end of battle so they can cheer
-- Player reform function only if troops in formation
-- Change formation algorithm to prevent troop crossing
8/28/2010
-- Give leaders special agent classification
-- AI: remove morale scripts (redundant in mt_lead_charge and incomplete everywhere else)
-- AI: fix undefined agent bug
9/4/2010
-- Turn off autorotate when troops following player
-- Fix team faction determination bug
-- Center expand/contract of troops that are not next to player
-- AI: add switch to turn off AI for non-kingdom teams (e.g. bandits)
-- AI: ensure first trigger fires after formations' to capture formations' inits
-- AI: fix mop up ratio for melee troops
-- AI: add agent rout tests to survey functions (don't count routing troops)
-- AI: replace deleted infantry position (oops!)
9/14/2010
-- AI: return charging distance to 20m
-- AI: have archers reassess every 5 seconds instead of 10
-- AI: add two meters to minimum archer distance to prevent all-javelin "archers" from auto-instigating a melee
-- AI: keep infantry from wandering off to non-cavalry target when archers under attack by cavalry
-- AI: sharpen up ranging at start of battle
-- AI: disallow specialized formations if there's no default formation
-- AI: infantry anticipate enemy cavalry charge
9/18/2010
-- AI: fix archer decision to move
-- AI: fix logic leading to Jockey phase of battle
-- Use leader in faction determination at start of battle
9/30/2010
-- Reenable archer stagger as option
-- Fix typo in team faction determination script
-- AI: default long range extended to empirical limit
-- Fix centering: archers Hold-F1, stand closer, spread out; archers & infantry Hold from battle panel
-- AI: add cavalry line charge and generally make them more aggressive
-- AI: add leader placement for when there is no infantry to stand by
-- AI: remove leader speed limitation: no longer needed
-- Have battlegroups/divisions 3-8 hold at start of battle
10/07/2010
-- Change: archer stagger is now archer "ranks" formation
-- AI: close a couple loopholes that were preventing infantry advance
-- AI: change logic that sometimes kept cavalry from charging
10/15/2010
-- AI: broaden test of army nearness to enemy for switch into fight phase
-- AI: break formation only for lower level troops
-- AI: remove random variable in cavalry target assessment
-- AI: double cavalry strength assessment vs. potential non-cavalry threat/target
-- AI: specify cavalry decision to free fight more precisely
-- AI: ignore fake reinforcements (i.e. reinforcements stages > 1)
-- AI: handle no archer situation for horse archers and during reinforcement
-- AI: remove obsolete destination tracking for cavalry wedge (and whatever loopholes that created)
11/12/2010
-- AI: handle team_give_order lumping mounted heroes with infantry
-- Rewrite arcsine in script_point_y_toward_position from scratch
-- Shut down reform on Stand Ground
-- Center rotation on reform (in progress)
-- AI: refine infantry formation approach
-- Reset reform clock for most formation commands
-- Fix centering function error
-- AI: Fix null target/threat logic (thanks Treebeard)
12/26/2010
-- Move some battlegroup data functionality to formations level for efficiency
-- Standardize formation positioning and centering
-- Fix cf_formation return values
-- Rename a constant to avoid collision with another mod
-- Give player cavalry room to set up
-- AI: back off another rank against opponents in deep formation
12/28/2010
-- Fix order tracking bug
-- Fix typo blocking Group8 data (thanks Treebeard)
01/03/2011
-- Fix default formation for independent player
-- Fix another order tracking bug on cavalry dismount
-- AI: restore data function to AI trigger to ensure accuracy (produced lots of Agent 0 errors)
06/08/2011
-- AI: Fix AI not attacking unmounted player
-- AI: Have AI take over dead player troops
-- Fix player formations running off
-- Add new argument to agent_get_ammo