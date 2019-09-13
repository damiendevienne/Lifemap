#!/usr/bin/python

## This code allows storing the whole NCBI tree in solr. Useful we think.
import sys,os
from ete3 import Tree
import numpy as np
from getTrees_fun import getTheTrees

T = getTheTrees()
t = T['1'].detach()
t.rank = 'no rank'
##traverse first time:
for n in t.traverse():
    n.path = [];
    node = n
    while node.up:
        n.path.append(node.up.taxid)
        node = node.up
    ##reformat the texts
    n.common_name_all = ', '.join(n.common_name)
    n.common_name = n.common_name[0] if len(n.common_name)>0 else ""
    ##we create a 'long' common name. the common name going to db is only the first of the list 
    n.common_name = n.common_name.replace("'","''");
    n.rank = n.rank.replace("'","''");
    n.sci_name = n.sci_name.replace("'","''")
    n.authority = n.authority.replace("'","''")
    n.synonym = n.synonym.replace("'","''")
 

##traverse to write
jsonFullNcbi = 'ADDITIONAL.FULLNCBI.json';
addi = open(jsonFullNcbi,"w");
addi.write('[\n')
for n in t.traverse():
    addi.write("\t{\n");
    addi.write("\t\t\"taxid\":\"%s\",\n" % n.taxid);
    addi.write("\t\t\"ascend\":[");
    for k in n.path[:-1]:
        addi.write("%s," % k)
    addi.write("1],\n")   
    addi.write("\t\t\"sci_name\":\"%s\",\n" % n.sci_name);
    addi.write("\t\t\"authority\":\"%s\",\n" % n.authority);
    addi.write("\t\t\"synonym\":\"%s\",\n" % n.synonym);
    addi.write("\t\t\"common_name\":\"%s\",\n" % n.common_name);
    addi.write("\t\t\"common_name_all\":\"%s\",\n" % n.common_name_all);
    addi.write("\t\t\"rank\":\"%s\"\n\t},\n" % n.rank);
    
##remove unwanted last character(,) of json file
addi.close()
consoleexex = 'head -n -1 ' + jsonFullNcbi + ' > temp.txt ; mv temp.txt '+ jsonFullNcbi;
os.system(consoleexex);
addi = open(jsonFullNcbi,"a");
addi.write("\t}\n]\n")
addi.close()

