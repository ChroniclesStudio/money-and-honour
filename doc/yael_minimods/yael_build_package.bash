#!/usr/bin/env bash
# -*- mode: sh; coding: us-ascii-unix -*-

set -e -E -u

pandoc --from=markdown --to=html --standalone yael_README.txt > yael_README.html
zip "yael_minimods_$(printf '%(%F)T' -1).zip" yael_*.{py,txt,html,bash}

python3 html2bbcode.py yael_README.html \
        '[["pre"],["[QUOTE]","[/QUOTE]"]]' \
        '[["li"],["[*][size=2]","[/size]"]]' \
        '[["strong"],["[B][COLOR=white]","[/COLOR][/B]"]]' \
        > yael_README.nexusmods.bbcode
python3 html2bbcode.py yael_README.html > yael_README.forum.bbcode
cat yael_README.nexusmods.bbcode > /dev/clipboard
echo 'Copied Nexusmods BBCODE to clipboard'
echo 'Forum BBCODE in file.'

