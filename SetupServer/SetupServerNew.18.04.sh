##UPDATE AND INSTALL REQUIRED PACKAGES
sudo apt-get --yes update
sudo apt-get --yes upgrade
sudo apt-get --yes install libboost-all-dev git-core tar unzip wget bzip2 build-essential autoconf libtool 
sudo apt-get --yes install libxml2-dev libgeos-dev libgeos++-dev libpq-dev libbz2-dev libproj-dev munin-node munin 
sudo apt-get --yes install libprotobuf-c0-dev protobuf-c-compiler libfreetype6-dev libpng-dev libtiff5-dev libicu-dev libgdal-dev libcairo-dev 
sudo apt-get --yes install libcairomm-1.0-dev apache2 apache2-dev libagg-dev liblua5.2-dev ttf-unifont lua5.1 liblua5.1-dev libgeotiff-epsg node-carto
sudo apt-get --yes install postgresql postgresql-contrib postgis postgresql-10-postgis-2.4
sudo apt-get --yes install gdal-bin libgdal-dev libmapnik-dev mapnik-utils python-mapnik
sudo apt-get --yes install python-numpy python-qt4 python-lxml python-six python-pip

##CONFIGURE POSTGRESQL/POSTGIS USER AND DATABASE
sudo -u postgres psql -c "DROP DATABASE IF EXISTS tree;"
sudo -u postgres psql -c "DROP USER IF EXISTS lm;"
sudo -u postgres psql -c "CREATE USER lm WITH PASSWORD 'gvC5b78Ch9nDePjF';"
sudo -u postgres psql -c "CREATE DATABASE tree OWNER lm ENCODING UTF8;"
##copy pgpass locally 


##INSTALL MOD TILE and RENDERD
git clone git://github.com/damiendevienne/mod_tile_deepzoom.git /tmp/mod_tile
(cd /tmp/mod_tile/ ; ./autogen.sh)
(cd /tmp/mod_tile/ ; ./configure)
(cd /tmp/mod_tile/ ; make)
(cd /tmp/mod_tile/ ; sudo make install)
(cd /tmp/mod_tile/ ; sudo make install-mod_tile)
sudo ldconfig
sudo mkdir /var/lib/mod_tile
sudo mkdir /var/run/renderd
sudo cp SetupServer/mod_tile.conf /etc/apache2/conf-available/mod_tile.conf
sudo a2enconf mod_tile

##CONFIGURE APACHE
sudo service apache2 reload
sudo cp ~/src/Lifemap/SetupServer/renderd.conf /etc/ ## a faire avant de relancer apache2
sudo cp ~/src/Lifemap/SetupServer/000-default.conf /etc/apache2/sites-available/ #replace apache config file 
sudo service apache2 restart

##INSTALL ETE (TREE MANIPULATION) AND DEPENDENCIES 
sudo pip install --upgrade pip
sudo pip install --upgrade psycopg2-binary
sudo pip install --upgrade ete3
##configure solr
sudo apt-get --yes install default-jre default-jdk
cd ~/src
wget http://mirrors.ircam.fr/pub/apache/lucene/solr/6.6.3/solr-6.6.3.tgz
tar xvzf solr-6.6.3.tgz
cd ~/src/solr-6.6.3
bin/solr start
bin/solr create -c taxo
bin/solr create -c addi
cp ~/src/Lifemap/OTHER/solr-config/schema.taxo.xml ~/src/solr-6.6.3/server/solr/taxo/conf/schema.xml
cp ~/src/Lifemap/OTHER/solr-config/solrconfig.taxo.xml ~/src/solr-6.6.3/server/solr/taxo/conf/solrconfig.xml
