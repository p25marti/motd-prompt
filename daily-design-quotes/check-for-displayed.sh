#!/bin/bash
#This checks for the file displayed-already.flag. If the file exists, remove it.

if [ -f /home/pingu/.config/daily-design-quotes/displayed-already.flag ]; then
    rm /home/pingu/.config/daily-design-quotes/displayed-already.flag
fi
