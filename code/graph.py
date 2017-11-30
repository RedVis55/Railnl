######################################
############### IMPORT ###############
######################################
##test

import networkx as nx 					#used at line 88
import matplotlib.pyplot as plt 		#used at line ..
from operator import itemgetter			#used at line ..

#######################################
######### CREATING THE GRAPH ##########
#######################################

def label_maker(stationposDict,names):
	#names is a list ['Amsterdam','Utrecht',enz.]
	full_names=[x for x in stationposDict]
	labels={x:x for x in stationposDict}
	for name in names:
		firstL=name[0]
		replaced=firstL+'.'
		for x in full_names:
			if name in x:
				new_name= replaced+x.replace(name,'')
				labels[x]=new_name
	return labels

def standard_graph(stationposDict,connectionlist,criticallist,ncriticallist,labels):
	G=nx.Graph()
	G.add_nodes_from(stationposDict.keys())
	for x in connectionlist:
		G.add_edge(x[0],x[1], weight=x[2])
	for n,p in stationposDict.items():
		G.node[n]['pos']=p
	return G

def draw_standard_graph(G,stationposDict,connectionlist,criticallist,ncriticallist,labels):
	nx.draw(G, stationposDict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
	nx.draw_networkx_nodes(G,stationposDict,node_size=60, with_labels=True,nodelist=criticallist,node_color='lightsalmon')
	nx.draw_networkx_nodes(G,stationposDict,node_size=60, with_labels=True,nodelist=ncriticallist,node_color='lightgrey')
	nx.draw_networkx_labels(G,stationposDict,labels,font_size=8,font_weight='normal')

	edge_labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx_edge_labels(G, stationposDict,edge_labels=edge_labels,font_size=6)
	nx.draw_networkx_edges(G, stationposDict, edge_labels=edge_labels, width=0.1, edge_color='k', style='solid')
	plt.show(G)


def color_path(G,tracks,colors,stationposDict,connectionlist,criticallist,ncriticallist,labels):
    for i in range(len(tracks)):
        H=nx.Graph()
        nx.draw(H, stationposDict)
        nx.draw_networkx_nodes(H,stationposDict,node_size=60, with_labels=True,nodelist=criticallist,node_color='lightsalmon')
        nx.draw_networkx_nodes(H,stationposDict,node_size=60, with_labels=True,nodelist=ncriticallist,node_color='lightgrey')
        nx.draw_networkx_labels(H,stationposDict,labels,font_size=8,font_weight='normal')

        edge_labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(H, stationposDict,edge_labels=edge_labels,font_size=8)
        nx.draw_networkx_edges(H, stationposDict, edge_labels=edge_labels, edgelist=connectionlist, width=0.1, edge_color='k', style='solid')
        print(tracks[i],colors[i])
        nx.draw_networkx_edges(H, stationposDict, edge_labels=edge_labels, edgelist=tracks[i], width=1.5, edge_color=colors[i], style='solid')
        #plt.show()


def color_path_framed(G,tracks,colors,stationposDict,connectionlist,criticallist,ncriticallist,labels):
	for i in range(len(tracks)):
		stations=[x[0][0] for x in tracks[i][0]]
	
		last=tracks[i][0][len(tracks[i][0])-1][0][1]
		stations.append(last)
		tempDict={x:stationposDict[x] for x in stations}
		snames={x:x for x in stations}
		temp_c=[x for x in stations if x in criticallist]
		temp_nc=[x for x in stations if x in ncriticallist]
		L=0
		L=nx.Graph()
		nx.draw(L, tempDict)
		nx.draw_networkx_nodes(L,tempDict,node_size=60, with_labels=True,nodelist=temp_c,node_color='lightsalmon')
		nx.draw_networkx_nodes(L,tempDict,node_size=60, with_labels=True,nodelist=temp_nc,node_color='lightgrey')
		nx.draw_networkx_labels(L,tempDict,snames,font_size=8,font_weight='normal')
		print([x[0] for x in tracks[i][0]])
        #edge_labels = nx.get_edge_attributes(G,'weight')
        #print(edge_labels)
        #nx.draw_networkx_edge_labels(H, tempDict,edge_labels=edge_labels,font_size=8)
        #nx.draw_networkx_edges(H, tempDict, edge_labels=edge_labels, edgelist=connectionlist, width=0.1, edge_color='k', style='solid')
		nx.draw_networkx_edges(L, tempDict, edgelist=[x[0] for x in tracks[i][0]], width=0.1, edge_color=colors[i], style='solid')
		# edge_labels=edge_labels
		plt.show()




def no_names(G,tracks,stationposDict,connectionlist,criticallist,ncriticallist,labels):
	nx.draw(G, stationposDict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
	nx.draw_networkx_nodes(G,stationposDict,node_size=20, with_labels=True,nodelist=criticallist,node_color='lightsalmon')
	nx.draw_networkx_nodes(G,stationposDict,node_size=20, with_labels=True,nodelist=ncriticallist,node_color='lightgrey')
	#nx.draw_networkx_labels(G,stationposDict,labels,font_size=8,font_weight='normal')
	for x in tracks:
		track= x[0]
		time= x[1]
		stations=[]
		# e_list=[]
		e_labels={}
		for y in track:
			f=y[0][0]
			l=y[0][1]
			if f not in stations:
				stations.append(f)
			if l not in stations:
				stations.append(l)
			# e_list.append([ y[0][0],y[0][1],y[1] ])
			e_labels[(f,l)]=y[1]
		tempDict={x:stationposDict[x] for x in stations}
		new_labels={x:labels[x] for x in stations}
		nx.draw_networkx_edges(G, stationposDict, edge_labels=e_labels, edgelist=e_labels, width=1, edge_color='blue', style='solid')
		nx.draw_networkx_edge_labels(G, stationposDict,edge_labels=e_labels,font_size=6)
		nx.draw_networkx_labels(G,stationposDict,new_labels,font_size=8,font_weight='normal')
	plt.show(G)



		# pos_higher = {}
		# y_off = 0.01  # offset on the y axis
		# x_off = 0.1   # offset on the x axis

		# for k, v in stationposDict.items():
		#     pos_higher[k] = (v[0]+x_off, v[1]+y_off)

		# #nx.draw_networkx_labels(G, pos_higher, new_labels,font_size=7,font_weight='normal',ha='right')
