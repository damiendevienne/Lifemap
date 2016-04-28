#Lifemap pipeline

###Prerequisites

These Lifemap functions are written in python (v2.7) and necssitate the following tools and libraries to be intalled: 
* The great ete3 toolkit (python) written by Jaime Huerta-Cepas: http://etetoolkit.org/download/ for tree manipulation and NCBI-related functions
* Solr Apache Search Engine (I used version 5.4.0): http://lucene.apache.org/solr/
* mapnik v3 (I used version 3.0.9): http://mapnik.org/
* mod_tile: https://github.com/openstreetmap/mod_tile WARNING! you have to use the **modified version** available in ../Lifemap/OTHER if you want to be able to viualize more than the default 18 zoom levels
* A PostgreSQL/PostGIS database. See http://postgis.net/install/ to see how to add the PostGIS extension to a PostgreSQL database.

###Description of functions

All functions are full of commentaries that should help interested users to reproduce Lifemap. *Main.py* contains calls to all the other pythons scripts. If everything is correctly configured, calling it once does all the job.
Other scripts are described below, in the order they are called in the *Main.py* script: 
* *getTrees.py* retrieves the whole NCBI taxonomy, and writes three files each containing one of the domains of life (ARCHAEA, BACTERIA and EUKARYOTES) in NHX format.
* *CleanTrees.py* removes all taxa whose name contains words *unidentified*, *environmental*, *unclassified* or *uncultured* and all the taxa below the species level. This function should not be called if one wants to keep the complete NCBI taxonomy.
* *Traverse_To_Pgsql_2.py* is the main function in Lifemap. It computes all the coordinates of all the nodes and tips of the tree, determine from which zoom level they should be visible on the map, computes the coordinates of the hlf circles, and writes everything to a PostgreSQL/PostGIS database. This script creates also a json file containing various information about each taxa that will be used by Solr later to search species on the map, and search paths.  
* *Additional.info.py* finds (for now) the information concerning whole genomes sequenced in the NCBI website and writes this information in  json file used later by Solr. It also computes for each node of the tree, the path to the root. This is written in the same json file and is used for finding paths between taxa in Lifemap.
* *updateSolr.py* feeds Solr with the coontent of the json files created earlier. Solr dictionnaries need to be created before and configured correctly with the file given in ../OTHER/
* *CreateIndex.py* create indexes in the PostgreSQL/PostGIS database which improves greatly the speed at which the data is retrieved.
