#!/usr/bin/python

import psycopg2 ##for postgresql connection

##CONNECT TO POSTGRESQL/POSTGIS DATABASE
try:
    conn = psycopg2.connect("dbname='tree' user='lm' host='localhost' password='0000'")
except:
    print "I am unable to connect to the database"

print 'Creating index...'
cur = conn.cursor()
cur.execute('CREATE INDEX linesid ON lines USING GIST(way);')
cur.execute('CREATE INDEX pointsid ON points USING GIST(way);')
cur.execute('CREATE INDEX polygid ON polygons USING GIST(way);')
conn.commit()

print 'Clustering...'
cur.execute('CLUSTER lines USING linesid;')
cur.execute('CLUSTER points USING pointsid;')
cur.execute('CLUSTER polygons USING polygid;')
conn.commit()

print 'Analyzing...'
cur.execute('ANALYZE lines;')
cur.execute('ANALYZE points;')
cur.execute('ANALYZE polygons;')
conn.commit()

print 'DONE...'

