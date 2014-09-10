# coding=gbk
import math

gridFidNode = {}
for line in open('gridFidNode_data/cy_gridFidNode.txt'):
	grid,fidNode = line.split('|')
	gridFidNode[grid] = fidNode
def iround(input):
	return ((int)(input/0.001))/1000.0
def	calpoint2line(x0,y0,x1,y1,x,y):
	return abs((y1-y0)*x+(x0-x1)*y+x1*y0-y1*x0)/math.sqrt((y1-y0)**2+(x0-x1)**2)
def getminfid(fidNodes,x,y):
	#print fidNodes
	dismin=5000
	#print fidNodes
	if(len(fidNodes)>0):
		fidNodelist=fidNodes.split(',')
		#print nodelist
		for l in xrange(0,len(fidNodelist)):
			fid,nodeList = fidNodelist[l].split('=')
			sublist=nodeList.split(':')
			xyxy0=sublist[0].split('-')
			x0=xyxy0[0]
			y0=xyxy0[1]
			xyxy1=sublist[1].split('-')
			x1=xyxy1[0]
			y1=xyxy1[1]
			dis=calpoint2line(float(x0),float(y0),float(x1),float(y1),x,y)
			if(dismin>dis):
				dismin=dis
				xmin0=x0
				ymin0=y0
				xmin1=x1
				ymin1=y1
				rfid = fid
		#print xmin1
		#print ymin1
		#print dismin*100000
		if dismin*100000<35:
			return rfid
		else:
			return 'null'
	else:
		return 'null'
def addNodes(fidNodes,gridkey):
	try:
		newNodes = gridFidNode[gridkey].strip()
	except:
		newNodes = ''
	if(newNodes!=''):
		if(fidNodes!=''):
			return fidNodes + ',' +newNodes
		else:
			return newNodes
	else:
		return fidNodes
def getfid(x,y):
	xround = iround(x)
	yround = iround(y)
	fidNodes=''
	xcenter=xround+0.0005
	ycenter=yround+0.0005
	if(x < xcenter and y < ycenter):
		fidNodes = addNodes(fidNodes,str(xcenter)+','+str(ycenter))
		fidNodes = addNodes(fidNodes,str(xcenter)+','+str(ycenter-0.001))
		fidNodes = addNodes(fidNodes,str(xcenter-0.001)+','+str(ycenter-0.001))		
		fidNodes = addNodes(fidNodes,str(xcenter-0.001)+','+str(ycenter))

	elif(x < xcenter and y > ycenter):
		fidNodes = addNodes(fidNodes,str(xcenter)+','+str(ycenter))
		fidNodes = addNodes(fidNodes,str(xcenter)+','+str(ycenter+0.001))
		fidNodes = addNodes(fidNodes,str(xcenter-0.001)+','+str(ycenter+0.001))		
		fidNodes = addNodes(fidNodes,str(xcenter-0.001)+','+str(ycenter))
	elif(x >xcenter and y > ycenter):
		fidNodes = addNodes(fidNodes,str(xcenter)+','+str(ycenter))
		fidNodes = addNodes(fidNodes,str(xcenter)+','+str(ycenter+0.001))
		fidNodes = addNodes(fidNodes,str(xcenter+0.001)+','+str(ycenter+0.001))		
		fidNodes = addNodes(fidNodes,str(xcenter+0.001)+','+str(ycenter))	
	elif(x >xcenter and y < ycenter):
		fidNodes = addNodes(fidNodes,str(xcenter)+','+str(ycenter))
		fidNodes = addNodes(fidNodes,str(xcenter)+','+str(ycenter-0.001))
		fidNodes = addNodes(fidNodes,str(xcenter+0.001)+','+str(ycenter-0.001))		
		fidNodes = addNodes(fidNodes,str(xcenter+0.001)+','+str(ycenter))	
	return getminfid(fidNodes,x,y)		

# if matched return fid else return 'null'
#print getfid(119.294381,26.078259)
print 'start data preprocessing...'