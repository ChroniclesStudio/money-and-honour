#### HEADER

from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

######################################################################
#  Each presentation record contains the following fields:
#  
#  1) Presentation id: used for referencing presentations in other
#     files. The prefix prsnt_ is automatically added before each
#     presentation id.
#  2) Presentation flags. See header_presentations.py for a list of
#     available flags
#  3) Presentation background mesh: See module_meshes.py for a list of
#     available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
#  
######################################################################


#### MODULE CODE

print '  ' + __name__


presentations = [
  ("yael_equip_overview", 0, mesh_load_window, [
      (ti_on_presentation_load,
       [(call_script, "script_yael_eqmgr_presentation_load")]),
      (ti_on_presentation_event_state_change,
       [(call_script, "script_yael_eqmgr_presentation_event_state_change")]),
      (ti_on_presentation_mouse_enter_leave,
       [(call_script, "script_yael_eqmgr_presentation_on_mouse_enter_leave")]),
      (ti_on_presentation_mouse_press,
       [(call_script, "script_yael_eqmgr_presentation_on_mouse_press")]),
  ]),
]
