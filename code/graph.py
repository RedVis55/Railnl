import networkx as nx
import station_class as st
import matplotlib.pyplot as plt
import gc
import copy


def timelimit(graph,track):
	track_time=0
	for i in range(len(track)):
		if i+1<len(track):
			a= track[i]
			b= track[i+1]
			time= float(graph[a][b]['weight'])
			track_time+= time
	print(track_time)


class Graph(): #object
	""" The instance of this class is a graph network"""

	def __init__(self, stationClass):
		""" ...... """
		self.stationClass = stationClass
		stations= [obj.name for obj in gc.get_objects() if isinstance(obj, stationClass)]
		locations= [(obj.name,obj.location) for obj in gc.get_objects() if isinstance(obj, stationClass)]
		double_connections= [(obj.name,n[0],n[1]) for obj in gc.get_objects() if isinstance(obj, stationClass) for n in obj.neighbours]
		
		self.graph = nx.Graph()
		self.graph.add_nodes_from(stations)
		for a,b,w in double_connections:
			if self.graph.has_edge(a,b)==False:
				self.graph.add_edge(a,b, weight=w)
		for n,p in locations:
			self.graph.node[n]['pos']=p

	def information(self):
		"""Returns the amount of nodes and the nodes themselves """
		return '{} {} {} {} {}'.format('There are',len(self.graph.nodes()),'nodes','\nNodes:',self.graph.nodes())


	def draw_choice(self,stationClass,option):
		""" This functions will create a visualisation of the graph. The input is the dict
			of the class Station
		 """
		graphdict={}
		locations= [(obj.name,obj.location) for obj in gc.get_objects() if isinstance(obj, stationClass)]
		graphdict= {x[0]:x[1] for x in locations}

		c_list= [obj.name for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='critical']
		nc_list= [obj.name for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='not critical']
		
		nx.draw(self.graph, graphdict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
		nx.draw_networkx_nodes(self.graph,graphdict,node_size=30,nodelist=c_list,node_color='lightsalmon')
		nx.draw_networkx_nodes(self.graph,graphdict,node_size=20,nodelist=nc_list,node_color='lightgrey')

		if option=='standard':
			labels= {obj.name:obj.label for obj in gc.get_objects() if isinstance(obj, st.Station)}
		elif option=='critical':
			labels= {obj.name:obj.label for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='critical'}
		elif option[0]=='track':
			tracks= option[1]
			for x in tracks:

				track= x[0]
				time= x[1]
				tracklist=[]
				templist=[]
				edge_labels={}
				for y in track:
					templist.append(y[0][0])
					templist.append(y[0][1])
					edge_labels[(y[0][0],y[0][1])]=y[1]
				tracklist= set(templist)
				t_labels= {obj.name:obj.label for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.name in tracklist}
				r_labels= {obj.name:obj.label for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='critical' and obj.name not in t_labels}
				
				nx.draw(self.graph, graphdict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
				nx.draw_networkx_nodes(self.graph,graphdict,node_size=30,nodelist=c_list,node_color='lightsalmon')
				nx.draw_networkx_nodes(self.graph,graphdict,node_size=20,nodelist=nc_list,node_color='lightgrey')
			
				nx.draw_networkx_edges(self.graph, graphdict,edgelist=edge_labels,width=0.5, edge_color='blue', style='solid',with_label=True)
				nx.draw_networkx_edge_labels(self.graph, graphdict,edge_labels=edge_labels,font_size=6)
				nx.draw_networkx_labels(self.graph,graphdict,t_labels,font_size=8,font_weight='bold')
				nx.draw_networkx_labels(self.graph,graphdict,r_labels,font_size=8,font_weight='normal')
				plt.show(self.graph)

		if 'labels' in locals():
			nx.draw_networkx_labels(self.graph,graphdict,labels,font_size=8,font_weight='normal')
			edge_labels = nx.get_edge_attributes(self.graph,'weight')
			#nx.draw_networkx_edge_labels(self.graph, graphdict,edge_labels=edge_labels,font_size=6)
			nx.draw_networkx_edges(self.graph, graphdict, edge_labels=edge_labels, width=0.1, edge_color='k', style='solid')
			plt.show(self.graph)

	def ndict(self,all_nodes,dict,step):
		list=[]
		for x in dict[step]:
			for y in self.graph[x]:
				if y not in all_nodes:
					list.append(y)
					all_nodes.append(y)
		dict[step+1]=list
		step += 1
		return all_nodes,dict,step

	def pathcount(self,node,nrange):
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
				self.ndict(all_nodes,dict,step)


	def pathmaker(self,bfs):
		parent_children=[]
		parent_children2=[]
		lenght= len(bfs)
		for i in range(lenght-1):
			for parent in bfs[i]:
			# print(parent)
				for child in bfs[i+1]:
					if child in self.graph[parent]:
						parent_children.append([parent+child])
						parent_children2.append([parent,child])
		return parent_children2


	def all_shortest_routes(self,station):
		bfs=self.pathcount(station,20)
		list1=[x for x in self.pathmaker(bfs)]
		list2=[x for x in self.pathmaker(bfs)]
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



	def combine_all(self,station):
		finallist= self.all_shortest_routes(station)
		templist= copy.copy(finallist)
		for x in finallist:
			last= x[len(x)-1:]
			for y in self.all_shortest_routes(last[0]):
				if y[0]!=station and y[1]!=station and len([l for l in y[1:] if l in x])==0:
					new=x+y[1:]
					if new not in templist:
						templist.append(new)
		return templist

	def timelimit(self,track):
		track_time=0
		for i in range(len(track)):
			if i+1<len(track):
				a= track[i]
				b= track[i+1]
				time= float(self.graph[a][b]['weight'])
				track_time+= time
		return track_time

	def combine_all_timelimit(self,station,limit):
		finallist= self.all_shortest_routes(station)
		templist= copy.copy(finallist)
		for x in templist:
			last= x[len(x)-1:]
			for y in self.all_shortest_routes(last[0]):
				new=x+y[1:]
				if self.timelimit(new)<=limit:
					if y[0]!=station and y[1]!=station and len([l for l in y[1:] if l in x])==0:
						if new not in templist:
							templist.append(new)
							print(new,self.timelimit(new))
		limit=[x for x in templist if self.timelimit(x)<=limit]
		return limit

	def random_track(self,start,connectionlist):
		tracks= self.all_shortest_routes(start)
		track_index = len(tracks)
		track_random = tracks[randint(0,track_index)]
		track= track_random

		tracklist=[]
		for i in range(len(track)):
			if i+1<len(track):
				tracklist.append([track[i],track[i+1]])
		track_w=[[[x[0],x[1]],float(x[2])] for x in connectionlist if [x[0],x[1]] in tracklist or [x[1],x[0]] in tracklist]

		nontracklist=[]
		for x in connectionlist:
			if [x[0],x[1]] not in track and [x[1],x[0]] not in tracklist:
				nontracklist.append([[x[0],x[1]],x[2]])
		time= sum([float(x[1]) for x in track_w])
		final_track=track_w,time        
		return tracklist,nontracklist,track_w,time,final_track


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

