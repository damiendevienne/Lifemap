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


from ete3 import Tree
from ete3 import NCBITaxa
ncbi = NCBITaxa()
ncbi.update_taxonomy_database()
print(">>> Downloading Archaeal tree...")
tarc = ncbi.get_descendant_taxa(2157, return_tree=True)
print(">>> DONE")
print("\n>>> Writing trees to files...")
tarc.write(outfile = "ARCHAEA", features = ["name", "taxid", "sci_name","common_name","rank"], format_root_node=True)
print("\n>>> Downloading Bacterial tree...")
tbac = ncbi.get_descendant_taxa(2, return_tree=True)
print(">>> DONE")
print("\n>>> Writing trees to files...")
tbac.write(outfile = "BACTERIA", features = ["name", "taxid", "sci_name","common_name","rank"], format_root_node=True)
print("\n>>> Downloading Euka tree...")
teuc = ncbi.get_descendant_taxa(2759, return_tree=True)
print(">>> DONE")
print("\n>>> Writing trees to files...")
teuc.write(outfile = "EUKARYOTES", features = ["name", "taxid", "sci_name","common_name","rank"], format_root_node=True)
print(">>> DONE")
