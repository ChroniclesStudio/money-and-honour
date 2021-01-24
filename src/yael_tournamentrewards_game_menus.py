from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from module_constants import *

game_menus = [
  (
    "tournament_bet",0,
    "The odds against you are {reg5} to {reg6}.{reg1? You have already bet {reg1} denars on yourself, and if you win, you will earn {reg2} denars.:} How much do you want to bet?",
    "none",
    [
      (assign, reg1, "$g_tournament_bet_placed"),
      (store_add, reg2, "$g_tournament_bet_win_amount", "$g_tournament_bet_placed"),
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":player_odds", reg0),
      (assign, ":min_dif", 100000),
      (assign, ":min_dif_divisor", 1),
      (assign, ":min_dif_multiplier", 1),
      (try_for_range, ":cur_multiplier", 1, 50),
        (try_for_range, ":cur_divisor", 1, 50),
          (store_mul, ":result", 100, ":cur_multiplier"),
          (val_div, ":result", ":cur_divisor"),
          (store_sub, ":difference", ":player_odds", ":result"),
          (val_abs, ":difference"),
          (lt, ":difference", ":min_dif"),
          (assign, ":min_dif", ":difference"),
          (assign, ":min_dif_divisor", ":cur_divisor"),
          (assign, ":min_dif_multiplier", ":cur_multiplier"),
        (try_end),
      (try_end),
      (assign, reg5, ":min_dif_multiplier"),
      (assign, reg6, ":min_dif_divisor"),
      ],
    [
      ("bet_200_denars", [(store_troop_gold, ":gold", "trp_player"),
                          (ge, ":gold", 200)
                          ],
       "200 denars.",
       [
         (assign, "$temp", 200),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_100_denars", [(store_troop_gold, ":gold", "trp_player"),
                          (ge, ":gold", 100)
                          ],
       "100 denars.",
       [
         (assign, "$temp", 100),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_50_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 50)
                         ],
       "50 denars.",
       [
         (assign, "$temp", 50),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_20_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 20)
                         ],
       "20 denars.",
       [
         (assign, "$temp", 20),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_10_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 10)
                         ],
       "10 denars.",
       [
         (assign, "$temp", 10),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_5_denars", [(store_troop_gold, ":gold", "trp_player"),
                        (ge, ":gold", 5)
                        ],
       "5 denars.",
       [
         (assign, "$temp", 5),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("go_back_dot", [], "Go back.",
       [
         (jump_to_menu, "mnu_town_tournament"),
        ]),

      # For every high-tier addition I remove a low-tier one, 
      # as this causes the highest bet and the confirmation 
      # option to be at the same position, allowing faster 
      # menu navigation [but also bugging out at <10 denars reset]
    ]
  ),
]
