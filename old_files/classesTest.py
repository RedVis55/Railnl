import csv

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

ncriticallist=[x for x in stationlist if x not in criticallist]

# print(connectionlist)
# print('')
# print(stationlist)

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


finalDict={}
for x in stationlist:
	testDict={}
	testDict['neighbours']=neighboursDict[x]
	testDict['location']=stationposDict[x]
	if x in criticallist:
		testDict['importance']='critical'
	if x in ncriticallist:
		testDict['importance']='not critical'
	finalDict[x]=testDict


class Station():

	def __init__(self,name,importance,location,neighbours):
		self.name = name
		self.importance = importance
		self.location = location
		self.neighbours = neighbours

	def information(self):
		return '{} {} {} {}'.format(self.name, self.importance, self.location, self.neighbours)


#########################################################################
############################## AFMAKEN DIT ##############################
#########################################################################

# for x in finalDict:
# 	name= x.replace(' ','').replace('/','')
# 	exec(name+ " = name")
# 	str_name= x
# 	importance= finalDict[x]['importance']
# 	location= finalDict[x]['location']
# 	neighbours= finalDict[x]['neighbours']
# 	# name = Station(str_name,importance,location,neighbours)

alkmaar= Station('Alkmaar','critical',(4.739722252, 52.63777924),[['Hoorn', '24'], ['Den Helder', '36'], ['Castricum', '9']])
print(alkmaar.information())



class connection():
	def __init__(self,stationA,sationB,time):
		self.stationA = stationA
		self.sationB = stationB
		self.time = time

	def information(self):
		return '{} {} {}'.format(self.stationA, self.stationB, self.time)


# print('oke'+str(1))

name='geklolhenk'
print(name,type(name))
exec(name+ " = name")
#print(geklolhenk)

# for x in finalDict:
# 	name= x.replace(' ','').replace('/','')#.lower()
# 	exec(name+ " = name")
# 	print(name,type(name))

name='Den Helder/'
str_name='Den Helder'
new_name= name.replace(' ','').replace('/','')#.lower()
exec(new_name+ " = new_name")

new_name= Station(str_name,'not critical',(4.739722252, 52.63777924),[['Den Helder', '36']])

#print(new_name.information())

apct=[]					#all possible critical tracks
for x in finalDict:
	if finalDict[x]['importance']=='critical':
		for y in finalDict[x]['neighbours']:
			apct.append([[x,y[0]],y[1]])

uct=[]
for x in finalDict:
	if finalDict[x]['importance']=='critical':
		for y in finalDict[x]['neighbours']:
			print(x,y[0])
