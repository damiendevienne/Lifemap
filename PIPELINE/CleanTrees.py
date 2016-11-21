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


##FEB 2016

##Here we clean the trees to create the LargePublic version of LifeMap

from ete3 import Tree
from ete3 import NCBITaxa
import sys 

if (sys.argv[1]=="1"):
    t = Tree("ARCHAEA")
if (sys.argv[1]=="2"):
    t = Tree("EUKARYOTES")
if (sys.argv[1]=="3"):
    t = Tree("BACTERIA")

print len(t)
for n in t.traverse():
    if (n.rank=='species'):
        child = n.children
        for i in child:
            i.rank = 'subspecies'
    if ('Unclassified' in n.sci_name)or('unclassified' in n.sci_name)or('uncultured' in n.sci_name)or('Uncultured' in n.sci_name)or('unidentified' in n.sci_name) or ('Unidentified' in n.sci_name) or ('environmental' in n.sci_name) or (n.rank=='subspecies'):
        n.detach()        
print len(t)

if (sys.argv[1]=="1"):
    t.write(outfile = "ARCHAEA", features = ["taxid", "sci_name","common_name","rank","name"], format_root_node=True)
if (sys.argv[1]=="2"):
    t.write(outfile = "EUKARYOTES", features = ["taxid", "sci_name","common_name","rank","name"], format_root_node=True)
if (sys.argv[1]=="3"):
    t.write(outfile = "BACTERIA", features = ["taxid", "sci_name","common_name","rank","name"], format_root_node=True)
