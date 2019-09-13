#!/usr/bin/python

## This code allows storing the whole NCBI tree in solr. Useful we think.
import sys,os
from ete3 import Tree
from getTrees_fun import getTheTrees

T = getTheTrees()
t = T['1'].detach()
t.rank = 'no rank'
##traverse first time:
for n in t.traverse():
    n.path_taxid = [n.taxid];
    n.path_sci_name = [n.sci_name]
    n.path_rank = [n.rank]
    node = n
    while node.up:
        n.path_taxid.append(node.up.taxid)
        n.path_sci_name.append(node.up.sci_name)
        n.path_rank.append(node.up.rank)
        node = node.up
    # n.rank = n.rank.replace("'","''");
    # n.sci_name = n.sci_name.replace("'","''")
 

##traverse to write
jsonFullNcbi = 'ADDITIONAL.FULLNCBI.json';
addi = open(jsonFullNcbi,"w");
addi.write('[\n')
for n in t.traverse():
    addi.write("\t{\n");
    addi.write("\t\t\"taxid\":\"%s\",\n" % n.taxid);
    addi.write("\t\t\"sci_name\":\"%s\",\n" % n.sci_name);
    addi.write("\t\t\"rank\":\"%s\",\n" % n.rank);
    addi.write("\t\t\"ascend_taxids\":[");
    for k in n.path_taxid[:-1]:
        addi.write("\"%s\"," % k)
    addi.write("\"1\"],\n")   
    addi.write("\t\t\"ascend_sci_names\":[");
    for k in n.path_sci_name[:-1]:
        addi.write("\"%s\"," % k)
    addi.write("\"root\"],\n")   
    addi.write("\t\t\"ascend_ranks\":[");
    for k in n.path_rank[:-1]:
        addi.write("\"%s\"," % k)
    addi.write("\"no rank\"]\n\t},\n")   
    
##remove unwanted last character(,) of json file
addi.close()
consoleexex = 'head -n -1 ' + jsonFullNcbi + ' > temp.txt ; mv temp.txt '+ jsonFullNcbi;
os.system(consoleexex);
addi = open(jsonFullNcbi,"a");
addi.write("\t}\n]\n")
addi.close()

