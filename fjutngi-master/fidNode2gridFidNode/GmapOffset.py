class GmapOffset:
	def __init__(self):
		self.offset_dict = {}
		for line in open('FJ_OFFSET.txt'):
			lng100,lat100,lngOffset,latOffset = line.replace('\n','').split(',')
			self.offset_dict[lng100+lat100] = lngOffset+','+latOffset

	def wgs2Mars(self, lng, lat):
		lnground = int(lng*100)
		latround = int(lat*100)
		lnglat = self.offset_dict[str(lnground) + str(latround)].split(',')
		lng_offset = lng + float(lnglat[0])
		lat_offset = lat + float(lnglat[1])
		return lng_offset,lat_offset
	
	def mars2Wgs(self, lng, lat):
		lnground = int(lng*100)
		latround = int(lat*100)
		lnglat = self.offset_dict[str(lnground) + str(latround)].split(',')
		lng_offset = lng - float(lnglat[0])
		lat_offset = lat - float(lnglat[1])
		return lng_offset,lat_offset


