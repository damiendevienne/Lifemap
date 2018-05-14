#!/bin/sh
/home/lm/src/mod_tile/render_list -a -z 0 -Z 4 -n 7 >> /var/log/renderd_list.org
/home/lm/src/mod_tile/render_list -n 7 < /home/lm/src/Lifemap/PIPELINE/XYZcoordinates >> /var/log/renderd_list.org
