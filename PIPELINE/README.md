#Lifemap pipeline

###Prerequisites

These Lifemap functions are written in python (v2.7) and necssitate the following tools and libraries to be intalled: 
* The great ete3 toolkit written by Jaime Huerta-Cepas: http://etetoolkit.org/download/
* Solr Apache Search Engine (I used version 5.4.0): http://lucene.apache.org/solr/
* mapnik v3 (I used version 3.0.9): http://mapnik.org/
* mod_tile: https://github.com/openstreetmap/mod_tile WARNING! you have to use the **modified version** available in ../Lifemap/OTHER if you want to be able to viualize more than the default 18 zoom levels

###Description of functions

All functions are full of commentaries that should help interested users to reproduce Lifemap. *Main.py* contains calls to all the other pythons scripts. If everything is correctly configured, calling it one does all the job.
Other scripts are described below: 
* *getTrees.py* retrieves the whole NCBI taxonomy, and writes three files each containing one of the domains of life (ARCHAEA, BACTERIA and EUKARYOTES) in NHX format.
* *CleanTrees.py* removes all taxa whose name contains words *unidentified*, *environmental*, *unclassified* or *uncultured* and all the taxa below the species level
