# coding=utf-8
import decimal
def imax(ilist):
	return ilist[0] if(ilist[0]>ilist[1]) else ilist[1]
def imin(ilist):
	return ilist[0] if(ilist[0]<ilist[1]) else ilist[1]
def iround(input):
	return ((int)(input/0.001))/1000.0

def remainder(input):
	return (input*100)%1==0
# x1=0.0075 #Xmin
# x2=0.0325 #Xmax
# y1=0.0175
# y2=0.0075
def getlist(point1,point2):
	grid=0.001
	halfgrid=grid/2
	x1=point1[0]#halfgrid
	x2=point2[0]#0.018
	y1=point1[1]#0.0075
	y2=point2[1]#0.0075

	ilist=[]
	#端点两个的格子
	ilist.append(str(iround(x1)+halfgrid)+","+str(iround(y1)+halfgrid))
	if str(iround(x2)+halfgrid)+","+str(iround(y2)+halfgrid) not in ilist:
		ilist.append(str(iround(x2)+halfgrid)+","+str(iround(y2)+halfgrid))
	if(x1==x2 and x1%grid==0):#与格子竖线重合 ，一条路算进两个格子。x1=0.01 x2=0.01 y1=halfgrid y2=0.025
		i=iround(imin([y1,y2]))
		while(i<=iround(imax([y1,y2]))):
			if str(iround(x1)+halfgrid)+","+str(i+halfgrid) not in ilist:
				ilist.append(str(iround(x1)+halfgrid)+","+str(i+halfgrid))
			if str(iround(x1)-halfgrid)+","+str(i+halfgrid) not in ilist:
				ilist.append(str(iround(x1)-halfgrid)+","+str(i+halfgrid))
			i=i+grid
	else:
		#两点x坐标没有跨越格子 
		if(iround(x1)==iround(x2)):
			i=iround(imin([y1,y2]))
			while(i<iround(imax([y1,y2]))):
				if str(iround(x1)+halfgrid)+","+str(i+halfgrid) not in ilist:
					ilist.append(str(iround(x1)+halfgrid)+","+str(i+halfgrid))
				i=i+grid
		#跨格子
		else:
		#与竖线必有相交
			i=iround(imin([x1,x2]))
			while(i<iround(imax([x1,x2]))):#遍历与竖线交点
				i=i+grid
				i=((int)(i/0.001))/1000.0
				y=(y2-y1)/(x2-x1)*(i-x1)+y1#两点式  x1不能等于x2
				if(y%grid==0):#线过格子交点根据斜率取该交点左下和右上，或右下左上格子。如 x1=halfgrid x2=0.025	y1=halfgrid y2=0.025
					if((y2-y1)/(x2-x1)>0):#斜率大于0，取该交点左下和右上
						if str(i-halfgrid)+","+str(iround(y)-halfgrid) not in ilist:
							ilist.append(str(i-halfgrid)+","+str(iround(y)-halfgrid))
						if str(i+halfgrid)+","+str(iround(y)+halfgrid) not in ilist:
							ilist.append(str(i+halfgrid)+","+str(iround(y)+halfgrid))
					if((y2-y1)/(x2-x1)<0):#斜率小于0，取该交点右下左上格子
						if str(i-halfgrid)+","+str(iround(y)+halfgrid) not in ilist:
							ilist.append(str(i-halfgrid)+","+str(iround(y)+halfgrid))
						if str(i+halfgrid)+","+str(iround(y)+halfgrid) not in ilist:
							ilist.append(str(i+halfgrid)+","+str(iround(y)-halfgrid))
				
				else:#不过交点的情况
					if str(i-halfgrid)+","+str(iround(y)+halfgrid) not in ilist:
						ilist.append(str(i-halfgrid)+","+str(iround(y)+halfgrid))
					if str(i+halfgrid)+","+str(iround(y)+halfgrid) not in ilist:
						ilist.append(str(i+halfgrid)+","+str(iround(y)+halfgrid))
						
			i=iround(imin([y1,y2]))
			while(i<iround(imax([y1,y2]))):#遍历与竖线交点
				i=i+grid
				i=((int)(i/0.001))/1000.0
				x=(x2-x1)/(y2-y1)*(i-y1)+x1#两点式  
				if(x%grid==0):#线过格子交点根据斜率取该交点左下和右上，或右下左上格子。如 x1=halfgrid x2=0.025	y1=halfgrid y2=0.025
					if((y2-y1)/(x2-x1)>0):#斜率大于0，取该交点左下和右上
						if str(iround(x)+halfgrid)+","+str(i+halfgrid) not in ilist:
							ilist.append(str(iround(x)+halfgrid)+","+str(i+halfgrid))
						if str(iround(x)-halfgrid)+","+str(i-halfgrid) not in ilist:
							ilist.append(str(iround(x)-halfgrid)+","+str(i-halfgrid))
					if((y2-y1)/(x2-x1)<0):#斜率小于0，取该交点右下左上格子
						if str(iround(x)+halfgrid)+","+str(i-halfgrid) not in ilist:
							ilist.append(str(iround(x)+halfgrid)+","+str(i-halfgrid))
						if str(iround(x)-halfgrid)+","+str(i+halfgrid) not in ilist:
							ilist.append(str(iround(x)-halfgrid)+","+str(i+halfgrid))
				
				else:#不过交点的情况
					if str(iround(x)+halfgrid)+","+str(i+halfgrid) not in ilist:
						ilist.append(str(iround(x)+halfgrid)+","+str(i+halfgrid))
					if str(iround(x)+halfgrid)+","+str(i-halfgrid) not in ilist:
						ilist.append(str(iround(x)+halfgrid)+","+str(i-halfgrid))


	return ilist
