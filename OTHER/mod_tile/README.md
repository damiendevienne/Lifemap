#mod_tile modification

If 32 zoom levels is not enough for what you want to visualize, you should replace the `src` and `includes` folders of your mod_tile version by those displayed here and recompile.

mod_tile is available at https://github.com/openstreetmap/mod_tile

The modified files given here are compatible with mod_tile version downloaded from GitHub on January, 1st 2016.


###Configuration file for mod_tile and renderd

The configuration file that I use for mod_tile/renderd is as follows: 
```
[renderd]
num_threads=8
tile_dir=/var/lib/mod_tile
stats_file=/var/run/renderd/renderd.stats


[mapnik]
plugins_dir=/usr/local/lib/mapnik/input
font_dir=/usr/local/lib/mapnik/fonts
font_dir_recurse=1

[default]
URI=/osm_tiles/
TILEDIR=/var/lib/mod_tile
XML=/home/ddevienne/DATA_IN/osm.xml
HOST=localhost
TILESIZE=256
MINZOOM=0
MAXZOOM=40
```

You may have to change some parameters for your needs.
