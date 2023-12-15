#!/bin/bash
rm messages.pot
find ../src -name '*.py' >POTFILES
xgettext --files-from=POTFILES --from-code=UTF-8 -L Python -o messages.pot
rm POTFILES
