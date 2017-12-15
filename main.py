import os, sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\RailNL\\code\\tracks")
sys.path.append(parent_dir_name+"\\RailNL\\code")

#sys.path.append(parent_dir_name+"\\RailNL\\code")
print(parent_dir_name+"\\RailNL\\code" )

import lists_dicts as ld
import graph as gr
import tracks as tr

import station_class as st
import tracks_class as tr_c
#import connection as cn
import create_tracks as ct
import hillclimber as hc
import random_neighbour as rn
import transform_track as tt
import score as sc


from random import randint


if __name__ == "__main__":

	# ADDING ALL THE INSTANCES
	stationDict= ld.import_data('Nationaal','data')[0]
	stations={}
	for x in stationDict:
		stations[x] = st.Station(x,x,stationDict[x]['importance'],stationDict[x]['location'],stationDict[x]['neighbours'])


	# UPDATE CERTAIN LABELS
	for x in stations:
		if 'Amsterdam' in stations[x].label:
			stations[x].update_single('Amsterdam','A.')
		if 'Rotterdam' in stations[x].label:
			stations[x].update_single('Rotterdam','R.')
		if 'Den Haag' in stations[x].label:
			stations[x].update_single('Den Haag','DH.')

	# station['full name'].reset_label()
	

	testtrack=[[['Assen', 'Zwolle'], 40.0], [['Groningen', 'Assen'], 17.0], [['Utrecht Centraal', 'Amersfoort'], 14.0], [['Utrecht Centraal', 'Schiphol Airport'], 33.0], [['Zwolle', 'Amersfoort'], 35.0]]
	testtime=139.0
	testtotal= [[testtrack,testtime],[testtrack,testtime]]

	testt1=['Utrecht Centraal', 'Amsterdam Amstel', 'Almere Centrum', 'Lelystad Centrum']
	testt2=['Amsterdam Centraal','Utrecht Centraal', 's-Hertogenbosch', 'Tilburg', 'Breda']

	# TEST
	L= gr.Graph(st.Station)


	print('Print t1')
	t1= tr_c.Tracks([testt1,testt2])
	t1.transform_tracks(stations,L.graph)
	for x in t1.transform:
		print(x)


	
	# print(t1.min_list)
	# print(t1.transform[0])
	# print(testtotal[0])

	# t1.compute_score(apct,uct)#apct,uct)
	# print(print(L.information()))

	L.draw_choice(st.Station,'standard')
	L.draw_choice(st.Station,'critical')
	L.draw_choice(st.Station,['track',testtotal])
	L.draw_choice(st.Station,['track',t1.transform])


	# dtest= L.pathcount('Maastricht',20)
	# for x in dtest:
	# 	print(x,dtest[x])

	# d2test= L.all_shortest_routes('Utrecht Centraal')
	# for x in d2test:
	# 	print(x)
	print(print(L.information()))

	d3test= ct.combine_all_timelimit(L.graph,'Groningen',120)
	
	L.draw_choice(st.Station,['track',tt.transform(L.graph,d3test)[0][10:15]])

	apct= sc.unique(stationDict)[0]
	uct= sc.unique(stationDict)[1]

	score= sc.score(tt.transform(L.graph,d3test)[0][10:15],apct,uct)
	print(score)

	totaltracks= ct.tracksRandom(L.graph,10)
	#print(tt.transform(L.graph,totaltracks)[0])
	#L.draw_choice(st.Station,['track',tt.transform(L.graph,totaltracks))



	
	# random_index= randint(0,len(d3test))
	# random_tlen= randint(0,len(d3test[random_index]))
	# random_tswitch= d3test[random_index][random_tlen]

	# print(len(d3test))
	# print(random_index,d3test[random_index])
	# # print(random_tlen,random_tswitch)
	# print('XX')
	# tracksli= rn.tracksRandom(L.graph,5)
	# for x in tt.transform(L.graph,tracksli)[0]:
	# 	print(x)

	# apct= tt.unique(stationDict)
	# uct= tt.unique(stationDict)

	# print(tt.score(L.graph,tracksli,apct,uct))
	# print('XX')
	# # for x in ct.combine_all_timelimit(L.graph,'Maastricht',180):
	# # 	print(x)
	# #print(len(ct.combine_all_timelimit(L.graph,'Maastricht',180)))
	# maastricht= ct.combine_all_timelimit(L.graph,'Groningen',180)[300]
	# print()
	# hc.hillclimber(L.graph,maastricht,180)
	# # for x in d3test:
	# # 	if d3test[random_index][:random_tlen+1]==x[:random_tlen+1]:
	# # 		print(x)

	# #print(d3test[1781])
	# print(L.information())
	#begin=['Utrecht Centraal', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Schiedam Centrum']

	# for x in d3test:
	# 	print(x)

	#print(gr.timelimit(L.graph,['Maastricht', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch'])



	






















	# double_connections= [(obj.name,n[0],n[1]) for n in obj.neighbours for obj in gc.get_objects() if isinstance(obj, st.Station)]
	# double_connections= [(obj.name,n[0],n[1]) for obj in gc.get_objects() if isinstance(obj, st.Station) for n in obj.neighbours]
	# for a,b,w in double_connections:
	# 	print(a,b,w)

