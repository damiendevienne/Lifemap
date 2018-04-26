#!/bin/sh
echo "$(echo "var DateUpdate='")" "$(date -R -r taxdump.tar.gz | cut -d' ' -f1-4)" "$(echo "';")" > date-update.js
sudo cp date-update.js /var/www/html
