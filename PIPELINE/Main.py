#!/usr/bin/python

import sys,os
from argparse import ArgumentParser, FileType ##for options handling


##
os.system("mkdir genomes")
## 1. get the tree and update database
##print 'RETRIEVING NCBI DATA'
##print '  Downloading trees...'
##os.system('python getTrees.py');
##print '  Done'
print '\NCREATING DATABASE'
print '  Traversing Archaeal tree...'
os.system('python Traverse_To_Pgsql_2.py 1 1');
print '  ...Done'
with open('tempndid', 'r') as f:
    ndid = f.readline()
print '  Traversing Eukaryotic tree... start at id: %s' % ndid
os.system('python Traverse_To_Pgsql_2.py 2 %s --updatedb False' % ndid)
print '  ...Done'
with open('tempndid', 'r') as f:
    ndid = f.readline()
print '  Traversing Bact tree... start at id:%s ' % ndid
os.system('python Traverse_To_Pgsql_2.py 3 %s --updatedb False' % ndid)
print '  ...Done'


## 1bis. Get additional info from NCBI
print '  Getting addditional Archaeal info...'
os.system('python Additional.info.py 1')
print '  Getting addditional Euka info...'
os.system('python Additional.info.py 2')
print '  Getting addditional Bacter info...'
os.system('python Additional.info.py 3')
print '  ...Done'
## 2. Update Solr informations
print '  Updating Solr... '
os.system('python updateSolr.py')
print '  ...Done '


## 3. move trees/ to /var/www/html after deleting previous version
##delete old 'trees' files
# print '  Deleting old newick tree files... '
# os.system('rm -r /var/www/html/trees/')
# print '  ...Done '
# print '  Moving new newick tree files... '
# os.system('mv trees/ /var/www/html/trees/')

## 4. Remove tiles
print '  Deleting old tiles... '
os.system('rm -r /var/lib/mod_tile/default/')


## 5. Create postgis index
print '  Creating index... '
os.system('python CreateIndex.py')

## 6. Restart apache, posgresql and renderd 
##os.system('killall lt-renderd')
##os.system('/etc/init.d/postgresql restart')
##os.system('/etc/init.d/apache2 restart')
##os.system('./home/ddevienne/TOOLS/mod_tile/renderd')

## 6.bis. Restarting the machine would be the easiest way.
os.system('reboot')