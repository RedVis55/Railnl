


class Tracks(object):
	"""docstring for Tracks"""
	def __init__(self, tracks):
		self.tracks= tracks
		self.score = 0
		self.transform= []
		self.total_time=0
		self.min_list=[]

	def transform_tracks(self,stationclass,graph):
		for track in self.tracks:
			tracklist=[]
			track_time=0
			for i in range(len(track)):
				if i+1<len(track):
					a= track[i]
					b= track[i+1]
					time= float(graph[a][b]['weight'])
					tracklist.append([[a,b],time])
					track_time+= time
			tracklist=[tracklist,track_time]
			#tracklist.append(track_time)
			self.transform.append(tracklist)
			self.min_list.append(track_time)
			self.total_time+= track_time
		return self.transform

	def compute_score(self,apct,uct):
		bkv=[]					#bereden kritieke verbindingen				
		t= len(self.transform)
		for i in range(t):
			track= self.transform[i]
			print(track)
			clist=[x for x in track if x in apct]
			print(clist)
			for x in clist:
				inverse_x = [[x[0][1],x[0][0]],x[1]]
				if x not in bkv:
					if inverse_x not in bkv:
						bkv.append(x)
		p= len(bkv)/len(uct)
		self.score= p*10000 - (t*20 + self.total_time/100000)
		print(bkv)
		print(self.score,bkv,len(bkv),self.min_list)
		return self.score,len(bkv),min

