def draw_graph(self,stationClass):
		graphdict={}
		locations= [(obj.name,obj.location) for obj in gc.get_objects() if isinstance(obj, stationClass)]
		graphdict= {x[0]:x[1] for x in locations}

		c_list= [obj.name for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='critical']
		nc_list= [obj.name for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='not critical']
		labels= {obj.name:obj.label for obj in gc.get_objects() if isinstance(obj, st.Station)}

		nx.draw(self.graph, graphdict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
		nx.draw_networkx_nodes(self.graph,graphdict,node_size=60,nodelist=c_list,node_color='lightsalmon')
		nx.draw_networkx_nodes(self.graph,graphdict,node_size=60,nodelist=nc_list,node_color='lightgrey')
		nx.draw_networkx_labels(self.graph,graphdict,labels,font_size=8,font_weight='normal')

		edge_labels = nx.get_edge_attributes(self.graph,'weight')
		nx.draw_networkx_edge_labels(self.graph, graphdict,edge_labels=edge_labels,font_size=6)
		nx.draw_networkx_edges(self.graph, graphdict, edge_labels=edge_labels, width=0.1, edge_color='k', style='solid')
		plt.show(self.graph)


	def draw_critical(self,stationClass):
		graphdict={}
		locations= [(obj.name,obj.location) for obj in gc.get_objects() if isinstance(obj, stationClass)]
		graphdict= {x[0]:x[1] for x in locations}

		c_list= [obj.name for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='critical']
		nc_list= [obj.name for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='not critical']
		labels= {obj.name:obj.label for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='critical'}

		nx.draw(self.graph, graphdict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
		nx.draw_networkx_nodes(self.graph,graphdict,node_size=40,nodelist=c_list,node_color='lightsalmon')
		nx.draw_networkx_nodes(self.graph,graphdict,node_size=20,nodelist=nc_list,node_color='lightgrey')
		nx.draw_networkx_labels(self.graph,graphdict,labels,font_size=8,font_weight='normal')

		edge_labels = nx.get_edge_attributes(self.graph,'weight')
		nx.draw_networkx_edge_labels(self.graph, graphdict,edge_labels=edge_labels,font_size=5)
		nx.draw_networkx_edges(self.graph, graphdict, edge_labels=edge_labels, width=0.1, edge_color='k', style='solid')
		plt.show(self.graph)

	def draw_path_only(self,stationClass,tracks):
		graphdict={}
		locations= [(obj.name,obj.location) for obj in gc.get_objects() if isinstance(obj, stationClass)]
		graphdict= {x[0]:x[1] for x in locations}

		c_list= [obj.name for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='critical']
		nc_list= [obj.name for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='not critical']
		
		# nx.draw(self.graph, graphdict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
		# nx.draw_networkx_nodes(self.graph,graphdict,node_size=30,nodelist=c_list,node_color='lightsalmon')
		# nx.draw_networkx_nodes(self.graph,graphdict,node_size=20,nodelist=nc_list,node_color='lightgrey')
		
		#labels= {obj.name:obj.label for obj in gc.get_objects() if isinstance(obj, st.Station) if obj.importance=='critical'}
		#nx.draw_networkx_labels(self.graph,graphdict,labels,font_size=8,font_weight='normal')

		for x in tracks:
			print(x)
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
			#dubbel dit, maar kan niet anders (niet compleet)
			nx.draw(self.graph, graphdict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
			nx.draw_networkx_nodes(self.graph,graphdict,node_size=30,nodelist=c_list,node_color='lightsalmon')
			nx.draw_networkx_nodes(self.graph,graphdict,node_size=20,nodelist=nc_list,node_color='lightgrey')
		
			nx.draw_networkx_edges(self.graph, graphdict,edgelist=edge_labels,width=0.5, edge_color='blue', style='solid',with_label=True)
			nx.draw_networkx_edge_labels(self.graph, graphdict,edge_labels=edge_labels,font_size=6)
			nx.draw_networkx_labels(self.graph,graphdict,t_labels,font_size=8,font_weight='bold')
			nx.draw_networkx_labels(self.graph,graphdict,r_labels,font_size=8,font_weight='normal')
			plt.show(self.graph)