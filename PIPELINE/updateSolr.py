#!/usr/bin/python

##FEB2016
# this code performs the following actions: 
# 1. start solr (if not started)
# 2. removing all taxo and ascen documents
# 3. Uploading taxo and ascend data
# 4. restarting solr.

import sys,os, time

path2solr = "/home/lm/src/solr-6.6.3/" 
startsolr = path2solr + "bin/solr start"
restartsolr = path2solr + "bin/solr restart"


# 1. start solr  
print '  (1/4) Starting Solr...\n'
os.system(startsolr)
print '  Solr successfully started\n'


# 2. Delete old documents  
print '  (2/4) Deleting Solr docs...\n'
print '          Deleting taxo...\n'
delete1 = "curl http://localhost:8080/solr/taxo/update?commit=true -d '<delete><query>*:*</query></delete>'"
os.system(delete1)
print '          Taxo successfully deleted\n'
print '          Deleting addi...\n'
delete2 = "curl http://localhost:8080/solr/addi/update?commit=true -d '<delete><query>*:*</query></delete>'"
os.system(delete2)
print '          Addi successfully deleted\n'
print '          Deleting ncbi...\n'
delete2 = "curl http://localhost:8080/solr/ncbi/update?commit=true -d '<delete><query>*:*</query></delete>'"
os.system(delete2)
print '          ncbi successfully deleted\n'
print '          Restarting Solr...\n'
os.system(restartsolr)
print '          Solr successfully restarted\n'

#sleep for 1 minute
time.sleep(60)


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
##and add the full NCBI docs
uupadtesolr3 = path2solr + "bin/post -c ncbi ADDITIONAL.FULLNCBI.json"
os.system(uupadtesolr2)
print '          -> Additions FULLNCBI successfully uploaded.'


print '        All files successfully uploaded\n'
    
# 4. Restarting solr 
print '  (4/4) Restarting Solr...\n'
os.system(restartsolr)
print '        Solr successfully restarted\n'
