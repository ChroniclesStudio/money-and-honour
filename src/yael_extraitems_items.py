from __future__ import print_function
from traceback import print_exc
from pprint import pprint
from yael_util import *

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *


# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

print('  ' + __name__)

def makedummy(dummy_offset):
    '''
    Dummy items for later additions.
    
    As removing items breaks save games, and reordering items mixes up
    items in the same game, I add dummy placeholders for future additions.
    '''
    return [
        "yael_dummy_"+str(dummy_offset), 
        "YAEL_EXTRAITEMS_DUMMY_" + str(dummy_offset), 
        [("book_a",0)], 
        itp_type_head_armor | itp_doesnt_cover_hair | itp_fit_to_head, 
        0,880,
        weight(14)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|head_armor(48)|difficulty(0),
        imodbits_cloth
    ]


EXTRA_ITEMS = [
    # stats like sarranid_elite_armor
    [
        "yael_elite_tribal_warrior_outfit", 
        "Elite Tribal Warrior Outfit", 
        [("tribal_warrior_outfit_a_new",0)], 
        itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,
        0,
        3828 ,
        weight(14)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(0),
        imodbits_cloth 
    ],
    makedummy(2),
    [
        "yael_invisible_nordic_warlord_helmet", 
        "Invisible Nordic Warlord Helmet", 
        [("invalid_item",0)], 
        itp_merchandise | itp_type_head_armor | itp_doesnt_cover_hair | itp_fit_to_head ,
        0, 
        880 , 
        weight(2.25)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,
        imodbits_plate 
    ],
    makedummy(4),
    makedummy(5),
    makedummy(6),
    makedummy(7),
    makedummy(8),
    makedummy(9),
    makedummy(10),
    makedummy(11),
    makedummy(12),
    makedummy(13),
    makedummy(14),
    makedummy(15),
    makedummy(16),
    makedummy(17),
    makedummy(18),
    makedummy(19),
    makedummy(20),
    makedummy(21),
    makedummy(22),
    makedummy(23),
    makedummy(24),
    makedummy(25),
    makedummy(26),
    makedummy(27),
    makedummy(28),
    makedummy(29),
    makedummy(30),
    makedummy(31),
    makedummy(32),
    makedummy(33),
    makedummy(34),
    makedummy(35),
    makedummy(36),
    makedummy(37),
    makedummy(38),
    makedummy(39),
    makedummy(40),
    makedummy(41),
    makedummy(42),
    makedummy(43),
    makedummy(44),
    makedummy(45),
    makedummy(46),
    makedummy(47),
    makedummy(48),
    makedummy(49),
    makedummy(50),
]

def modmerge(var_set):
    try:
        items = var_set['items']
        insertpos = 'not_found'
        for idx, item in enumerate(items):
            if item[0] == "items_end":
                insertpos = idx
                break

        assert insertpos != 'not_found'

        items[insertpos:insertpos] = EXTRA_ITEMS

        if False:
            for idx, item in enumerate(items):
                print('   ', (idx, item[0]))
        
    except:
        print_exc()




#### REMARKS
##
## [1] Cannot reduce total number of items without breaking save
## games. It is however possible to remove itp_merchandise / change
## the model to some obvious placeholder like invalid_item, book_a
## through book_e, etc.
