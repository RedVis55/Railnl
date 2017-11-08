import csv

class Station:

	stationlist=[]
	connectionlist=[]
	stationposDict={}
	criticallist=[]

	with open('ConnectiesHolland.csv') as csvfile:
		rows = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in rows:
			if row[0] not in stationlist:
				stationlist.append(row[0])
			if row[1] not in stationlist:
				stationlist.append(row[1])
			connectionlist.append(row)

	with open('StationsHolland.csv') as csvfile:
		rows = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in rows:
			stationposDict[row[0]]=(float(row[2]),float(row[1]))
			#longitude is de x-as en latitude is de y-as
		if row[3]=='Kritiek':
			criticallist.append(row[0])

	def __init__(self,):
		pass

	def pathcount(node,nrange):
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
				ndict(all_nodes,dict,step)


	def neighbours(station,stationlist):
		allN= pathcount(station,15)
		for station in  allN[1]:
			print (station)


print(Station.neighbours('Haarlem',['Heemstede-Aerdenhout']))