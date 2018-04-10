#!/usr/bin/python

import sys,os
from argparse import ArgumentParser, FileType ##for options handling

parser = ArgumentParser(description='Open taxonomic tree and recode it into PostGRES/PostGIS database.')
parser.add_argument('group', help='Group to look at. Can be B,A or E for Bacteria, Archaea and Eukaryotes respectively', choices=['A','B','E'])
parser.add_argument('start', help='index of the first node met in the tree', type=int)
parser.add_argument('--lang', nargs='?', const='EN', default='EN', help='Language chosen. FR for french, EN (default) for english', choices=['EN','FR'])

args = parser.parse_args()
print args

groupnb = args.group
print groupnb
