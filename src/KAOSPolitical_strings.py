# POLITICAL (1.2) by Lazeras
# Released 1 December 2014
strings = [
  #KAOS  (POLITICAL)
  ("lord_defects_rebel", "Lord Defects^^{s1} has denounced {s4} right to rule {s3}, and joined {s2} as the rightful ruler"),
  ("lord_defects_marshall", "Lord Defects^^{s1} Marshall of {s3} has abandonded  {reg4?her:his} allegiance to the {s3}, and joined {s2}"),

  ("kingdom_1_leader_male", "King {s0}"),
  ("kingdom_1_leader_female", "Queen {s0}"),
  ("kingdom_2_leader_male", "King {s0}"),
  ("kingdom_2_leader_female", "Queen {s0}"),
  ("kingdom_3_leader_male", "{s0} Khan"),
  ("kingdom_3_leader_female", "{s0} Khatun"),
  ("kingdom_4_leader_male", "King {s0}"),
  ("kingdom_4_leader_female", "Queen {s0}"),
  ("kingdom_5_leader_male", "Righ {s0}"),
  ("kingdom_5_leader_female", "Banrinn {s0}"),
  ("kingdom_6_leader_male", "{s0} Sultan"),
  ("kingdom_6_leader_female", "{s0} sultanah"),

  #Generla Kings Titles above standard
  ("kings_rank_2_male", "Emperor {s0}"),
  ("kings_rank_2_female", "Emporess {s0}"),
  ("kings_rank_1_male", "High King {s0}"),
  ("kings_rank_1_female", "High Queen {s0}"),
  ("faction_title_male_heir", "Prince {s0} {reg10?-{s61}:} "), 
  ("faction_title_female_Heir", "Princess {s0} {reg10?-{s61}:} "),

  ("faction_title_male_heir_high", "High Prince {s0} {reg10?-{s61}:} "), 
  ("faction_title_female_Heir_high", "High Princess {s0} {reg10?-{s61}:} "),

  ("faction_title_male_heir_empire", "Imperial Prince {s0} {reg10?-{s61}:} "), 
  ("faction_title_female_Heir_empire", "Imperial Princess {s0} {reg10?-{s61}:} "),
 
  ("faction_title_female_older_unmarried", "Maid {s0}"),
  ("faction_tittle_marshall", "Marshall"),
  ("kings_rank_0", "Warlord {s0}"),

  ("kaos_swadia_empire", "Empire of Swadia"),
  ("kaos_Vaegirs_empire", "Empire of Vaegirs"),
  ("kaos_Khergit_empire", "Khergit Empire"),
  ("kaos_Nords_empire", "Empire of Nords"),
  ("kaos_Rhodoks_empire", "Empire of Rhodoks"),
  ("kaos_Sarranid_empire", "Sarranid Empire"),

  ("kaos_swadia_king", "Kingdom of Swadia"),
  ("kaos_Vaegirs_king", "Kingdom of Vaegirs"),
  ("kaos_Khergit_king", "Khergit Khanate"),
  ("kaos_Nords_king", "Kingdom of Nords"),
  ("kaos_Rhodoks_king", "Kingdom of Rhodoks"),
  ("kaos_Sarranid_king", "Sarranid Sultanate"),



  ("kaos_swadia_king_20", "Duchy of Swadia"),
  ("kaos_Vaegirs_king_20", "Vaegirs Union"),
  ("kaos_Khergit_king_20", "Khergit Tribes"),
  ("kaos_Nords_king_20", "Duchy of Nords"),
  ("kaos_Rhodoks_king_20", "Duchy of Rhodoks"),
  ("kaos_Sarranid_king_20", "Sarranid Principality"),


  ("kaos_troop_note_relation", "{reg10? {s61}:}"),


# Jrider + TITLES v0.3 new titles, for suffix,  has been add to all titles except for king's
  ("new_faction_title_male_player", "Dominus {s0}{reg10?-{s61}:}"), # Latin
  ("new_faction_title_male_player_village", "Baro {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_player_castle", "Comes {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_player_town", "Dux {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_player_king", "Rex {s0}{reg10?-{s61}:}"),
  
  ("new_faction_title_male_1", "Lord {s0}{reg10?-{s61}:}"), # English
  ("new_faction_title_male_1_village", "Baron {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_1_castle", "Count {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_1_town", "Duke {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_1_king", "King {s0}{reg10?-{s61}:}"),
  
  ("new_faction_title_male_2", "Dvorianin {s0}{reg10?-{s61}:}"), # Russian
  ("new_faction_title_male_2_village", "Posadnik {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_2_castle", "Boyar {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_2_town", "Kniaz {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_2_king", "Korol {s0}{reg10?-{s61}:}"),

  ("new_faction_title_male_3", "Taishi {s0}{reg10?-{s61}:}"), # Mongol/Chinese
  ("new_faction_title_male_3_village", "Darga {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_3_castle", "Noyan {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_3_town", "Wang {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_3_king", "Khan {s0}{reg10?-{s61}:}"),

  ("new_faction_title_male_4", "Heera {s0}{reg10?-{s61}:}"), # Old norse/mid-norwegian
  ("new_faction_title_male_4_village", "Hersir {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_4_castle", "Jarl {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_4_town", "Hertogi {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_4_king", "Konungr {s0}{reg10?-{s61}:}"),

  ("new_faction_title_male_5", "Tigheam {s0}{reg10?-{s61}:}"), # Scots Gaelic
  ("new_faction_title_male_5_village", "Thegn {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_5_castle", "Iarla {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_5_town", "Diuc {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_5_king", "Righ {s0}{reg10?-{s61}:}"),

  ("new_faction_title_male_6", "Sayyid {s0}{reg10?-{s61}:}"), # Arabic
  ("new_faction_title_male_6_village", "Sheik {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_6_castle", "Quadi {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_6_town", "Mushir {s0}{reg10?-{s61}:}"),
  ("new_faction_title_male_6_king", "Sultan {s0}{reg10?-{s61}:}"),

  # equivalent for female character/wife and specific for landless unmarried daugther/sister
  ("new_faction_title_female_player", "Domina {s0}{reg10?-{s61}:}"), # Latin
  ("new_faction_title_female_player_village", "Baronessa {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_player_castle", "Comitessa {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_player_town", "Ducessa {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_player_queen", "Regina {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_player_unmarried", "Magistra {s0}{reg10?-{s61}:}"),

  ("new_faction_title_female_1", "Lady {s0}{reg10?-{s61}:}"), # English
  ("new_faction_title_female_1_village", "Baroness {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_1_castle", "Countess {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_1_town", "Duchess {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_1_queen", "Queen {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_1_unmarried", "Mistress {s0}{reg10?-{s61}:}"),

  ("new_faction_title_female_2", "Dvorianska {s0}{reg10?-{s61}:}"), # Russian 
  ("new_faction_title_female_2_village", "Posadnitsa {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_2_castle", "Boiaryna {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_2_town", "Kniaginia {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_2_queen", "Koroleva {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_2_unmarried", "Mestari {s0}{reg10?-{s61}:}"),

  ("new_faction_title_female_3", "Behi {s0}{reg10?-{s61}:}"), # Mongol/Chinese
  ("new_faction_title_female_3_village", "Darthun {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_3_castle", "Nohi {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_3_town", "Wathun {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_3_queen", "Khathun {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_3_unmarried", "Gongzhu {s0}{reg10?-{s61}:}"),

  ("new_faction_title_female_4", "Fru {s0}{reg10?-{s61}:}"), # Old norse/mid-norwegian
  ("new_faction_title_female_4_village", "Baronsfru {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_4_castle", "Greifynja {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_4_town", "Hertogafru {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_4_queen", "Drottning {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_4_unmarried", "Mesterinde {s0}{reg10?-{s61}:}"),

  ("new_faction_title_female_5", "Baintigheam {s0}{reg10?-{s61}:}"), # Scots Gaelic
  ("new_faction_title_female_5_village", "Bannthegn {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_5_castle", "Baniarla {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_5_town", "Bandiuc {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_5_queen", "Banrinn {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_5_unmarried", "Meistres {s0}{reg10?-{s61}:}"),

  ("new_faction_title_female_6", "Sayyida {s0}{reg10?-{s61}:}"), # Arabic
  ("new_faction_title_female_6_village", "Sheika {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_6_castle", "Qadiya {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_6_town", "Mushira {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_6_queen", "Sultana {s0}{reg10?-{s61}:}"),
  ("new_faction_title_female_6_unmarried", "Maulana {s0}{reg10?-{s61}:}"),
# Jrider -

# Jrider + TITLES v0.0 specialization strings, you can put these at the end of the file
  ("hero_titles_none", "Hero {s0}"),
  ("hero_titles_diplomat", "Diplomat {s0}"),
  ("hero_titles_tactician", "Chancellor {s0}"),
  ("hero_titles_scout", "Ranger {s0}"),
  ("hero_titles_physician", "Doctor {s0}"),
  ("hero_titles_trader", "Treasurer {s0}"),
  ("hero_titles_raider", "Raider {s0}"),
  ("hero_titles_slayer", "Slayer {s0}"),
  ("hero_titles_slaver", "Slaver {s0}"),
  ("hero_titles_party", "{s0}"),

  ("hero_specdesc_none", "none"),
  ("hero_specdesc_diplomat", "Diplomat (Persuasion)"),
  ("hero_specdesc_tactician", "Chancellor (Tactics, Engineer and Trainer)"),
  ("hero_specdesc_scout", "Ranger (Spotting, Tracking and Path finding)"),
  ("hero_specdesc_physician", "Doctor (Wound treatment, Surgery and First aid)"),
  ("hero_specdesc_trader", "Treasurer (Trading)"),
  ("hero_specdesc_diplomat", "Slayer (Weapon Master Power Draw Power Strike)"),
  ("hero_specdesc_tactician", "Slaver (Prisoner Management)"),
  ("hero_specdesc_scout", "Raider (Looting)"),

# Jrider -

# Jrider + TITLES v0.3 relation to ruler suffix, you can put these at the end of the file
  ("ruler_relation_mnus_100_ns", "Incensed"), # -100 Vengeful
  ("ruler_relation_mnus_80_ns",  "Resentful"), # -80 Vengeful/revengeful
  ("ruler_relation_mnus_60_ns",  "Resentful"), # -60 Hateful
  ("ruler_relation_mnus_40_ns",  "Malcontent"), # -40 Resentful
  ("ruler_relation_mnus_20_ns",  "Malcontent"), # -20 Grumbling
  ("ruler_relation_plus_0_ns",   "placeholder shouldn't appear"),# 0...19
  ("ruler_relation_plus_20_ns",  "Supportive"), # cooperative
  ("ruler_relation_plus_40_ns",  "Supportive"), # supportive
  ("ruler_relation_plus_60_ns",  "Faithful"), # gracious
  ("ruler_relation_plus_80_ns",  "Faithful"), # devoted
# Jrider -
  #KAOS  (POLITICAL)

# Lav modifications start (custom lord notes)
  ("lcn_faction", "He is loyal to {s41}."),
  ("lcn_stats", "Renown: {reg60}. Controversy: {reg61}."),
  ("lcn_prompt", "Enter your personal notes on {s41}:"),
# Lav modifications end (custom lord notes)

  ("key_0", "0"),
  ("key_1", "1"),
  ("key_2", "2"),
  ("key_3", "3"),
  ("key_4", "4"),
  ("key_5", "5"),
  ("key_6", "6"),
  ("key_7", "7"),
  ("key_8", "8"),
  ("key_9", "9"),
  ("key_a", "A"),
  ("key_b", "B"),
  ("key_c", "C"),
  ("key_d", "D"),
  ("key_e", "E"),
  ("key_f", "F"),
  ("key_g", "G"),
  ("key_h", "H"),
  ("key_i", "I"),
  ("key_j", "J"),
  ("key_k", "K"),
  ("key_l", "L"),
  ("key_m", "M"),
  ("key_n", "N"),
  ("key_o", "O"),
  ("key_p", "P"),
  ("key_q", "Q"),
  ("key_r", "R"),
  ("key_s", "S"),
  ("key_t", "T"),
  ("key_u", "U"),
  ("key_v", "V"),
  ("key_w", "W"),
  ("key_x", "X"),
  ("key_y", "Y"),
  ("key_z", "Z"),
]

from util_common import *

def modmerge_strings(orig_strings):
    # add remaining strings
    from util_common import add_objects
    num_appended, num_replaced, num_ignored = add_objects(orig_strings, strings)
    #print num_appended, num_replaced, num_ignored
	
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "strings"
        orig_strings = var_set[var_name_1]
        modmerge_strings(orig_strings)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)