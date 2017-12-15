

def transform(graph,tracks):
	transform=[]
	min_list=[]
	total_time=0
	for track in tracks:
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
		transform.append(tracklist)
		min_list.append(track_time)
		total_time+= track_time
	return transform,total_time,min_list


def unique(dict):
	apct=[]					#all possible critical tracks
	uct=[]					#unique critical tracks
	for x in dict:
		if dict[x]['importance']=='critical':
			for y in dict[x]['neighbours']:
				n_input=[[x,y[0]],float(y[1])]
				i_input =[[y[0],x],float(y[1])]
				apct.append(i_input)
				apct.append(n_input)
				if i_input not in uct:
					uct.append(n_input)
	return apct,uct

def score(graph,tracks,apct,uct):
	bkv=[]					#bereden kritieke verbindingen				
	transformed= transform(graph,tracks)[0]
	minlist= transform(graph,tracks)[1]
	time= minlist= transform(graph,tracks)[2]
	t= len(tracks)
	for i in range(t):
		track= transformed[i][0]
		clist=[x for x in track if x in apct]
		for x in clist:
			inverse_x = [[x[0][1],x[0][0]],x[1]]
			if x not in bkv:
				if inverse_x not in bkv:
					bkv.append(x)
	p= len(bkv)/len(uct)
	S= 0#p*10000 - (t*20 + min/100000)
	# print(bkv)
	return S,len(bkv),min
