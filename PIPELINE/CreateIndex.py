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


import psycopg2 ##for postgresql connection

##CONNECT TO POSTGRESQL/POSTGIS DATABASE
try:
    conn = psycopg2.connect("dbname='tol' user='ddevienne' host='localhost' password='damdam81'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
cur.execute('CREATE INDEX linesid ON lines USING GIST(way);')
cur.execute('CREATE INDEX pointsid ON points USING GIST(way);')
cur.execute('CREATE INDEX polygid ON polygons USING GIST(way);')
conn.commit()

cur.execute('CLUSTER lines USING linesid;')
cur.execute('CLUSTER points USING pointsid;')
cur.execute('CLUSTER polygons USING polygid;')
conn.commit()

cur.execute('ANALYZE lines;')
cur.execute('ANALYZE points;')
cur.execute('ANALYZE polygons;')
conn.commit()

