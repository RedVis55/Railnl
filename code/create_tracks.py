import copy
from random import randint

def ndict(graph,all_nodes,dict,step):
	list=[]
	for x in dict[step]:
		for y in graph[x]:
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
	lenght= len(bfs)
	for i in range(lenght-1):
		for parent in bfs[i]:
			for child in bfs[i+1]:
				if child in graph[parent]:
					parent_children.append([parent,child])
	return parent_children

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

def timelimit(graph,track):
	track_time=0
	for i in range(len(track)):
		if i+1<len(track):
			a= track[i]
			b= track[i+1]
			time= float(graph[a][b]['weight'])
			track_time+= time
	return track_time

def combine_all_timelimit(graph,station,limit):
	""" Get all possible tracks from the input station to all the other stations in 
	network. Be cautious using the timelimit. Using 'Utrecht Centraal' and a limit
	of 180 minutes can cause runtimes of 10 minutes """
	finallist= all_shortest_routes(graph,station)
	templist= copy.copy(finallist)
	for x in templist:
		last= x[len(x)-1:]
		for y in all_shortest_routes(graph,last[0]):
			new=x+y[1:]
			if timelimit(graph,new)<=limit:
				if y[0]!=station and y[1]!=station and len([l for l in y[1:] if l in x])==0:
					if new not in templist:
						templist.append(new)
	limit=[x for x in templist if timelimit(graph,x)<=limit]
	return limit

def firstRandom(graph,station,allstations):
	allN= pathcount(graph,station,15)
	n_list= [x for x in allN[1] if x not in allstations]
	if n_list==[]:
		return None
	else:
		index_len= len(n_list)-1
		random_index=randint(0,index_len)
		return n_list[random_index]

def pathsRandom(graph,stationA):
	path= [stationA]
	totdistance= 0
	station= stationA
	for i in range(20):
		random_path= firstRandom(graph,station,path)
		if random_path != None:
			distance= float(graph[station][random_path]['weight'])
			if totdistance + distance > 120:
				return path
			totdistance += distance

			path.append(random_path)
		else:
			return path


def tracksRandom(graph,r):
    len_nodes= len(graph.nodes())
    tracks=[]
    for i in range(r):
        random_index= randint(0,len_nodes-1)
        random_node= [x for x in graph.nodes()][random_index]
        random_track= pathsRandom(graph,random_node)
        tracks.append(random_track)
    return tracks
