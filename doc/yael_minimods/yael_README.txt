<!-- -*- coding: utf-8; mode: markdown -*- -->


<!-- Short description for nexus -->

SUMMARY
=======

A collection of independent modmerger (mini)mods, aimed at casual
modders, who want to spice up an existing module with modmerger mods.
Most notably improvements for red/blue color-blind players for the
arena.

Make cattle follow you, disable unwanted quests, color-blindness
improvements for tournaments, customized tournament and arena rewards,
sell prisoners in taverns, and a few items.

Contains as most significant addition a tabular equipment manager,
displaying all companions (and their skills) at once.

Mods can be added independently.


CHANGELOG
=========

**2018-06-09** Added ``yael_eqmgr`` mod, which is so far by now the
most complex part.

**2017-11-19.3** Fixed bug in ``yael_ransomtavern`` which caused
prisoners to be sold at the 50 denars rate of the galley slave trader.
Thematically fitting to the dialog, but not intended `` ‾\ツ/‾ ``.

**2017-11-19.2** ``yael_tournamentrewards`` was leading to an empty
bet menu when trying to bet with money remaining in the range of 5-9
denars. This should now be fixed.

**2017-11-19.1** Fixed a bug in ``yael_colorblind1``, that caused doors
in towns to lead to the wrong place.


INSTALLATION
============

Obtain a copy of the warband module system.

Install the [ModMerger framework][1].

Copy the files from this mod into the module system directory.

Add the names of the wanted mods from the subsequent listing to
the variable *mods_active* in *modmerger_options.py*, e.g.

    mods_active = [
        "yael_core",        ## ALWAYS NEEDED
        "yael_cattlefollow",
        "yael_colorblind1",
    ]


LIST OF MODS AND FILES
======================

**yael_core.** Defines some resources shared across the submods.


**yael_eqmgr.** Adds a tabular equiment manager to the camp menu.

In the equipment manager view, a table of all companion and player
equipment and the player's inventory are shown. 

  - Hover the mouse over an item to display tooltip, requirements, and
    highlight companions that cannot equip it.
  - Click an item to select it. Click another slot to swap them. (Drag
    and drop wasn't feasibly implementable.)
  - Right-click on any slot to unselect the current slot.
  
Additionally a second page provides a tabular overview of companion
skills, in order to support planning upgrades.


**yael_colorblind1.** Manipulates the team assignment in tournaments
to ensure that never the player *and* an enemy team are red/green –
which are extremely hard to tell apart in a tournament at dusk or dawn
when being among the 10% of male players affected by red-green
colorblindness.

When four teams are fighting, the player is ensured to be either
yellow or blue. Though yellow is also affected by red-green color
blindness, its higher relative brightness still makes it sufficiently
distinct.

I am not entirely sure if that last statement holds for stronger
color-blindness (I can tell red and green apart, it is just more
difficult), so if you can't tell the yellow from the red and green
teams, please let me know.


**yael_colorblind2.** The previous conflicts with mods that make major
changes to the tournaments (in particular the script of the "Join next
fight" menu entry). As an alternative, this mod switches green
tournament clothing for the white set, which is unused in the vanilla
game. This avoids having the green and red sets, which are the hardest
to distinguish for red-green color-blind people, at the same time.

This mod should be compatible with almost any mod, unless the other
mod makes use of white tournament clothing.


**yael_cattlefollow.** In the menu of cattle, you get an option
causing cattle to follow you instead of running from you. Less like
herding, but more convenient if you dislike the herding quests.


**yael_disablequests.** Disables some of the randomized quests given
by lords and villagers. What quests exactly are disabled, is defined
by the variable ``DISABLED_QUEST_IDS`` in
``yael_disablequests_dialogs.py``.

Before enabling this mod, you will probably want to customize that
variable. In order to find IDs, for which this mod works, search
``module_dialogs.py`` for the string

    (eq,"$random_quest_no",<ID HERE>),

The mod works by removing the dialogs, that have this as the first
item in their conditions block.


**yael_tournamentrewards.** Doubles the allowed bets, making it easier
to earn money from tournaments.

Naive implementation, that simply replaces the ``tournament_net`` by a
copy of the original menu with changed bet tiers. I probably won't
come around to creating a cleaner version of this mod.


**yael_ransomtavern.** Your local tavern keeper needs some help with
the dishes. Don't you have some hands to share? (Preferably some who
won't complain if they go unpaid, if you get my drift...)

More seriously though, this mod adds an option to tavern keepers, that
allows selling prisoners to them, so you are no longer dependent on
the random luck of having a ransom broker around for emptying your
prisoner-slots.


**yael_arenarewards.** Increases the amount of gold and experience
earned upon completing an arena fight.

For customization, the amounts are defined in
``yael_arenarewards_constants.py``. The variable names should be
self-explanatory.


**yael_extraitems.** Adds some customized items.

    +------------ B E W A R E --------------+
    |  Mods  that  add  items  cannot  be   |
    |  removed without breaking savegames.  |
    +---------------------------------------+

The items added are...

  - An invisible nordic warlord helmet.
  - A tribal warrior outfit with stats of the Sarranid elite armor.

The items are statwise indistinguishable from their templates, and
thus balanced. They should show up in merchants.

If the items don't show up in merchants, they can still be accessed by
using the *cheatmenu* console command, going to “CHEAT MENU! → Find an
item". Added items should be in the highest range (around 600). The
inivisble helmet will look like an empty inventory slot, where none
should be, and can only be seen from its mouse-over menu.

When removal of mods reduces the total number of items known to the
game, old savegames crash the game. If the number of items is kept
constant or increased, but the order of items changes, the savegame
will contain mixed-up IDs. This might also crash the game, or cause
your helmet to turn into a book.


<!-- ------------------------------------------------------------- -->

[1]: https://forums.taleworlds.com/index.php?topic=128890.0
