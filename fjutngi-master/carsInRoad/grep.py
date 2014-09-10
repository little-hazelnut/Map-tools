import matching
w_filename = '20131220JvYuanZhouTe_bridge_zy558.txt'
r_filename = 'E:\FZcity(119.113,26.155-119.684,25.904)\\20131220.txt'
print 'writing:'+w_filename
file = open(w_filename,'w')
for line in open(r_filename):
	linearr = line.split(',')
	lng = float(linearr[4])
	lat = float(linearr[5])
	fid = matching.getfid(lng,lat)
	if(fid=='zy558'):
		file.write(line)
print 'ok'
