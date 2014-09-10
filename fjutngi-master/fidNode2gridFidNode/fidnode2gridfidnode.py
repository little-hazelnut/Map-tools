# coding=utf-8
import point2grid
import shapefile
from GmapOffset import *
import time 
start = time.clock()
gmapOffset = GmapOffset()
# print gmapOffset.wgs2Mars(119.355759,26.1078699)
grid={}

file_object = open('all2_gridFidNode.txt', 'w')
tag=0
offset_dict={}



for line in open('all2_fidNode.txt'):
	tag = tag + 1
	if(tag%100 ==0 ):
		print tag
	fid,points = line.strip().split('|')
	pointArr = points.split(':')
	for i in xrange(0,len(pointArr)-1):
		lng1,lat1 = pointArr[i].split(',')
		lng2,lat2 = pointArr[i+1].split(',')
		try:
			lng1,lat1 = gmapOffset.mars2Wgs(float(lng1),float(lat1))
			lng2,lat2 = gmapOffset.mars2Wgs(float(lng2),float(lat2))
		except:
			print 'error'
		ilist=point2grid.getlist([float(lng1),float(lat1)],[float(lng2),float(lat2)])#两个node经过的网格list
		strtmp=fid+"="+str(lng1)+"-"+str(lat1)+":"+str(lng2)+"-"+str(lat2)#将这两个node转为字符串
		#file_object.write(";"+str(ilist))
		for i in xrange(0,len(ilist)):#以list中的网格为key，node为value保存
			if(grid.has_key(str(ilist[i]))):#如果该网格key已经存在
				if (grid[str(ilist[i])].count(strtmp)==0):#如果node不存在
					grid[str(ilist[i])].append(strtmp)#添加node
			else:#如果该网格key不存在
				tmpfid=[strtmp]#添加node进入临时list
				grid.setdefault(str(ilist[i]),tmpfid)#添加网格key，并添加只有一个node的list

##################################################################################################
print '2test'
for k in grid:
	file_object.write(k)
	file_object.write("|")
	for j in xrange(0,len(grid[k])):
		file_object.write(grid[k][j])
		if(j<len(grid[k])-1):
			file_object.write(",")
	file_object.write("\n")

file_object.close( )
end = time.clock() 
print end-start 
#for 
#  Read the 8th point in the 4th shape