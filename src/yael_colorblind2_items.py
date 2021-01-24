

#### MODULE CODE

from traceback import print_exc
from pprint import pprint
from yael_util import *

def modmerge(var_set):
    try:
        items = var_set['items']

        ## Works as intended, but white armor looks out-of-place
        ## ingame. Enforcing blue player-clothing would be better.
        swapstats(items, 'arena_tunic_white', 'arena_tunic_green')
        swapstats(items, 'arena_armor_white', 'arena_armor_green')
        # pprint([y_get(items,'arena_{0}_{1}'.format(a,b)) for a in ('tunic','armor') for b in ('green','white')])
    except:
        print_exc()

def swapstats(items, id_a, id_b):
    '''
    Swap definitions of items, keeping the ID.
    '''
    index_a, entry_a = y_get(items, id_a)
    index_b, entry_b = y_get(items, id_b)
    items[index_a] = tuple([id_a] + entry_b[1:])
    items[index_b] = tuple([id_b] + entry_a[1:])
