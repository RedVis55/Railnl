from lists_dicts 		import *
from graph 				import *
from random_shortest	import *
from score				import *
from random_neighbour	import *


# IMPORTS USED IN ALL FILES

# import csv                      			#used in lists_dicts.py
# import networkx as nx 					#used in lists_dicts,graph,random_shortest
# import matplotlib.pyplot as plt 			#used in graph
# from operator import itemgetter			#used at line ..
# from random import randint				#used in random_shortest

#######################################
############ ASSIGN VALUES ############
#######################################

#open_c			= open_connections('ConnectiesHolland.csv')
open_c			= open_connections('ConnectiesNationaal.csv')
stationlist		= open_c[0]
connectionlist	= open_c[1]

#open_s 			= open_stations('StationsHolland.csv')
open_s 			= open_stations('StationsNationaal.csv')
stationposDict	= open_s[0]
criticallist	= open_s[1]
ncriticallist	= open_s[2]
stationDict 	= dict_maker(stationlist,connectionlist,stationposDict,criticallist,ncriticallist)

uniqued			= unique(stationDict)
apct			= uniqued[0]
uct				= uniqued[1]

change_names	= ['Amsterdam','Rotterdam','Den Haag']
labels 			= label_maker(stationposDict,change_names)
G				= standard_graph(stationposDict,connectionlist,criticallist,ncriticallist,labels)


track1= random_track(G,'Den Helder',connectionlist)[4]
track2= random_track(G,'Maastricht',connectionlist)[4]
track3= random_track(G,'Leeuwarden',connectionlist)[4]
track4= random_track(G,'Vlissingen',connectionlist)[4]


# print(track3)
# print()
# print(track1,track2)


#color_path(G,[track1,track2],['blue','red'],stationposDict,connectionlist,criticallist,ncriticallist,labels)
#color_path_framed(G,[track1,track2,track3,track4],['blue','black','black','black'],stationposDict,connectionlist,criticallist,ncriticallist,labels)

#print(stationposDict)

for x in nx.get_edge_attributes(G,'weight'):
	print(x)
no_names(G,[track3],stationposDict,connectionlist,criticallist,ncriticallist,labels)
#draw_standard_graph(G,stationposDict,connectionlist,criticallist,ncriticallist,labels)


# print(pathsRandom(G,'Utrecht Centraal'))
# print(pathsRandom(G,'Utrecht Centraal'))
# print(pathsRandom(G,'Utrecht Centraal'))
# print(pathsRandom(G,'Utrecht Centraal'))


#print(score([track1,track2,track3,track4],apct,uct))

# print(random_track(G,'Den Helder',connectionlist)[4])
# print(random_track(G,'Den Helder',connectionlist)[2])

# print(all_shortest_routes(G,'Den Helder'))

# print(tracksRandom(G,2))





# scores=[]
# for x in range(500):
# 	tracks= tracksRandom(G,15)
# 	tscore= score(tracks,apct,uct)
# 	scores.append(round(tscore[0]))

# scores2=[]
# for x in range(500):
# 	tracks= tracksRandom(G,7)
# 	tscore= score(tracks,apct,uct)
# 	scores2.append(round(tscore[0]))

# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt

# plt.hist(scores, bins=[x*100 for x in range(100)], range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, hold=None, data=None)
# plt.hist(scores2, bins=[x*100 for x in range(100)], range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color='red', label=None, stacked=False, normed=None, hold=None, data=None)

# plt.show()
