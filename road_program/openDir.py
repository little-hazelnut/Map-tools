import os
import re

type = "txt"
rr = re.compile( "\.%s$" %type , re.I )
arr = []

def traDir(path):
	for root,dirs,files in os.walk(path):
		for fn in files:
			if rr.search(fn):
				arr.append(root+'/'+fn)
				#print root,fn

	return arr			


#for k,v in enumerate(fn_arr):
	#print k,v
	
	