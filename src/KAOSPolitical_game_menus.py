# POLITICAL (1.2) by Lazeras
# Released 1 December 2014
from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################


# Manualy all lines under the `game_menus` into the bottom of the module_game_menus at the bottom
game_menus = [
#######################################################################################################################
# REPLACED GAME MENUS
#######################################################################################################################

  (
    "start_character_1",mnf_disable_all_keys,
    "You were born years ago, in a land far away. Your father was...",
    "none",
    [
    (str_clear,s10),
    (str_clear,s11),
    (str_clear,s12),
    (str_clear,s13),
    (str_clear,s14),
    (str_clear,s15),
    ],
    [
    ("start_noble",[],"An impoverished noble.",[
      (assign,"$background_type",cb_noble),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@You came into the world a {reg3?daughter:son} of declining nobility,\
 owning only the house in which they lived. However, despite your family's hardships,\
 they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
  (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_merchant",[],"A travelling merchant.",[
      (assign,"$background_type",cb_merchant),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@You were born the {reg3?daughter:son} of travelling merchants,\
 always moving from place to place in search of a profit. Although your parents were wealthier than most\
 and educated you as well as they could, you found little opportunity to make friends on the road,\
 living mostly for the moments when you could sell something to somebody."),
  (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_guard",[],"A veteran warrior.",[
      (assign,"$background_type",cb_guard),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@As a child, your family scrabbled out a meagre living from your father's wages\
 as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an\
 education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
  (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_forester",[],"A hunter.",[
      (assign,"$background_type",cb_forester),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@{reg3?daughter:son}"),
      (str_store_string,s10,"@You were the {reg3?daughter:son} of a family who lived off the woods,\
 doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows,\
 even a spot of poaching whenever things got tight. Winter was never a good time for your family\
 as the cold took animals and people alike, but you always lived to see another dawn,\
 though your brothers and sisters might not be so fortunate."),
  (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_nomad",[],"A steppe nomad.",[
      (assign,"$background_type",cb_nomad),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@{reg3?daughter:son}"),
      (str_store_string,s10,"@You were a child of the steppe, born to a tribe of wandering nomads who lived\
 in great camps throughout the arid grasslands.\
 Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
 how to ride almost before you learned how to walk. "),
  (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_thief",[],"A thief.",[
      (assign,"$background_type",cb_thief),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@As the {reg3?daughter:son} of a thief, you had very little 'formal' education.\
 Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
 until you learned how to pick locks, all the way through your childhood.\
 Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
  (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_priest",[],"Priests.",[
      (assign,"$background_type",cb_priest),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@A {reg3?daughter:son} that nobody wanted, you were left to the church as a baby,\
 a foundling raised by the priests and nuns to their own traditions.\
 You were only one of many other foundlings and orphans, but you nonetheless received a lot of attention\
 as well as many years of study in the church library and before the altar. They taught you many things.\
 Gradually, faith became such a part of your life that it was no different from the blood coursing through your veins."),
  (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("go_back",[],"Go back",
     [(jump_to_menu,"mnu_start_game_1"),
    ]),
    ]
  ),



  (
    "start_character_2",0,
    "{s10}^^ You started to learn about the world almost as soon as you could walk and talk. You spent your early life as...",
    "none",
    [],
    [
      ("page",
        [
          (eq, "$background_type", cb_noble),
        ],
        "A page at a nobleman's court.",[
      (assign,"$background_answer_2", cb2_page),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you were sent to live in the court of one of the nobles of the land.\
 There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
 But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
 and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
  (jump_to_menu,"mnu_start_character_3"),
    ]),
      ("apprentice",
        [
          (this_or_next|eq, "$background_type", cb_thief),
          (this_or_next|eq, "$background_type", cb_forester),
          (this_or_next|eq, "$background_type", cb_guard),
          (eq, "$background_type", cb_merchant),
        ],
        "A craftsman's apprentice.",[
      (assign,"$background_answer_2", cb2_apprentice),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
 new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
 you wished to stay."),
  (jump_to_menu,"mnu_start_character_3"),
    ]),
      ("stockboy",
        [
          (this_or_next|eq, "$background_type", cb_thief),
          (this_or_next|eq, "$background_type", cb_merchant),
          (this_or_next|eq, "$background_type", cb_forester),
          (eq, "$background_type", cb_thief),
        ],
        "A shop assistant.",[
      (assign,"$background_answer_2",cb2_merchants_helper),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans.\
 You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd\
 got the better deal."),
  (jump_to_menu,"mnu_start_character_3"),
    ]),
      ("urchin",
        [
          (this_or_next|eq, "$background_type", cb_thief),
          (this_or_next|eq, "$background_type", cb_guard),
          (this_or_next|eq, "$background_type", cb_forester),
          (this_or_next|eq, "$background_type", cb_nomad),
          (eq, "$background_type", cb_thief),
        ],
        "A street urchin.",[
      (assign,"$background_answer_2",cb2_urchin),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you took to the streets, doing whatever you must to survive.\
 Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
 always one step ahead of the law and those who wished you ill."),
  (jump_to_menu,"mnu_start_character_3"),
    ]),
      ("nomad",
        [
          (this_or_next|eq, "$background_type", cb_thief),
          (this_or_next|eq, "$background_type", cb_guard),
          (this_or_next|eq, "$background_type", cb_merchant),
          (this_or_next|eq, "$background_type", cb_forester),
          (this_or_next|eq, "$background_type", cb_nomad),
          (eq, "$background_type", cb_thief),
        ],
        "A steppe child.",[
      (assign,"$background_answer_2",cb2_steppe_child),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you rode the great steppes on a horse of your own, learning the ways of the grass and the desert.\
 Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country.\
 Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}."),
  (jump_to_menu,"mnu_start_character_3"),
    ]),

      ("courtier",
        [
          (this_or_next|eq, "$background_type", cb_guard),
          (this_or_next|eq, "$background_type", cb_merchant),
          (eq, "$background_type", cb_noble),
        ],
        "Courtier.",[
      (assign,"$background_answer_2",6),
      (assign, reg3, "$character_gender"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@{reg3?girl:boy}"),
      (str_store_string,s11,"@As a {s12} growing out of childhood,\
 you spent much of your life at court, inserting yourself into the tightly-knit circles of nobility.\
 With the years you became more and more involved with the politics and intrigue demanded of a high-born {s13}.\
 You could not afford to remain a stranger to backstabbing and political violence, even if you wanted to."),
  (jump_to_menu,"mnu_start_character_3"),
    ]),

      ("noble",
        [
          (this_or_next|eq, "$background_type", cb_priest),
          (eq, "$background_type", cb_noble),
        ],
        "Noble in training.",[
      (assign,"$background_answer_2",7),
      (assign, reg3, "$character_gender"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@{reg3?girl:boy}"),
      (try_begin),
      (eq,"$character_gender",tf_male),
      (str_store_string,s11,"@As a {s12} growing out of childhood,\
 you were trained and educated to perform the duties and wield the rights of a noble landowner.\
 The managing of taxes and rents were equally important in your education as diplomacy and even\
 personal defence. You learned everything you needed to become a lord of your own hall."),
      (else_try),
      (str_store_string,s11,"@As a {s12} growing out of childhood,\
 you were trained and educated to the duties of a noble {s13}. You learned much about the household arts,\
 but even more about diplomacy and decorum, and all the things that a future husband might choose to speak of.\
 Truly, you became every inch as shrewd as any lord, though it would be rude to admit it aloud."),
      (try_end),
  (jump_to_menu,"mnu_start_character_3"),
    ]),

      ("acolyte",
        [
          (this_or_next|eq, "$background_type", cb_thief),
          (this_or_next|eq, "$background_type", cb_nomad),
          (eq, "$background_type", cb_priest),
        ],
        "Cleric acolyte.",[
    (assign,"$background_answer_2",8),
      (assign, reg3, "$character_gender"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@{reg3?girl:boy}"),
      (str_store_string,s11,"@As a {s12} growing out of childhood,\
 you became an acolyte in the church, the lowest rank on the way to priesthood.\
 Years of rigorous learning and hard work followed. You were one of several acolytes,\
 performing most of the menial labour in the church in addition to being trained for more holy tasks.\
 On the night of your adulthood you were allowed to conduct your first service.\
 After that you were no longer an acolyte {s12}, but a {s13} waiting to take your vows into the service of God."),
  (jump_to_menu,"mnu_start_character_3"),
    ]),
      ("go_back",[],"Go back.",
     [(jump_to_menu,"mnu_start_character_1"),
    ]),
    ]
  ),



  (
    "start_character_3",mnf_disable_all_keys,
    "{s11}^^ Then, as a young adult, life changed as it always does. You became...",
    "none",
    [(assign, reg3, "$character_gender"),],
    [
      ("bravo",
        [

        ],
        "A travelling bravo.",[
        (assign,"$background_answer_3",1),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You left your old life behind to travel the roads as a mercenary, a bravo, guarding caravans for coppers\
 or bashing in heads for silvers. You became a {s14} of the open road, working with bandits as often as against.\
 Going from fight to fight, you grew experienced at battle, and you learned what it was to kill."),
  (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("merc",
        [
        ],
        "A sellsword in foreign lands.",[
        (assign,"$background_answer_3",2),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You signed on with a mercenary company and travelled far from your home. The life you found was rough and\
 ready, marching to the beat of strange drums and learning unusual ways of fighting.\
 There were men who taught you how to wield any weapon you desired, and plenty of battles to hone your skills.\
 You were one of the charmed few who survived through every campaign in which you marched."),
  (jump_to_menu,"mnu_start_character_4"),
        ]),

       ("squire",
        [
        (eq,"$character_gender",tf_male),
          (this_or_next|eq, "$background_answer_2", cb2_page),
          (this_or_next|eq, "$background_answer_2", 7),
          (eq, "$background_answer_2", 6),
        ],
        "A squire.",[
        (assign,"$background_answer_3",cb3_squire),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 When you were named squire to a noble at court, you practiced long hours with weapons,\
 learning how to deal out hard knocks and how to take them, too.\
 You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals.\
 But in addition to learning the chivalric ideal, you also learned about the less uplifting side\
 -- old warriors' stories of ruthless power politics, of betrayals and usurpations,\
 of men who used guile as well as valor to achieve their aims."),
  (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("lady",
        [
        (eq,"$character_gender",tf_female),
          (this_or_next|eq, "$background_answer_2", cb2_page),
          (this_or_next|eq, "$background_type", cb_noble),
          (eq, "$background_type", 7),
        ],
        "A lady-in-waiting.",[
        (assign,"$background_answer_3",cb3_lady_in_waiting),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things,\
 the wives and mistresses of noble men as well as maidens who had yet to find a husband.\
 However, even here you found politics at work as the ladies schemed for prominence and fought each other\
 bitterly to catch the eye of whatever unmarried man was in fashion at court.\
 You soon learned ways of turning these situations and goings-on to your advantage. With it came the\
 realisation that you yourself could wield great influence in the world, if only you applied yourself\
 with a little bit of subtlety."),
  (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("student",
        [
        ],
        "A university student.",[
        (assign,"$background_answer_3",cb3_student),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 You found yourself as a student in the university of one of the great cities,\
 where you studied theology, philosophy, and medicine.\
 But not all your lessons were learned in the lecture halls.\
 You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight.\
 However, you certainly were able to observe how a broken jaw is set,\
 or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),
  (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("peddler",
        [
          (this_or_next|eq, "$background_answer_2", cb2_apprentice),
          (this_or_next|eq, "$background_answer_2", cb2_urchin),
          (eq, "$background_answer_2", cb2_merchants_helper),
        ],
        "A goods peddler.",[
        (assign,"$background_answer_3",cb3_peddler),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 Heeding the call of the open road, you travelled from village to village buying and selling what you could.\
 It was not a rich existence, but you became a master at haggling even the most miserly elders into\
 giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
  (jump_to_menu,"mnu_start_character_4"),
        ]),

      ("craftsman",
        [
          (this_or_next|eq, "$background_answer_2", cb2_apprentice),
          (this_or_next|eq, "$background_answer_2", cb2_urchin),
          (eq, "$background_answer_2", cb2_merchants_helper),
        ],
        "A smith.",[
        (assign,"$background_answer_3", cb3_craftsman),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
 As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
 With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
  (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("poacher",
        [
          (this_or_next|eq, "$background_answer_2", cb2_steppe_child),
          (this_or_next|eq, "$background_answer_2", cb2_urchin),
          (eq, "$background_answer_2", cb2_merchants_helper),
        ],
        "A game poacher.",[
        (assign,"$background_answer_3", cb3_poacher),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
 and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
 the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
 firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
  (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("preacher",
        [
          (eq, "$background_answer_2", 8),
        ],
        "Itinerant preacher.",[
        (assign,"$background_answer_3",6),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You packed your few belongings and went out into the world to spread the word of God. You preached to\
 anyone who would listen, and impressed many with the passion of your sermons. Though you had taken a vow\
 to remain in poverty through your itinerant years, you never lacked for food, drink or shelter; the\
 hospitality of the peasantry was always generous to a rising {s13} of God."),
  (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("go_back",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_2"),
        ]
       ),
    ]
  ),

  (
    "start_character_4",mnf_disable_all_keys,
    "{s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was...",
    #Finally, what made you decide to strike out on your own as an adventurer?",
    "none",
    [],
    [
      ("revenge",[],"Personal revenge.",[
        (assign,"$background_answer_4", cb4_revenge),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
 You want vengeance. You want justice. What was done to you cannot be undone,\
 and these debts can only be paid in blood..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("death",[],"The loss of a loved one.",[
        (assign,"$background_answer_4",cb4_loss),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
 painful. Perhaps your new life will let you forget,\
 or honour the name that you can no longer bear to speak..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("wanderlust",[],"Wanderlust.",[
        (assign,"$background_answer_4",cb4_wanderlust),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
 wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
 freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("fervor",
        [
          (this_or_next|eq, "$background_type", cb_priest),
          (this_or_next|eq, "$background_answer_2", 8),
          (eq, "$background_answer_3", 6),
        ],
        "Religious fervor.",[
        (assign,"$background_answer_4",4),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 Regardless, the intense faith burning in your soul would not let you find peace in any single place.\
 There were others in the world, souls to be washed in the light of God. Now you preach wherever you go,\
 seeking to bring salvation and revelation to the masses, be they faithful or pagan. They will all know the\
 glory of God by the time you're done..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("disown",[],"Being forced out of your home.",[
        (assign,"$background_answer_4",cb4_disown),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
 now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
     ("greed",[],"Lust for money and power.",[
        (assign,"$background_answer_4",cb4_greed),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 To everyone else, it's clear that you're now motivated solely by personal gain.\
 You want to be rich, powerful, respected, feared.\
 You want to be the one whom others hurry to obey.\
 You want people to know your name, and tremble whenever it is spoken.\
 You want everything, and you won't let anyone stop you from having it..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("go_back",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_3"),
        ]
       ),
    ]
  ),









  (
 "choose_skill",mnf_disable_all_keys,
    "{s13}", 
    "none",
    [
        (assign,"$current_string_reg",10),
        (assign, ":difficulty", 0),
       
       (try_begin),
        (eq, "$character_gender", tf_female),
        (str_store_string, s14, "str_woman"),
        (val_add, ":difficulty", 1),
       (else_try),  
        (str_store_string, s14, "str_man"),
       (try_end),
      
       (try_begin),
            (this_or_next|eq,"$background_type",cb_king),
            (this_or_next|eq,"$background_type",cb_prince),
            (this_or_next|eq,"$background_type",cb_vassal),
            (eq,"$background_type",cb_noble),
        (str_store_string, s15, "str_noble"),
        (val_sub, ":difficulty", 1),
       (else_try),
        (str_store_string, s15, "str_common"),
       (try_end),
       
       (try_begin),
        (eq, ":difficulty", -1),
        (str_store_string, s16, "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
       (else_try),
        (eq, ":difficulty", 0),
        (str_store_string, s16, "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
       (else_try),
        (eq, ":difficulty", 1),
        (str_store_string, s16, "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
       (try_end),
  ],
    [
##      ("start_swordsman",[],"Swordsmanship.",[
##        (assign, "$starting_skill", 1),
##        (str_store_string, s14, "@You are particularly talented at swordsmanship."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_archer",[],"Archery.",[
##        (assign, "$starting_skill", 2),
##        (str_store_string, s14, "@You are particularly talented at archery."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_medicine",[],"Medicine.",[
##        (assign, "$starting_skill", 3),
##        (str_store_string, s14, "@You are particularly talented at medicine."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
      ("begin_adventuring",[],"Become an adventurer and ride to your destiny.",[
           (set_show_messages, 0),
           (try_begin),
             (eq,"$character_gender",0),
             (troop_raise_attribute, "trp_player",ca_strength,1),
             (troop_raise_attribute, "trp_player",ca_charisma,1),
           (else_try),
             (troop_raise_attribute, "trp_player",ca_agility,1),
             (troop_raise_attribute, "trp_player",ca_intelligence,1),
           (try_end),

           (troop_raise_attribute, "trp_player",ca_strength,1),
           (troop_raise_attribute, "trp_player",ca_agility,1),
           (troop_raise_attribute, "trp_player",ca_charisma,1),
           
           (troop_raise_skill, "trp_player","skl_leadership",1),
           (troop_raise_skill, "trp_player","skl_riding",1),
##           (try_begin),
##             (eq, "$starting_skill", 1),
##             (troop_raise_attribute, "trp_player",ca_agility,1),
##             (troop_raise_attribute, "trp_player",ca_strength,1),
##             (troop_raise_skill, "trp_player",skl_power_strike,2),
##             (troop_raise_proficiency, "trp_player",0,30),
##             (troop_raise_proficiency, "trp_player",1,20),
##           (else_try),
##             (eq, "$starting_skill", 2),
##             (troop_raise_attribute, "trp_player",ca_strength,2),
##             (troop_raise_skill, "trp_player",skl_power_draw,2),
##             (troop_raise_proficiency, "trp_player",3,50),
##           (else_try),
##             (troop_raise_attribute, "trp_player",ca_intelligence,1),
##             (troop_raise_attribute, "trp_player",ca_charisma,1),
##             (troop_raise_skill, "trp_player",skl_first_aid,1),
##             (troop_raise_skill, "trp_player",skl_wound_treatment,1),
##             (troop_add_item, "trp_player","itm_winged_mace",0),
##             (troop_raise_proficiency, "trp_player",0,15),
##             (troop_raise_proficiency, "trp_player",1,15),
##             (troop_raise_proficiency, "trp_player",2,15),
##           (try_end),
      (try_begin),      
        (eq,"$background_type",cb_king),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,3),
        (troop_raise_skill, "trp_player",skl_riding,3),
        (troop_raise_skill, "trp_player",skl_tactics,3),
        (troop_raise_skill, "trp_player",skl_leadership,3),
        (troop_raise_skill, "trp_player", skl_power_strike,1),
        (troop_raise_skill, "trp_player", skl_ironflesh,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,45),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,45),
        (troop_add_item, "trp_player","itm_leather_gloves",imod_battered),
        (troop_add_item, "trp_player","itm_arming_cap",imod_battered),
        (troop_add_item, "trp_player","itm_courtly_outfit",imod_battered),
        (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),    
        (troop_set_slot, "trp_player", slot_troop_renown, 200),
        (call_script, "script_change_player_honor", 30),
        (troop_add_gold, "trp_player", 1000),

        (party_add_xp, "p_main_party", 6000),
  (else_try),       
        (eq,"$background_type",cb_vassal),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_riding,2),
        (troop_raise_skill, "trp_player",skl_tactics,2),
        (troop_raise_skill, "trp_player",skl_leadership,3),
        (troop_raise_skill, "trp_player", skl_power_strike,1),
        (troop_raise_skill, "trp_player", skl_ironflesh,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,25),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,25),
        (troop_add_item, "trp_player","itm_leather_gloves",imod_battered),
        (troop_add_item, "trp_player","itm_arming_cap",imod_battered),
        (troop_add_item, "trp_player","itm_courtly_outfit",imod_battered),
        (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),
        (troop_set_slot, "trp_player", slot_troop_renown, 150),
        (call_script, "script_change_player_honor", 20),
        (troop_add_gold, "trp_player", 500),

        (party_add_xp, "p_main_party", 3000),
  (else_try),
        (this_or_next|eq,"$background_type",cb_prince),
        (eq,"$background_type",cb_vassal),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_riding,2),
        (troop_raise_skill, "trp_player",skl_tactics,2),
        (troop_raise_skill, "trp_player",skl_leadership,3),
        (troop_raise_skill, "trp_player", skl_power_strike,1),
        (troop_raise_skill, "trp_player", skl_ironflesh,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,25),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,25),
        (troop_add_item, "trp_player","itm_leather_gloves",imod_battered),
        (troop_add_item, "trp_player","itm_arming_cap",imod_battered),
        (troop_add_item, "trp_player","itm_courtly_outfit",imod_battered),
        (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),
        (troop_set_slot, "trp_player", slot_troop_renown, 150),
        (call_script, "script_change_player_honor", 20),
        (troop_add_gold, "trp_player", 2500),

        (party_add_xp, "p_main_party", 4500),
  (else_try),
        (eq,"$background_type",cb_noble),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_skill, "trp_player",skl_weapon_master,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_tactics,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_polearm,10),
        (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),
        (troop_set_slot, "trp_player", slot_troop_renown, 100),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb_noble),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_skill, "trp_player",skl_riding,2),
        (troop_raise_skill, "trp_player",skl_first_aid,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb_merchant),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_trade,2),
        (troop_raise_skill, "trp_player",skl_inventory_management,2),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
        #TRADE LEDGER
        #(troop_add_item, "trp_player","itm_book_trade_ledger",0),
        #TRADE LEDGER 
        (troop_add_gold, "trp_player", 250),
        (troop_set_slot, "trp_player", slot_troop_renown, 20),
      (else_try),
        (eq,"$background_type",cb_guard),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player","skl_ironflesh",1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),
        (troop_raise_skill, "trp_player","skl_trainer",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,20),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        (troop_add_item, "trp_player","itm_tab_shield_kite_b",imod_battered),
        (troop_add_gold, "trp_player", 50),
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
      (else_try),
        (eq,"$background_type",cb_forester),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,2),
        (troop_raise_skill, "trp_player","skl_power_draw",1),
        (troop_raise_skill, "trp_player","skl_tracking",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (troop_raise_skill, "trp_player","skl_athletics",1),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_archery,30),
        (troop_add_gold, "trp_player", 30),
      (else_try),
        (eq,"$background_type",cb_nomad),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_power_draw",1),
        (troop_raise_skill, "trp_player","skl_horse_archery",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_riding",2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_archery,30),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        (troop_add_item, "trp_player","itm_tab_shield_small_round_a",imod_battered),
        (troop_add_gold, "trp_player", 15),
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
      (else_try),
        (eq,"$background_type",cb_nomad),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_wound_treatment",1),
        (troop_raise_skill, "trp_player","skl_first_aid",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_riding",2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,5),
        (troop_raise_proficiency, "trp_player",wpt_archery,20),
        (troop_raise_proficiency, "trp_player",wpt_throwing,5),
        (troop_add_item, "trp_player","itm_tab_shield_small_round_a",imod_battered),
        (troop_add_gold, "trp_player", 20),
      (else_try),
        (eq,"$background_type",cb_thief),
        (troop_raise_attribute, "trp_player",ca_agility,3),
        (troop_raise_skill, "trp_player","skl_athletics",2),
        (troop_raise_skill, "trp_player","skl_power_throw",1),
        (troop_raise_skill, "trp_player","skl_inventory_management",1),
        (troop_raise_skill, "trp_player","skl_looting",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_throwing,20),
        (troop_add_item, "trp_player","itm_throwing_knives",0),
        (troop_add_gold, "trp_player", 25),
      (else_try),
        (eq,"$background_type",cb_priest),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
        (troop_raise_proficiency, "trp_player",0,10),
        (troop_add_item, "trp_player","itm_robe",0),
        (troop_add_item, "trp_player","itm_wrapping_boots",0),
        (troop_add_item, "trp_player","itm_club",0),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
        (troop_add_item, "trp_player","itm_sumpter_horse",0),
        (troop_add_gold, "trp_player", 10),
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
      (try_end),

    (try_begin),
        (eq,"$background_answer_2",cb2_page),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,5),
    (else_try),
        (eq,"$background_answer_2",cb2_apprentice),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_skill, "trp_player","skl_engineer",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
    (else_try),
        (eq,"$background_answer_2",cb2_urchin),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (troop_raise_skill, "trp_player","skl_looting",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_throwing,5),
    (else_try),
        (eq,"$background_answer_2",cb2_steppe_child),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player","skl_horse_archery",1),
        (troop_raise_skill, "trp_player","skl_power_throw",1),
        (troop_raise_proficiency, "trp_player",wpt_archery,15),
        (call_script,"script_change_troop_renown", "trp_player", 5),
    (else_try),
        (eq,"$background_answer_2",cb2_merchants_helper),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player","skl_inventory_management",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
  (else_try),
        (eq,"$background_answer_2",5),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_athletics,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_proficiency, "trp_player",1,5),
        (troop_raise_proficiency, "trp_player",2,5),
        (call_script,"script_change_troop_renown", "trp_player", 15),
  (else_try),
        (eq,"$background_answer_2",6),
        (troop_raise_attribute, "trp_player",ca_charisma,3),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player",skl_weapon_master,1),
        (troop_raise_proficiency, "trp_player",0,15),
        (troop_raise_proficiency, "trp_player",2,10),
        (troop_raise_proficiency, "trp_player",4,10),
        (call_script,"script_change_troop_renown", "trp_player", 20),
  (else_try),
        (eq,"$background_answer_2",7),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_tactics,1),
        (troop_raise_proficiency, "trp_player",0,10),
        (troop_raise_proficiency, "trp_player",1,10),
        (call_script,"script_change_troop_renown", "trp_player", 15),
  (else_try),
        (eq,"$background_answer_2",8),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_surgery,1),
        (troop_raise_skill, "trp_player",skl_first_aid,1),
        (troop_raise_proficiency, "trp_player",2,10),
        (call_script,"script_change_troop_renown", "trp_player", 5),
  (try_end),

  (try_begin),
        (eq,"$background_answer_3",1),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_shield,1),
        (troop_add_gold, "trp_player", 10),
        (troop_add_item, "trp_player","itm_scimitar",0),
        (troop_add_item, "trp_player","itm_wooden_shield",imod_battered),
        (troop_add_item, "trp_player","itm_leather_jerkin",imod_ragged),
        (troop_add_item, "trp_player","itm_leather_boots",imod_tattered),
           
        (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        (troop_add_item, "trp_player","itm_bolts",0),
        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
        (troop_add_gold, "trp_player", 20),

        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,30),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,30),

    (else_try),
        (eq,"$background_answer_3",2),
        (troop_raise_attribute, "trp_player",ca_agility,2),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_shield",1),
        (troop_raise_skill, "trp_player","skl_tracking",1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (try_begin),
        (this_or_next|player_has_item,"itm_hide_boots"),
        (troop_has_item_equipped,"trp_player","itm_hide_boots"),
        (troop_remove_item, "trp_player","itm_hide_boots"),
        (try_end),
        (troop_add_item, "trp_player","itm_khergit_guard_helmet",imod_crude),
        (troop_add_item, "trp_player","itm_khergit_guard_armor",imod_crude),
        (troop_add_item, "trp_player","itm_mail_chausses",imod_crude),
        (troop_add_item, "trp_player","itm_sword_khergit_1",imod_plain),
        (troop_add_item, "trp_player","itm_dried_meat",0),
        (troop_add_item, "trp_player","itm_hunting_bow",0),
        (troop_add_item, "trp_player","itm_barbed_arrows",0),
        (troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
        (troop_add_gold, "trp_player", 20),

        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,40),
    (else_try),
        (eq,"$background_answer_3",cb3_poacher),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player","skl_power_draw",1),
        (troop_raise_skill, "trp_player","skl_tracking",1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (troop_raise_skill, "trp_player","skl_athletics",1),
        (troop_add_gold, "trp_player", 10),
        (troop_raise_proficiency, "trp_player",wpt_polearm,10),
        (troop_raise_proficiency, "trp_player",wpt_archery,35),
           
        (troop_add_item, "trp_player","itm_axe",imod_chipped),
        (troop_add_item, "trp_player","itm_rawhide_coat",0),
        (troop_add_item, "trp_player","itm_hide_boots",0),
        (troop_add_item, "trp_player","itm_hunting_bow",0),
        (troop_add_item, "trp_player","itm_barbed_arrows",0),
        (troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
        (troop_add_item, "trp_player","itm_dried_meat",0),
        (troop_add_item, "trp_player","itm_dried_meat",0),
        (troop_add_item, "trp_player","itm_furs",0),
        (troop_add_item, "trp_player","itm_furs",0),
    (else_try),
        (eq,"$background_answer_3",cb3_craftsman),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),

        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_engineer",1),
        (troop_raise_skill, "trp_player","skl_tactics",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        (troop_add_gold, "trp_player", 100),
        (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        (troop_add_item, "trp_player","itm_coarse_tunic",0),  
        (troop_add_item, "trp_player","itm_sword_medieval_b", imod_balanced),
        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        (troop_add_item, "trp_player","itm_bolts",0),
        (troop_add_item, "trp_player","itm_tools",0),
        (troop_add_item, "trp_player","itm_saddle_horse",0),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_peddler),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_riding",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_inventory_management",1),
        (troop_add_item, "trp_player","itm_leather_gloves",imod_plain),
        (troop_add_gold, "trp_player", 90),
        (troop_raise_proficiency, "trp_player",wpt_polearm,15),
        (troop_add_item, "trp_player","itm_leather_jacket",0),
        (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        (troop_add_item, "trp_player","itm_fur_hat",0),
        (troop_add_item, "trp_player","itm_staff",0),
        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        (troop_add_item, "trp_player","itm_bolts",0),
        (troop_add_item, "trp_player","itm_saddle_horse",0),
        (troop_add_item, "trp_player","itm_sumpter_horse",0),
        (troop_add_item, "trp_player","itm_linen",0),
        (troop_add_item, "trp_player","itm_pottery",0),
        (troop_add_item, "trp_player","itm_wool",0),
        (troop_add_item, "trp_player","itm_wool",0),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",6),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_skill, "trp_player",skl_first_aid,1),
        (troop_raise_skill, "trp_player",skl_surgery,2),
        (troop_add_item, "trp_player","itm_leather_gloves",imod_ragged),
        (troop_add_item, "trp_player","itm_quarter_staff",imod_heavy),
        (troop_add_item, "trp_player","itm_common_hood",0),
        (troop_add_item, "trp_player","itm_robe",0),
        (troop_add_item, "trp_player","itm_ankle_boots",0),
        (troop_add_item, "trp_player","itm_saddle_horse",0),
        (troop_add_gold, "trp_player", 15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,25),
    (else_try),
        (eq,"$background_answer_3",cb3_troubadour),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_add_gold, "trp_player", 80),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,25),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
        (troop_add_item, "trp_player","itm_tabard",imod_sturdy),
        (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        (troop_add_item, "trp_player","itm_hunting_crossbow", 0),
        (troop_add_item, "trp_player","itm_bolts", 0),
        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_squire),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player","skl_riding",1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),
        (troop_add_gold, "trp_player", 20),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,30),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,30),
        (troop_raise_proficiency, "trp_player",wpt_polearm,30),
        (troop_raise_proficiency, "trp_player",wpt_archery,10),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        (troop_add_item, "trp_player","itm_leather_jerkin",imod_ragged),
        (troop_add_item, "trp_player","itm_leather_boots",imod_tattered),
        (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        (troop_add_item, "trp_player","itm_bolts",0),
        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_lady_in_waiting),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player","skl_persuasion",2),
        (troop_raise_skill, "trp_player","skl_riding",1),
        (troop_raise_skill, "trp_player","skl_wound_treatment",1),
        (troop_add_item, "trp_player","itm_dagger", 0),
        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        (troop_add_item, "trp_player","itm_bolts",0),
        (troop_add_item, "trp_player","itm_courser", imod_spirited),
        (troop_add_item, "trp_player","itm_woolen_hood",imod_sturdy),
        (troop_add_item, "trp_player","itm_woolen_dress",imod_sturdy),
        (troop_add_gold, "trp_player", 100),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,15),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_student),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_surgery",1),
        (troop_raise_skill, "trp_player","skl_wound_treatment",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),
        (troop_add_gold, "trp_player", 80),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,20),
        (troop_add_item, "trp_player","itm_linen_tunic",imod_sturdy),
        (troop_add_item, "trp_player","itm_woolen_hose",0),
        (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        (troop_add_item, "trp_player","itm_hunting_crossbow", 0),
        (troop_add_item, "trp_player","itm_bolts", 0),
        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
        (store_random_in_range, ":book_no", books_begin, books_end),
        (troop_add_item, "trp_player",":book_no",0),
    (try_end),

      (try_begin),
        (eq,"$background_answer_4",cb4_revenge),
        (troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
      (else_try),
        (eq,"$background_answer_4",cb4_loss),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_skill, "trp_player","skl_ironflesh",1),
      (else_try),
        (eq,"$background_answer_4",cb4_wanderlust),
        (troop_raise_attribute, "trp_player",ca_agility,2),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (else_try),
        (eq,"$background_answer_4",4),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_wound_treatment,2),
        (troop_raise_proficiency, "trp_player",5,10),
      (else_try),
        (eq,"$background_answer_4",cb4_disown),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
      (else_try),
        (eq,"$background_answer_4",cb4_greed),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_looting",1),
      (try_end),


           (try_begin),
             (this_or_next|eq, "$background_type", cb_king),
             (this_or_next|eq, "$background_type", cb_vassal),
             (eq, "$background_type", cb_noble),
             (jump_to_menu, "mnu_auto_return"),
#normal_banner_begin
             (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#             (start_presentation, "prsnt_custom_banner"),
           (else_try),
             (change_screen_return, 0),
           (try_end),
           (set_show_messages, 1),
        ]),
      ("go_back_dot",[],"Go back.",[
        (jump_to_menu,"mnu_start_character_4"),
        ]),
    ]
  ),


#######################################################################################################################
# REPLACED GAME MENUS
#######################################################################################################################

  #KAOS  (POLITICAL)
  ("camp_political",0,
   "Choose an option:",
   "none",
   [
     ],
    [
		#My opinion is that it should be renown-dependent...
   		("action_change_party_name",
       	[

          (eq, "$kaos_use_custom_name", 1),
       		#(troop_slot_ge, "trp_player", slot_troop_renown, 150),
       	], 
       	"Change your party's name.",
	       	[
	       		(start_presentation, "prsnt_set_party_name")
	       	]
       	),

      ("action_rename_kingdom",
       [
         (eq, "$players_kingdom_name_set", 1),
         (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
         (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
         ],"Rename your kingdom.",
       [
       		(start_presentation, "prsnt_name_kingdom"),
        ]
       ),

      ("action_modify_banner",
        [
          (troop_slot_ge, "trp_player", slot_troop_renown, 300),
        ],"{!}Modify your banner.",
        [
           (start_presentation, "prsnt_banner_selection"),
        ]
       ),

       ("action_change_vassal_title",
       [
           (eq, "$kaos_use_custom_title", 1),
           #(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
           #(faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
       ],"Change your vassals' title of nobility.",
       [
       		(start_presentation, "prsnt_set_vassal_title"),
        ]
       ),

      ("action_modify_color",[],"Modify Factions Color's.",
       [
           (start_presentation, "prsnt_change_all_factions_color"),
           #(start_presentation, "prsnt_custom_banner"),
        ]
       ),

      ("action_modify_political",[],"Modify Political Options.",
       [
           (start_presentation, "prsnt_kaos_political_options"),
           #(start_presentation, "prsnt_custom_banner"),
        ]
       ),


      ("pol_action_camp",[],"Back to camp menu.",
       [
        (jump_to_menu, "mnu_camp"),
       ]
       ),
    ]
  ),
  #KAOS  (POLITICAL)

  ("start_vassal_1",0, "{s10}^^ The old debt was owed to your father by ...", "none",
    [],
  [
      ("Swadia",[
        ],"King Harlaus",[

       (assign,"$kaos_kings_vassal", 1),
       (assign, reg3, "$character_gender"),
       (str_store_string,s11,"@Because of the old debt King Harlaus owed your father he has taken you in as a vassal of Kingdom of Swadia"),         
       #(call_script, "script_player_join_faction", "fac_kingdom_1"),
      #trp_kingdom_1_lord
      #(jump_to_menu,"mnu_choose_skill"),
      (jump_to_menu,"mnu_start_character_4"),
    ]),

    ("Vaegirs",[
        ],"King Yaroglek",[
       (assign,"$kaos_kings_vassal", 2),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@Because of the old debt King Yaroglek owed your father he has taken you in as a vassal of Kingdom of Vaegirs"),        
    (jump_to_menu,"mnu_start_character_4"),
    ]),

    ("Khanate",[
        ],"Sanjar Khan",[

       (assign,"$kaos_kings_vassal", 3),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@Because of the old debt Sanjar Khan owed your father he has taken you in as a vassal of Khergit Khanate"),        
    (jump_to_menu,"mnu_start_character_4"),
    ]),

    ("Nords",[
        ],"King Ragnar",[
       (assign,"$kaos_kings_vassal", 4),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@Because of the old debt King Ragnar owed your father he has taken you in as a vassal of Kingdom of Nords"),        
    (jump_to_menu,"mnu_start_character_4"),
    ]),

      ("Rhodoks",[
        ],"King Graveth",[
       (assign,"$kaos_kings_vassal", 5),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@Because of the old debt King Graveth owed your father he has taken you in as a vassal of Kingdom of Rhodoks"),        
    (jump_to_menu,"mnu_start_character_4"),
    ]),

  ("Sultanate",[
        ],"Sultan Hakim",[
       (assign,"$kaos_kings_vassal", 6),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@Because of the old debt Sultan Hakim owed your father he has taken you in as a vassal of Sarranid Sultanate"),        
    (jump_to_menu,"mnu_start_character_4"),
    ]),
  ("go_back",[],"Go back.",
    [
    (jump_to_menu,"mnu_start_character_1"),
    ]),
   ]),





  ("start_prince_1",0, "{s10}^^ You have returned home to your father ...", "none",
    [],
  [
      ("Swadia",[
        ],"King Harlaus",[

       (assign,"$kaos_kings_prince", 1),
       (assign, reg3, "$character_gender"),
      (jump_to_menu,"mnu_start_character_4"),
    ]),

    ("Vaegirs",[
        ],"King Yaroglek",[
       (assign,"$kaos_kings_prince", 2),
      (assign, reg3, "$character_gender"),
    (jump_to_menu,"mnu_start_character_4"),
    ]),

    ("Khanate",[
        ],"Sanjar Khan",[

       (assign,"$kaos_kings_prince", 3),
      (assign, reg3, "$character_gender"),
    (jump_to_menu,"mnu_start_character_4"),
    ]),

    ("Nords",[
        ],"King Ragnar",[
       (assign,"$kaos_kings_prince", 4),
      (assign, reg3, "$character_gender"),
    (jump_to_menu,"mnu_start_character_4"),
    ]),

      ("Rhodoks",[
        ],"King Graveth",[
       (assign,"$kaos_kings_prince", 5),
      (assign, reg3, "$character_gender"),
    (jump_to_menu,"mnu_start_character_4"),
    ]),

  ("Sultanate",[
        ],"Sultan Hakim",[
       (assign,"$kaos_kings_prince", 6),
      (assign, reg3, "$character_gender"),
    (jump_to_menu,"mnu_start_character_4"),
    ]),
  ("go_back",[],"Go back.",
    [
    (jump_to_menu,"mnu_start_character_1"),
    ]),
   ]),





  ("start_king_1",0, "{s10}^^ Your fathers kingdom was...", "none",
    [],
  [
      ("Swadia",[
        ],"Your father was King Harlaus",[
       (assign, reg3, "$character_gender"),
       (assign, "$kaos_kings_kingdom", 1),
       (str_store_string,s11,"@You are your fathers {reg3?daughter:son}, and the death of of your father has left you to fill his spot as leader of the Kingdom of Swadia"),
      (jump_to_menu,"mnu_choose_skill"),
    ]),

    ("Vaegirs",[
        ],"Your father was King Yaroglek",[
      (assign, reg3, "$character_gender"),
       (assign, "$kaos_kings_kingdom", 2),
      (str_store_string,s11,"@You are your fathers {reg3?daughter:son}, and the death of of your father has left you to fill his spot as leader of the Kingdom of Vaegirs"),
    (jump_to_menu,"mnu_choose_skill"),
    ]),

    ("Khanate",[
        ],"Your father was Sanjar Khan",[
      (assign, reg3, "$character_gender"),
       (assign, "$kaos_kings_kingdom", 3),
      (str_store_string,s11,"@You are your fathers {reg3?daughter:son}, and the death of of your father has left you to fill his spot as leader of the Khergit Khanate"),
    (jump_to_menu,"mnu_choose_skill"),
    ]),

    ("Nords",[
        ],"Your father was King Ragnar",[
      (assign, reg3, "$character_gender"),
       (assign, "$kaos_kings_kingdom", 4),
      (str_store_string,s11,"@You are your fathers {reg3?daughter:son}, and the death of of your father has left you to fill his spot as leader of the Kingdom of Nords"),
    (jump_to_menu,"mnu_choose_skill"),
    ]),

      ("Rhodoks",[
        ],"Your father was King Graveth",[
      (assign, reg3, "$character_gender"),
       (assign, "$kaos_kings_kingdom", 5),
      (str_store_string,s11,"@You are your fathers {reg3?daughter:son}, and the death of of your father has left you to fill his spot as leader of the Kingdom of Rhodoks"),
    (jump_to_menu,"mnu_choose_skill"),
    ]),

  ("Sultanate",[
        ],"Your father was Sultan Hakim",[
      (assign, reg3, "$character_gender"),
       (assign, "$kaos_kings_kingdom", 6),
      (str_store_string,s11,"@You are your fathers {reg3?daughter:son}, and the death of of your father has left you to fill his spot as leader of the Sarranid Sultanate"),
    (jump_to_menu,"mnu_choose_skill"),
    ]),

  ("go_back",[],"Go back.",
    [
    (jump_to_menu,"mnu_start_character_1"),
    ]),
   ]),

  
#rubik Source code of Restoration
 # restoration begin
  (
    "notification_kingdom_restoration",0,
    "Restoration^^{s11} of {s13} gets a fief from {s12}, {s13} is restored! All lords of {s13} include {s14} will come back to {s13} later.",
    "none",
    [
      (troop_get_slot, ":original_faction", "$g_notification_menu_var1", slot_troop_original_faction),
      (faction_get_slot, ":original_king", ":original_faction", slot_faction_leader),
      (str_store_troop_name, s11, "$g_notification_menu_var1"),
      (str_store_faction_name, s12, "$g_notification_menu_var2"),
      (str_store_faction_name, s13, ":original_faction"),
      (str_store_troop_name, s14, ":original_king"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, ":original_faction", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", ":original_faction", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", ":original_faction", pos0),
      (try_end),
      ],
    [
      ("continue",[],"Continue...",
        [
          (troop_get_slot, ":original_faction", "$g_notification_menu_var1", slot_troop_original_faction),
          ## start peace
          (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
            (neq, ":cur_kingdom", ":original_faction"),
            (neq, ":cur_kingdom", "$g_notification_menu_var2"),
            (call_script, "script_diplomacy_start_peace_between_kingdoms", ":cur_kingdom", ":original_faction", 0),
          (try_end),
          ## start war
          (call_script, "script_diplomacy_start_war_between_kingdoms", "$g_notification_menu_var2", ":original_faction", 1),
          (call_script, "script_update_all_notes"),
          (change_screen_return),
        ]),
     ]
  ),
  ## restoration end
#rubik Source code of Restoration






  #KAOS  (POLITICAL)
  ("dummy",0,
   "Choose an option:",
   "none",
   [
     ],
    [

    ]
  ),
]

update_camp_action_blank = [
      #KAOS  (POLITICAL)

      ("action_modify_banner",[(eq, "$cheat_mode", 1)],"{!}Cheat: Modify your banner.",
       [
           (start_presentation, "prsnt_banner_selection"),
           #(start_presentation, "prsnt_custom_banner"),
        ]
       ),
      #KAOS  (POLITICAL)
]

update_camp_action_blank_2 = [
      #KAOS  (POLITICAL)
      ("action_rename_kingdom",
       [
         (eq, "$kaos_disabled", 0),
         (eq, "$players_kingdom_name_set", 1),
         (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
         (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
       ],"Rename your kingdom.",
       [
           (start_presentation, "prsnt_name_kingdom"),
       ]
     ),
      #KAOS  (POLITICAL)
]

update_camp_action = [
      #KAOS  (POLITICAL)
      ("action_political_actions",[],"Go to Political Options",
       [
          (jump_to_menu, "mnu_camp_political"),
       ]
      ),
      #KAOS  (POLITICAL)
]

update_start_0 = [
      #KAOS  (POLITICAL)
      ("continue",[],"Continue...",
       [
         (assign, "$kaos_kings_kingdom", 0),
         (assign, "$kaos_kings_vassal", 0),
         (jump_to_menu, "mnu_start_game_1"),
       ]
      ),
      #KAOS  (POLITICAL)
]


update_menu_town_1 = [
    ## REPLACEMENT MENU - 
     ("town_1",
       [
            (eq, "$kaos_kings_kingdom", 0), 
            (eq, "$kaos_kings_vassal", 0), 
            (eq, "$kaos_kings_prince", 0), 

            (eq, "$current_startup_quest_phase", 0),
       ],"join a caravan to Praven, in the Kingdom of Swadia.",
       [
         (assign, "$current_town", "p_town_6"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_praven"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),  
 ]

update_menu_town_2 = [
    ## REPLACEMENT MENU - 
      ("town_2",
        [
            (eq, "$kaos_kings_kingdom", 0), 
            (eq, "$kaos_kings_vassal", 0), 
            (eq, "$kaos_kings_prince", 0), 
            (eq, "$current_startup_quest_phase", 0),
        ],"join a caravan to Reyvadin, in the Kingdom of the Vaegirs.",
       [
         (assign, "$current_town", "p_town_8"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_reyvadin"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),   
 ]

update_menu_town_3 = [
    ## REPLACEMENT MENU - 
      ("town_3",
        [
            (eq, "$kaos_kings_kingdom", 0), 
            (eq, "$kaos_kings_vassal", 0), 
            (eq, "$kaos_kings_prince", 0), 
            (eq, "$current_startup_quest_phase", 0),
        ],"join a caravan to Tulga, in the Khergit Khanate.",
       [
         (assign, "$current_town", "p_town_10"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_tulga"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),   
 ]

update_menu_town_4 = [
    ## REPLACEMENT MENU - 
      ("town_4",
        [
            (eq, "$kaos_kings_kingdom", 0), 
            (eq, "$kaos_kings_vassal", 0), 
            (eq, "$kaos_kings_prince", 0), 
            (eq, "$current_startup_quest_phase", 0),
          ],"take a ship to Sargoth, in the Kingdom of the Nords.",
       [
         (assign, "$current_town", "p_town_1"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_sargoth"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]), 
 ]

update_menu_town_5 = [
    ## REPLACEMENT MENU - 
      ("town_5",
        [
            (eq, "$kaos_kings_kingdom", 0), 
            (eq, "$kaos_kings_vassal", 0), 
            (eq, "$kaos_kings_prince", 0), 
            (eq, "$current_startup_quest_phase", 0),
       ],"take a ship to Jelkala, in the Kingdom of the Rhodoks.",
       [
         (assign, "$current_town", "p_town_5"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_jelkala"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
 ]

update_menu_town_6 = [
    ## REPLACEMENT MENU - 
      ("town_6",
        [
            (eq, "$kaos_kings_kingdom", 0), 
            (eq, "$kaos_kings_vassal", 0), 
            (eq, "$kaos_kings_prince", 0), 
            (eq, "$current_startup_quest_phase", 0),
       ],"join a caravan to Shariz, in the Sarranid Sultanate.",
       [
         (assign, "$current_town", "p_town_19"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_shariz"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
 ]

update_menu_start_phase_2 = [

      ("town_1_king",
        [
          (eq, "$current_startup_quest_phase", 0),
          (eq, "$kaos_kings_kingdom", 1), 
          (call_script,"script_set_player_kingdom_init", "fac_kingdom_1", "p_town_6", "fac_culture_1", "trp_knight_1_1", "trp_knight_2_1", "trp_kingdom_1_lord", "scn_town_6_castle"),
       ],"You take a caravan home to Praven.",
       [
         (assign, "$current_town", "p_town_6"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_praven"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_2_king",
        [
          (eq, "$current_startup_quest_phase", 0),
          (eq, "$kaos_kings_kingdom", 2), 
          (call_script,"script_set_player_kingdom_init", "fac_kingdom_2", "p_town_8", "fac_culture_2", "trp_knight_2_1", "trp_knight_3_1", "trp_kingdom_2_lord", "scn_town_8_castle"),
        ],"You take a caravan home to Reyvadin.",
       [
         (assign, "$current_town", "p_town_8"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_reyvadin"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_3_king",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_kingdom", 3), 
            (call_script,"script_set_player_kingdom_init", "fac_kingdom_3", "p_town_10", "fac_culture_3", "trp_knight_3_1", "trp_knight_4_1", "trp_kingdom_3_lord", "scn_town_10_castle"),
        ],"You take a caravan home to Tulga.",
       [
         (assign, "$current_town", "p_town_10"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_tulga"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_4_king",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_kingdom", 4), 
            (call_script,"script_set_player_kingdom_init", "fac_kingdom_4", "p_town_1", "fac_culture_4", "trp_knight_4_1", "trp_knight_5_1", "trp_kingdom_4_lord", "scn_town_1_castle"),
        ],"You take a ship home to Sargoth.",
       [
         (assign, "$current_town", "p_town_1"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_sargoth"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_5_king",
        [
          (eq, "$current_startup_quest_phase", 0),
          (eq, "$kaos_kings_kingdom", 5), 
          (call_script,"script_set_player_kingdom_init", "fac_kingdom_5", "p_town_5", "fac_culture_5", "trp_knight_5_1", "trp_knight_6_1", "trp_kingdom_5_lord", "scn_town_5_castle"),
        ],"You take a ship home to Jelkala.",
       [
         (assign, "$current_town", "p_town_5"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_jelkala"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_6_king",
        [
          (eq, "$current_startup_quest_phase", 0),
          (eq, "$kaos_kings_kingdom", 6), 
          (call_script,"script_set_player_kingdom_init", "fac_kingdom_6", "p_town_19", "fac_culture_6", "trp_knight_6_1", "trp_knight_1_1_wife", "trp_kingdom_6_lord", "scn_town_19_castle"),
    ],"You take a caravan home to Shariz.",
       [
         (assign, "$current_town", "p_town_19"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_shariz"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),









      ("town_1_prince",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 1), 
            (call_script,"script_set_player_prince_init", "fac_kingdom_1", "trp_knight_1_1", "trp_knight_2_1", "trp_kingdom_1_lord"),
            (str_store_party_name, s55, "$kaos_prince_start"),
       ],"You take a caravan home to {s55}.",
       [
         (assign, "$current_town", "$kaos_prince_start"),
         (assign, "$g_starting_town", "$kaos_prince_start"),
         (assign, "$g_journey_string", "str_journey_to_praven"),
         (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
         (change_screen_return),
       ]),
       
      ("town_1_prince_2",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 1), 
            #(call_script,"script_set_player_prince_init", "fac_kingdom_1", "trp_knight_1_1", "trp_knight_2_1", "trp_kingdom_1_lord"),
       ],"You take a caravan to Paven.",
       [
         (assign, "$current_town", "p_town_6"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_praven"),
         (party_relocate_near_party, "p_main_party", "p_town_6", 2),
         (change_screen_return),
       ]),
       
      ("town_2_prince",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 2), 
            (call_script,"script_set_player_prince_init", "fac_kingdom_2", "trp_knight_2_1", "trp_knight_3_1", "trp_kingdom_2_lord"),
            (str_store_party_name, s55, "$kaos_prince_start"),
       ],"You take a caravan home to {s55}.",
       [
         (assign, "$current_town", "$kaos_prince_start"),
         (assign, "$g_starting_town", "$kaos_prince_start"),
         (assign, "$g_journey_string", "str_journey_to_reyvadin"),
         (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
         (change_screen_return),
       ]),
     
      ("town_2_prince_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 2), 
            #(call_script,"script_set_player_prince_init", "fac_kingdom_2", "trp_knight_2_1", "trp_knight_3_1", "trp_kingdom_2_lord"),
        ],"You take a caravan to Reyvadin.",
       [
         (assign, "$current_town", "p_town_8"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_reyvadin"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_3_prince",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 3), 
            (call_script,"script_set_player_prince_init", "fac_kingdom_3", "trp_knight_3_1", "trp_knight_4_1", "trp_kingdom_3_lord"),
            (str_store_party_name, s55, "$kaos_prince_start"),
        ],"You take a caravan home to {s55}.",
       [
         (assign, "$current_town", "$kaos_prince_start"),
         (assign, "$g_starting_town", "$kaos_prince_start"),
         (assign, "$g_journey_string", "str_journey_to_tulga"),
         (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
         (change_screen_return),
       ]),
       
      ("town_3_prince_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 3), 
            #(call_script,"script_set_player_prince_init", "fac_kingdom_3", "trp_knight_3_1", "trp_knight_4_1", "trp_kingdom_3_lord"),
        ],"You take a caravan to Tulga.",
       [
         (assign, "$current_town", "p_town_10"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_tulga"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_4_prince",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 4), 
            (call_script,"script_set_player_prince_init", "fac_kingdom_4", "trp_knight_4_1", "trp_knight_5_1", "trp_kingdom_4_lord"),
            (str_store_party_name, s55, "$kaos_prince_start"),
        ],"You take a ship home to {s55}.",
       [
         (assign, "$current_town", "$kaos_prince_start"),
         (assign, "$g_starting_town", "$kaos_prince_start"),
         (assign, "$g_journey_string", "str_journey_to_sargoth"),
         (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
         (change_screen_return),
       ]),
       
       
      ("town_4_prince_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 4), 
            #(call_script,"script_set_player_prince_init", "fac_kingdom_4", "trp_knight_4_1", "trp_knight_5_1", "trp_kingdom_4_lord"),
        ],"You take a ship to Sargoth.",
       [
         (assign, "$current_town", "p_town_1"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_sargoth"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_5_prince",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 5), 
            (call_script,"script_set_player_prince_init", "fac_kingdom_5","trp_knight_5_1", "trp_knight_6_1", "trp_kingdom_5_lord"),
            (str_store_party_name, s55, "$kaos_prince_start"),
        ],"You take a ship home to {s55}.",
       [
         (assign, "$current_town", "$kaos_prince_start"),
         (assign, "$g_starting_town", "$kaos_prince_start"),
         (assign, "$g_journey_string", "str_journey_to_jelkala"),
         (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
         (change_screen_return),
       ]),
       
      ("town_5_prince_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 5), 
            #(call_script,"script_set_player_prince_init", "fac_kingdom_5","trp_knight_5_1", "trp_knight_6_1", "trp_kingdom_5_lord"),
        ],"You take a ship to Jelkala.",
       [
         (assign, "$current_town", "p_town_5"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_jelkala"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_6_prince",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 6), 
            (call_script,"script_set_player_prince_init", "fac_kingdom_6", "trp_knight_6_1", "trp_knight_1_1_wife", "trp_kingdom_6_lord"),
            (str_store_party_name, s55, "$kaos_prince_start"),
        ],"You take a caravan home to {s55}.",
       [
         (assign, "$current_town", "$kaos_prince_start"),
         (assign, "$g_starting_town", "$kaos_prince_start"),
         (assign, "$g_journey_string", "str_journey_to_shariz"),
         (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
         (change_screen_return),
       ]),

      ("town_6_prince_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_prince", 6), 
            #(call_script,"script_set_player_prince_init", "fac_kingdom_6", "trp_knight_6_1", "trp_knight_1_1_wife", "trp_kingdom_6_lord"),
        ],"You take a caravan to Shariz.",
       [
         (assign, "$current_town", "p_town_19"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_shariz"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),






      ("town_1_vassal",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 1), 
            (call_script,"script_set_player_vassal_init", "fac_kingdom_1", "trp_knight_1_1", "trp_knight_2_1", "trp_kingdom_1_lord"),
            (str_store_party_name, s55, "$kaos_vasal_start"),
       ],"You take a caravan home to {s55}.",
       [
         (assign, "$current_town", "p_town_6"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_praven"),
         (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
         (change_screen_return),
       ]),
       
      ("town_1_vassal_2",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 1), 
           # (call_script,"script_set_player_vassal_init", "fac_kingdom_1", "trp_knight_1_1", "trp_knight_2_1", "trp_kingdom_1_lord"),
       ],"You take a caravan to Paven.",
       [
         (assign, "$current_town", "p_town_6"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_praven"),
         (party_relocate_near_party, "p_main_party", "p_town_6", 2),
         (change_screen_return),
       ]),
       
      ("town_2_vassal",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 2), 
            (call_script,"script_set_player_vassal_init", "fac_kingdom_2", "trp_knight_2_1", "trp_knight_3_1", "trp_kingdom_2_lord"),
            (str_store_party_name, s55, "$kaos_vasal_start"),
       ],"You take a caravan home to {s55}.",
       [
         (assign, "$current_town", "p_town_8"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_reyvadin"),
         (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
         (change_screen_return),
       ]),
     
      ("town_2_vassal_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 2), 
           # (call_script,"script_set_player_vassal_init", "fac_kingdom_2", "trp_knight_2_1", "trp_knight_3_1", "trp_kingdom_2_lord"),
        ],"You take a caravan to Reyvadin.",
       [
         (assign, "$current_town", "p_town_8"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_reyvadin"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_3_vassal",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 3), 
            (call_script,"script_set_player_vassal_init", "fac_kingdom_3", "trp_knight_3_1", "trp_knight_4_1", "trp_kingdom_3_lord"),
            (str_store_party_name, s55, "$kaos_vasal_start"),
        ],"You take a caravan home to {s55}.",
       [
         (assign, "$current_town", "p_town_10"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_tulga"),
         (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
         (change_screen_return),
       ]),
       
      ("town_3_vassal_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 3), 
            #(call_script,"script_set_player_vassal_init", "fac_kingdom_3", "trp_knight_3_1", "trp_knight_4_1", "trp_kingdom_3_lord"),
        ],"You take a caravan to Tulga.",
       [
         (assign, "$current_town", "p_town_10"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_tulga"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_4_vassal",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 4), 
            (call_script,"script_set_player_vassal_init", "fac_kingdom_4", "trp_knight_4_1", "trp_knight_5_1", "trp_kingdom_4_lord"),
            (str_store_party_name, s55, "$kaos_vasal_start"),
        ],"You take a ship home to {s55}.",
       [
         (assign, "$current_town", "p_town_1"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_sargoth"),
         (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
         (change_screen_return),
       ]),
       
       
      ("town_4_vassal_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 4), 
            #(call_script,"script_set_player_vassal_init", "fac_kingdom_4", "trp_knight_4_1", "trp_knight_5_1", "trp_kingdom_4_lord"),
        ],"You take a ship to Sargoth.",
       [
         (assign, "$current_town", "p_town_1"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_sargoth"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_5_vassal",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 5), 
            (call_script,"script_set_player_vassal_init", "fac_kingdom_5","trp_knight_5_1", "trp_knight_6_1", "trp_kingdom_5_lord"),
            (str_store_party_name, s55, "$kaos_vasal_start"),
        ],"You take a ship home to {s55}.",
       [
         (assign, "$current_town", "p_town_5"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_jelkala"),
         (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
         (change_screen_return),
       ]),
       
      ("town_5_vassal_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 5), 
            #(call_script,"script_set_player_vassal_init", "fac_kingdom_5","trp_knight_5_1", "trp_knight_6_1", "trp_kingdom_5_lord"),
        ],"You take a ship to Jelkala.",
       [
         (assign, "$current_town", "p_town_5"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_jelkala"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
       
      ("town_6_vassal",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 6), 
            (call_script,"script_set_player_vassal_init", "fac_kingdom_6", "trp_knight_6_1", "trp_knight_1_1_wife", "trp_kingdom_6_lord"),
            (str_store_party_name, s55, "$kaos_vasal_start"),
        ],"You take a caravan home to {s55}.",
       [
         (assign, "$current_town", "p_town_19"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_shariz"),
         (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
         (change_screen_return),
       ]),

      ("town_6_vassal_1",
        [
            (eq, "$current_startup_quest_phase", 0),
            (eq, "$kaos_kings_vassal", 6), 
            #(call_script,"script_set_player_vassal_init", "fac_kingdom_6", "trp_knight_6_1", "trp_knight_1_1_wife", "trp_kingdom_6_lord"),
        ],"You take a caravan to Shariz.",
       [
         (assign, "$current_town", "p_town_19"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_shariz"),
         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
         (change_screen_return),
       ]),
]


menu_update_character_start_1 = [
   #KAOS (START)
  ("start_king",[],"You replace your father as King",
    [
      (assign,"$background_type",cb_king),
      (assign,"$background_answer_2", cb2_page),
       (try_begin),
            (eq,"$character_gender",tf_female),
            (assign,"$background_answer_3",cb3_lady_in_waiting),
       (else_try),
            (assign,"$background_answer_3",cb3_squire),
       (try_end),
       (assign,"$background_answer_4",cb4_loss),

      (assign, reg3, "$character_gender"),
      (assign, "$kaos_kings_kingdom", 1),
      (str_store_string,s10,"@You were raised as a Prince and were provided the best education and training the kingdom could provide you have been recalled from your studies."),
      (jump_to_menu,"mnu_start_king_1"),
     ]
  ),

  ("start_prince",[],"You return home to your father ..",
    [
      (assign,"$background_type",cb_prince),
      (assign, reg3, "$character_gender"),
      (assign, "$kaos_kings_prince", 1),
      (str_store_string,s10,"@Only you know why you have returned from abroad after all these years to your father.."),     

      (assign,"$background_answer_2", cb2_page),
      (try_begin),
            (eq,"$character_gender",tf_female),
            (assign,"$background_answer_3",cb3_lady_in_waiting),
      (else_try),
           (assign,"$background_answer_3",cb3_squire),
      (try_end),
      (jump_to_menu,"mnu_start_prince_1"),
     ]
  ),

  ("start_vassal",[],"You have become the sworn vassal of ..",
    [
      (assign,"$background_type",cb_vassal),
      (assign, reg3, "$character_gender"),
      (assign, "$kaos_kings_vassal", 1),     

      (assign,"$background_answer_2", cb2_page),
      (try_begin),
            (eq,"$character_gender",tf_female),
            (assign,"$background_answer_3",cb3_lady_in_waiting),
      (else_try),
           (assign,"$background_answer_3",cb3_squire),
      (try_end),
    
      (str_store_string,s10,"@Due to an old debt owed to your father have been allowed to become the vassal of.."),
      (jump_to_menu,"mnu_start_vassal_1"),
     ]
  ),
  #KAOS (START)
]


view_world_map = [
      ("world_map",[],"View World Map.",
       [
         (start_presentation, "prsnt_world_map"),
        ]
       ),
]

from util_common import *
from util_wrappers import *

def modmerge_game_menus(orig_game_menus, check_duplicates = True):
  if( not check_duplicates ):
    orig_game_menus.extend(game_menus) # Use this only if there are no replacements (i.e. no duplicated item names)
  else:
  # Use the following loop to replace existing entries with same id
    for i in range (0,len(game_menus)-1):
      find_index = find_object(orig_game_menus, game_menus[i][0]); # find_object is from header_common.py
      if( find_index == -1 ):
        orig_game_menus.append(game_menus[i])
      else:
        orig_game_menus[find_index] = game_menus[i]

  # splice this into "town" menu to call the center management hub.
  find_i = list_find_first_match_i( orig_game_menus, "camp" )
  menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
  find_i = list_find_first_match_i(menuoptions, "camp_action")   
  OpBlockWrapper(menuoptions).InsertBefore(find_i, update_camp_action)  


  find_i = list_find_first_match_i( orig_game_menus, "start_phase_2" )
  menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
  find_i = list_find_first_match_i(menuoptions, "town_6")   
  OpBlockWrapper(menuoptions).InsertAfter(find_i, update_menu_start_phase_2)  

  find_i = list_find_first_match_i( orig_game_menus, "start_character_1" )
  menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
  find_i = list_find_first_match_i(menuoptions, "start_noble")   
  OpBlockWrapper(menuoptions).InsertBefore(find_i, menu_update_character_start_1)  


  #Updated by Lazeras for KAOS
  # splice this into "town" menu to call the center management hub.
  find_i = list_find_first_match_i( orig_game_menus, "reports" )
  menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
  find_i = list_find_first_match_i(menuoptions, "view_party_size_report")   
  OpBlockWrapper(menuoptions).InsertAfter(find_i, view_world_map)  



  #Updated by Lazeras for KAOS
  try: #full replace entries
    menu_Town = list_find_first_match_i(orig_game_menus, "start_phase_2") # get "start_phase_2" menu
    menu_Town_options_list = GameMenuWrapper(orig_game_menus[menu_Town]).GetMenuOptions() # get option list
    for option_i in range(len(menu_Town_options_list)): # checking all menu options
        option_id = GameMenuOptionWrapper(menu_Town_options_list[option_i]).GetId() # take the name of current menu_option
        if (option_id == "town_1"): # if is target option
          menu_Town_options_list[option_i] = update_menu_town_1[0] # full replace it by new code
        if (option_id == "town_2"): # if is target option
          menu_Town_options_list[option_i] = update_menu_town_2[0] # full replace it by new code
        if (option_id == "town_3"): # if is target option
          menu_Town_options_list[option_i] = update_menu_town_3[0] # full replace it by new code
        if (option_id == "town_4"): # if is target option
          menu_Town_options_list[option_i] = update_menu_town_4[0] # full replace it by new code
        if (option_id == "town_5"): # if is target option
          menu_Town_options_list[option_i] = update_menu_town_5[0] # full replace it by new code
        if (option_id == "town_6"): # if is target option
          menu_Town_options_list[option_i] = update_menu_town_6[0] # full replace it by new code

  except:
      import sys
      print "Injecton 1 failed:", sys.exc_info()[1]
      raise



def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)