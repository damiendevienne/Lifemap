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


import sys,os

##WE ADD (march2016) a cleaning process to remove
##unclassified, unidentified, unnamed species from NCBI taxonomy
##as well as sub-species level.

os.system("mkdir genomes trees")

## 1. get the tree and update database
print 'RETRIEVING NCBI DATA'
print '  Downloading trees...'
os.system('python getTrees.py');
print '  Done'

##1.1 Clean trees
print '\NCLEANING TREES'
os.system('python CleanTrees.py 1');
os.system('python CleanTrees.py 2');
os.system('python CleanTrees.py 3');

print '\NCREATING DATABASE'
print '  Traversing Archaeal tree...'
os.system('python Traverse_To_Pgsql_2.py 1 1');
print '  ...Done'
with open('tempndid', 'r') as f:
    ndid = f.readline()
print '  Traversing Eukaryotic tree... start at id: %s' % ndid
os.system('python Traverse_To_Pgsql_2.py 2 %s' % ndid)
print '  ...Done'
with open('tempndid', 'r') as f:
    ndid = f.readline()
print '  Traversing Archaeae tree... start at id:%s ' % ndid
os.system('python Traverse_To_Pgsql_2.py 3 %s' % ndid)
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
print '  Deleting old newick tree files... '
os.system('rm -r /var/www/html/trees/')
print '  ...Done '
print '  Moving new newick tree files... '
os.system('mv trees/ /var/www/html/trees/')

## 4. Remove tiles
print '  Deleting old tiles... '
os.system('rm -r /var/lib/mod_tile/default/')


## 5. Create postgis index
print '  Creating index... '
os.system('python CreateIndex.py')

## 6. Restart apache, posgresql and renderd 
os.system('killall lt-renderd')
os.system('/etc/init.d/postgresql restart')
os.system('/etc/init.d/apache2 restart')
os.system('/home/ddevienne/TOOLS/mod_tile/renderd')
