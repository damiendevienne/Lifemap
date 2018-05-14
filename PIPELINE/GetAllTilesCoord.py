#!/usr/bin/python
import math

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return [xtile, ytile]

zoom = False
lat = False
lon = False

coo = open("XYZcoordinates", "w"); ##output

def getXYZ(fi):
	with open(fi) as f:  
		for line in f:
			tmp = line.split(":")
			if (len(tmp)>1):
				key = tmp[0].replace("\"", "").replace(" ","")
				val = tmp[1].replace("\"", "").replace(" ","").replace(",","").rstrip()
				if (key=='zoom'):
					zoom = val;
				if (key=='lat'):
					lat = val
				if (key=='lon'):
					lon = val;
					#do stuff
					if (zoom<=15):
						xy = deg2num(float(lat), float(lon), float(zoom))
						coo.write("%d %d %s\n" % (xy[0], xy[1],zoom))
					zoom = False
					lat = False
					lon = False

getXYZ('TreeFeatures1.json')
getXYZ('TreeFeatures2.json')
getXYZ('TreeFeatures3.json')

coo.close();
