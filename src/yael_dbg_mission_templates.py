

from traceback import print_exc
from pprint import pprint
from yael_util import *


def modmerge(var_set):
    try:
        print '  ' + __name__
        mtl = var_set['mission_templates']
        lead_charge = y_get_path(mtl, ('lead_charge',))
        triggers = lead_charge[5]
        if False:
            for i, t in enumerate(triggers):
                print "%d'th trigger" % i
                y_pprint_script(t[3])
                y_pprint_script(t[4])
                print ''
    except:
        print_exc()
