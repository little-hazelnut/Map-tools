#-*- coding:utf-8 -*-
#grep 新版 
#使用openDir : 加入循环读取一个文件夹中指定后缀数据文件的功能

import matching
import openDir
import os.path

r_filename = 'M:\FZcity(119.113,26.155-119.684,25.904)'
w_dir = ''
suffix = 'DaoShanWest_Road.txt'
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
			if(fid == 'cy9793' or fid == 'cy9794' or fid == 'cy9937' or fid == 'cy9938'):
				file.write(line)
		print 'ok'