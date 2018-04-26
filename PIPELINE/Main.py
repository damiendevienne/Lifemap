#!/usr/bin/python

import sys,os
from argparse import ArgumentParser, FileType ##for options handling


##kill render_list (in case it is running)
os.system("sudo kill render_list")

os.system("cd /home/lm/src/Lifemap/PIPELINE")

##
os.system("mkdir genomes") ##if not exists
## 1. get the tree and update database
print '\NCREATING DATABASE'
print '  Doing Archaeal tree...'
os.system('python Traverse_To_Pgsql_2.py 1 1');
print '  ...Done'
with open('tempndid', 'r') as f:
    ndid = f.readline()
print '  Doing Eukaryotic tree... start at id: %s' % ndid
os.system('python Traverse_To_Pgsql_2.py 2 %s --updatedb False' % ndid)
print '  ...Done'
with open('tempndid', 'r') as f:
    ndid = f.readline()
print '  Doing Bact tree... start at id:%s ' % ndid
os.system('python Traverse_To_Pgsql_2.py 3 %s --updatedb False' % ndid)
print '  ...Done'

## 2. Get additional info from NCBI
print '  Getting addditional Archaeal info...'
os.system('python Additional.info.py 1')
print '  Getting addditional Euka info...'
os.system('python Additional.info.py 2')
print '  Getting addditional Bacter info...'
os.system('python Additional.info.py 3')
print '  ...Done'

## 3. Update Solr informations
print '  Updating Solr... '
os.system('python updateSolr.py')
print '  ...Done '

## 4. Create postgis index
print '  Creating index... '
os.system('python CreateIndex.py')
print '  Done... '

# 5. get and copy date of update to /var/www/html
os.system('sudo getDateUpdate.sh')

## 6. Remove old tiles
print '  Deleting old tiles... '
os.system('sudo rm -r /var/lib/mod_tile/default/')

## 7. Restarting the machine 
print 'restart NOW'
os.system('sudo reboot')



##/home/lm/src/Lifemap/PIPELINE/Main.py >> /var/log/lifemap.log

