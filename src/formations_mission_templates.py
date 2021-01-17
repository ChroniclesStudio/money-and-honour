# Formations by Motomataru

from module_constants import *

# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "mission_templates"
		orig_mission_templates = var_set[var_name_1]

		# START do your own stuff to do merging

		if (version > 1011): # assume warband
			from formations_mission_templates_wb import modmerge_formations_mission_templates
			logger.info("Version is warband, merging %s using warband routine."% var_name_1)
		else:
			from formations_mission_templates_mb import modmerge_formations_mission_templates
			logger.info("Version is not warband, merging %s using vanilla routine."% var_name_1)

		modmerge_formations_mission_templates(orig_mission_templates)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
