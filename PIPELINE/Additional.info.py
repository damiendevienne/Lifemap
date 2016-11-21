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
from ete3 import Tree

groupnb = sys.argv[1]; ##will be written

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
##                       NOW WE RETRIEVE WHAT WE WILL PUT IN THE JSON FILES
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
if (groupnb=="1"):
    os.system("wget ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt")
    os.system("wget ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt")
    os.system("mv eukaryotes.txt prokaryotes.txt genomes/")
    t = Tree("ARCHAEA")
if (groupnb=="2"):
    t = Tree("EUKARYOTES")
if (groupnb=="3"):
    t = Tree("BACTERIA")

class genom(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, taxid,size,gc,status):
        self.taxid = [taxid]
        self.size = [size]
        self.gc =[gc]
        self.status =[status]
    def __str__(self):
        return "%d elements " % len(self.taxid)
    def __repr__(self):
        return "%d elements " % len(self.taxid)
    def len(self):
        return self.__len__()
    def append(self,t,si,g,st):
        self.taxid.append(t)
        self.size.append(si)
        self.gc.append(g)
        self.status.append(st)

def make_genom(taxid, size,gc, status):
    gen = genom(taxid, size,gc, status)
    return gen

Genomes = {}
with open("genomes/eukaryotes.txt", "r") as f:
    for line in f:
        temp = line.split('\t')
        if temp[1] in Genomes:
            Genomes[temp[1]].append(temp[1], temp[6], temp[7], temp[18])
        else:
            Genomes.update({temp[1]:genom(temp[1], temp[6], temp[7], temp[18])})
with open("genomes/prokaryotes.txt", "r") as f:
    for line in f:
        temp = line.split('\t')
        if temp[1] in Genomes:
            Genomes[temp[1]].append(temp[1], temp[6], temp[7], temp[18])
        else:
            Genomes.update({temp[1]:genom(temp[1], temp[6], temp[7], temp[18])})


##traverse first time:
for n in t.traverse():
    n.path = [];
    try:
        n.nbgenomes+=0
    except AttributeError:
        n.nbgenomes = 0
    if n.taxid in Genomes:
        nb = len(Genomes[n.taxid].gc)
        try:
            n.nbgenomes += nb
        except AttributeError:
            n.nbgenomes = 0
    node = n
    while node.up:
        try:
            node.up.nbgenomes += n.nbgenomes
        except AttributeError:
            node.up.nbgenomes = 0
        n.path.append(node.up.taxid)
        node = node.up

##traverse to write
jsonAddi = 'ADDITIONAL.'+ groupnb + '.json';
addi = open(jsonAddi,"w");
addi.write('[\n')
for n in t.traverse():
    addi.write("\t{\n");
    addi.write("\t\t\"taxid\":\"%s\",\n" % n.taxid);
    addi.write("\t\t\"ascend\":[");
    for k in n.path:
        addi.write("%s," % k)
    addi.write("0],\n")   
    addi.write("\t\t\"genomes\":\"%d\"\n\t},\n" % n.nbgenomes);
    
##remove unwanted last character(,) of json file
addi.close()
consoleexex = 'head -n -1 ' + jsonAddi + ' > temp.txt ; mv temp.txt '+ jsonAddi;
os.system(consoleexex);
addi = open(jsonAddi,"a");
addi.write("\t}\n]\n")
addi.close()

