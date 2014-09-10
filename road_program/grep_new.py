#-*- coding:utf-8 -*-
#grep 新版 
#使用openDir : 加入循环读取一个文件夹中指定后缀数据文件的功能

import matching
import openDir
import os.path

r_filename = 'E:\FZcity(119.113,26.155-119.684,25.904)'
w_dir = ''
suffix = 'YangZhongRoad.txt'
file_arr = []

if(os.path.isfile(r_filename)):
	file_arr.append(r_filename)
	#print 'file'
else:
	file_arr = openDir.traDir(r_filename)
	#print 'dir'

	
for k,v in enumerate(file_arr):
	print k,v;

for k,v in enumerate(file_arr):
	if(k>=0):
		#w_filename = '20131201pushang_bridge1.txt'
		w_filename = w_dir + os.path.basename(v).split(".")[0] + suffix
		print 'writing: '+ w_filename
		file = open(w_filename,'w')
		for line in open(v):
			linearr = line.split(',')
			lng = float(linearr[4])
			lat = float(linearr[5])
			fid = matching.getfid(lng,lat)
			if(fid == 'cy9807' or fid == 'cy9808' or fid == 'cy10260' or fid == 'cy10263' or fid == 'cy10314' or fid == 'cy10316'):
					file.write(line)
		print 'ok'
		
#晋安南路（cy） 40
#cy9118 9119 9140 9141 9148 9167 9169 9275
#实验路段：all

#洋中路（cy） 40
#cy9807 9808 10260 10261 10263 10264 10314 10316
#实验路段：cy9807 9808 10260 10263 10314 10316