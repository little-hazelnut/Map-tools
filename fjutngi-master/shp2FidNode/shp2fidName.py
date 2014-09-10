#coding = utf-8
import shapefile
import sys
#shp = sys.input()
#shpList = ['gd','gs','ks','zy',cy]
shpList = ['cy']
file = open('cy_fidName.txt','w')
for shp in shpList:
	sf = shapefile.Reader('data/'+ shp +'.shp')
	shapes = sf.shapes()
	records = sf.records()

	#print shapes[0].parts
	#print shapes[0].points
	# for line in shapes:
		# file.write(str(line.points)+'\n')
	# print len(shapes)
	records = sf.records()
	print len(shapes)
	for i in xrange(0,len(shapes)):
		pointStr=''
		for point in shapes[i].points:
			x,y = point
			pointStr = pointStr +str(x) + ',' + str(y) + ':'
		#file.write('zy'+str(records[i][0])+'|'+pointStr[0:-1]+'\n')
		file.write(shp+str(i)+'|'+records[i][2]+'\n')
# kprint records[1]
# print records[2]
# print len(records)
