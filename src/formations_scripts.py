# Formations AI by Motomataru

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
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]

		# START do your own stuff to do merging

		if (version > 1011): # assume warband
			from formations_scripts_wb import modmerge_formations_scripts
			logger.info("Version is warband, merging %s using warband routine."% var_name_1)
		else:
			from formations_scripts_mb import modmerge_formations_scripts
			logger.info("Version is not warband, merging %s using vanilla routine."% var_name_1)

		modmerge_formations_scripts(orig_scripts)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
# INSTRUCTIONS:
# Insert an uncommented copy of the code snippet between formation_start and
# formation_end at the end of module_scripts.py

## formation_start
#try:
#	from formations_scripts import modmerge_formations_scripts
#	modmerge_formations_scripts( scripts )
#except:
#	import sys
#	print "Formations: Unexpected error:", sys.exc_info()[1]
#	raise
## formation_end
     

from header_common import *
from header_operations import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from ID_animations import *

# start get version: this section is only needed if you need version-dependent merging
try:
    from modmerger_options import module_sys_info
    version = module_sys_info["version"]
except:
    version = 1127 # version not specified. assume warband this is last built on
# end get version


def modmerge_formations_scripts(orig_scripts):
    var_name_1 = "scripts"
    
    if (version > 1011): # assume warband
        from formations_scripts_wb import modmerge_formations_scripts as modmerge_formations_scripts_wb
        logger.info("Version is warband, merging %s using warband routine."% var_name_1)
        modmerge_formations_scripts_wb(orig_scripts)
    else:
        from formations_scripts_mb import modmerge_formations_scripts as modmerge_formations_scripts_mb
        logger.info("Version is not warband, merging %s using vanilla routine."% var_name_1)
        modmerge_formations_scripts_mb(orig_scripts)



# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1]

		# START do your own stuff to do merging

        modmerge_formations_scripts(orig_scripts)

		# END do your own stuff

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
    
