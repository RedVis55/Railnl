######################################
############### IMPORT ###############
######################################

import csv                      		#used at line 20
import networkx as nx 					#used at line 88
import matplotlib.pyplot as plt 		#used at line ..
from operator import itemgetter			#used at line ..
from random import randint				#used at line ..



#######################################
#### FUNCTIONS FOR LISTS AND DICTS ####
#######################################

def open_connections(file):
	stationlist=[]
	connectionlist=[]
	with open(file) as csvfile:
		rows = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in rows:
			if row[0] not in stationlist:
				stationlist.append(row[0])
			if row[1] not in stationlist:
				stationlist.append(row[1])
			connectionlist.append(row)
	return stationlist,connectionlist

def open_stations(file):
	stationposDict={}
	criticallist=[]
	ncriticallist=[]
	with open(file) as csvfile:
		rows = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in rows:
			stationposDict[row[0]]=(float(row[2]),float(row[1]))   #longitude is de x-as en latitude is de y-as
			if row[3]=='Kritiek':
				criticallist.append(row[0])
			else:
				ncriticallist.append(row[0])
	return stationposDict,criticallist,ncriticallist

def dict_maker(stationlist,connectionlist,stationposDict):
	neighboursDict={}
	for x in stationlist:
		station_neighbours=[]
		station = x
		for y in connectionlist:
			if station==y[0]:
				station_neighbours.append([y[1],y[2]])
			elif station==y[1]:
				station_neighbours.append([y[0],y[2]])
		neighboursDict[station]=station_neighbours

	stationDict={}
	for x in stationlist:
		tempDict={}
		tempDict['neighbours']=neighboursDict[x]
		tempDict['location']=stationposDict[x]
		if x in criticallist:
			tempDict['importance']='critical'
		if x in ncriticallist:
			tempDict['importance']='not critical'
		stationDict[x]=tempDict	

	return stationDict 


#######################################
############ ASSIGN VALUES ############
#######################################

open_c			= open_connections('ConnectiesHolland.csv')
stationlist		= open_c[0]
connectionlist	= open_c[1]
open_s 			= open_stations('StationsHolland.csv')
stationposDict	= open_s[0]
criticallist	= open_s[1]
ncriticallist	= open_s[2]
stationDict 	= dict_maker(stationlist,connectionlist,stationposDict)


#######################################
######### CREATING THE GRAPH ##########
#######################################

def label_maker(stationposDict,[names]):
	labels={}
	for x in stationposDict.keys():
		if 'Amsterdam' in x:
			labels[x]=x.replace('Amsterdam',"A.")
		elif 'Rotterdam' in x:
			labels[x]=x.replace('Rotterdam',"R.")
		else:
			labels[x]=x

def standard_graph(stationposDict,connectionlist,labels):
	G=nx.Graph
	G.add_nodes_from(stationposDict.keys())
	for x in connectionlist:
		G.add_edge(x[0],x[1], weight=x[2])
	for n,p in stationposDict.items():
		G.node[n]['pos']=p
	nx.draw(G, stationposDict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
