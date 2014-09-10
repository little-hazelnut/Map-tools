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
		ilist=point2grid.getlist([float(lng1),float(lat1)],[float(lng2),float(lat2)])#����node����������list
		strtmp=fid+"="+str(lng1)+"-"+str(lat1)+":"+str(lng2)+"-"+str(lat2)#��������nodeתΪ�ַ���
		#file_object.write(";"+str(ilist))
		for i in xrange(0,len(ilist)):#��list�е�����Ϊkey��nodeΪvalue����
			if(grid.has_key(str(ilist[i]))):#���������key�Ѿ�����
				if (grid[str(ilist[i])].count(strtmp)==0):#���node������
					grid[str(ilist[i])].append(strtmp)#���node
			else:#���������key������
				tmpfid=[strtmp]#���node������ʱlist
				grid.setdefault(str(ilist[i]),tmpfid)#�������key�������ֻ��һ��node��list

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