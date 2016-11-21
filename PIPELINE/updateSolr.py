#!/usr/bin/python

#    This file is part of Lifemap.

#    Lifemap is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Lifemap is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Lifemap.  If not, see <http://www.gnu.org/licenses/>.


##FEB2016
# this code performs the following actions: 
# 1. start solr (if not started)
# 2. removing all taxo and ascen documents
# 3. Uploading taxo and ascend data
# 4. restarting solr.

import sys,os, time

path2solr = "/home/ddevienne/TOOLS/solr-5.4.0/"
startsolr = path2solr + "bin/solr start"
restartsolr = path2solr + "bin/solr restart"


# 1. start solr  
print '  (1/4) Starting Solr...\n'
os.system(startsolr)
print ('sleep a bit')
time.sleep(30)
print '  Solr successfully started\n'


# 2. Delete old documents  
print '  (2/4) Deleting Solr docs...\n'
print '          Deleting taxo...\n'
delete1 = "curl http://localhost:8983/solr/taxo/update?commit=true -d '<delete><query>*:*</query></delete>'"
os.system(delete1)
print '          Taxo successfully deleted\n'
print '          Deleting addi...\n'
delete2 = "curl http://localhost:8983/solr/addi/update?commit=true -d '<delete><query>*:*</query></delete>'"
os.system(delete2)
print '          Addi successfully deleted\n'
print '          Restarting Solr...\n'
os.system(restartsolr)
print '          Solr successfully restarted\n'

# 3. Uploading files 
print '  (3/4) Uploading files to Solr...\n'
for i in range(1,4):
    uupadtesolr = path2solr + "bin/post -c taxo TreeFeatures%d.json" % i
    os.system(uupadtesolr)
    print '          -> TreeFeatures %d successfully uploaded.' % i 

for i in range(1,4):
    uupadtesolr2 = path2solr + "bin/post -c addi ADDITIONAL.%d.json" % i
    os.system(uupadtesolr2)
    print '          -> Additions %d successfully uploaded.' % i 
print '        All files successfully uploaded\n'
    
# 4. Restarting solr 
print '  (4/4) Restarting Solr...\n'
os.system(restartsolr)
print '        Solr successfully restarted\n'
