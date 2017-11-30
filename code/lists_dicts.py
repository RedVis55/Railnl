######################################
############### IMPORT ###############
######################################

import csv                      		#used at line 20
import networkx as nx 					#used at line 88

#######################################
#### FUNCTIONS FOR LISTS AND DICTS ####
#######################################

def open_connections(file):
	stationlist=[]
	connectionlist=[]
	with open('csv-files/'+file) as csvfile:
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
	with open('csv-files/'+file) as csvfile:
		rows = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in rows:
			stationposDict[row[0]]=(float(row[2]),float(row[1]))   #longitude is de x-as en latitude is de y-as
			if len(row)>3:
				if row[3]=='Kritiek':
					criticallist.append(row[0])
			else:
				ncriticallist.append(row[0])
	return stationposDict,criticallist,ncriticallist

def dict_maker(stationlist,connectionlist,stationposDict,criticallist,ncriticallist):
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