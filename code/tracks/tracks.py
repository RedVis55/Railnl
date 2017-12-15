def ndict(graph,all_nodes,dict,step):
		list=[]
		for x in dict[step]:
			for y in graph.graph[x]:
				if y not in all_nodes:
					list.append(y)
					all_nodes.append(y)
		dict[step+1]=list
		step += 1
		return all_nodes,dict,step

def pathcount(graph,node,nrange):
	dict={}
	all_nodes=[node]
	dict[0]=[node]
	step=0
	for step in range(nrange):
		if step==nrange-1:
			return dict
		if dict[step]==[]:
			return dict
		else: 
			ndict(graph,all_nodes,dict,step)


def pathmaker(graph,bfs):
	parent_children=[]
	parent_children2=[]
	lenght= len(bfs)
	for i in range(lenght-1):
		for parent in bfs[i]:
		# print(parent)
			for child in bfs[i+1]:
				if child in graph[parent]:
					parent_children.append([parent+child])
					parent_children2.append([parent,child])
	return parent_children2


def all_shortest_routes(graph,station):
	bfs=pathcount(graph,station,20)
	list1=[x for x in pathmaker(graph,bfs)]
	list2=[x for x in pathmaker(graph,bfs)]
	list3=[]
	for x in list1:
		l_index=len(x)-1
		first=x[:l_index]
		second=x[l_index:]
		for y in list2:
			if y[0] == second[0]:
				new_c=first+y
				list1.append(new_c)
				#print(new_c)#x,y,first,second,
	for x in list1:
		if x[0]==station:
			list3.append(x) 
	return list3


def combine_all(graph,station):
	finallist= all_shortest_routes(graph,station)
	templist= copy.copy(finallist)
	for x in finallist:
		last= x[len(x)-1:]
		for y in all_shortest_routes(graph,last[0]):
			if y[0]!=station and y[1]!=station and len([l for l in y[1:] if l in x])==0:
				new=x+y[1:]
				if new not in templist:
					templist.append(new)
	return templist

# def random_track(start,connectionlist):
# 	tracks= self.all_shortest_routes(start)
# 	track_index = len(tracks)
# 	track_random = tracks[randint(0,track_index)]
# 	track= track_random

# 	tracklist=[]
# 	for i in range(len(track)):
# 			if i+1<len(track):
# 				tracklist.append([track[i],track[i+1]])
# 	track_w=[[[x[0],x[1]],float(x[2])] for x in connectionlist if [x[0],x[1]] in tracklist or [x[1],x[0]] in tracklist]

# 	nontracklist=[]
# 	for x in connectionlist:
# 		if [x[0],x[1]] not in track and [x[1],x[0]] not in tracklist:
# 			nontracklist.append([[x[0],x[1]],x[2]])
# 	time= sum([float(x[1]) for x in track_w])
# 	final_track=track_w,time        
# 	return tracklist,nontracklist,track_w,time,final_track


	# def unique(dict):
	# 	apct=[]					#all possible critical tracks
	# 	uct=[]					#unique critical tracks
	# 	for x in dict:
	# 		if dict[x]['importance']=='critical':
	# 			for y in dict[x]['neighbours']:
	# 				n_input=[[x,y[0]],float(y[1])]
	# 				i_input =[[y[0],x],float(y[1])]
	# 				apct.append(i_input)
	# 				apct.append(n_input)
	# 				if i_input not in uct:
	# 					uct.append(n_input)
	# 	return apct,uct		

	# def score(tracks,apct,uct):
	# 	bkv=[]					#bereden kritieke verbindingen				
	# 	min=0
	# 	minlist=[]
	# 	t= len(tracks)
	# 	for i in range(t):
	# 		min += tracks[i][1]
	# 		minlist.append(tracks[i][1])
	# 		track= tracks[i][0]
	# 		clist=[x for x in track if x in apct]
	# 		for x in clist:
	# 			inverse_x = [[x[0][1],x[0][0]],x[1]]
	# 			if x not in bkv:
	# 				if inverse_x not in bkv:
	# 					bkv.append(x)
	# 	p= len(bkv)/len(uct)
	# 	S= p*10000 - (t*20 + min/100000)
	# 	# print(bkv)
	# 	return S,len(bkv),min


# (	[[['Assen', 'Zwolle'], 40.0], [['Groningen', 'Assen'], 17.0], 
# 	[['Utrecht Centraal', 'Amersfoort'], 14.0], [['Utrecht Centraal', 'Schiphol Airport'], 33.0], 
# 	[['Zwolle', 'Amersfoort'], 35.0]]
# 	, 139.0)

