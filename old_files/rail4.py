##################################
############# IMPORT #############
##################################

import csv                      		#used at line ..
import networkx as nx 					#used at line ..
import matplotlib.pyplot as plt 		#used at line ..
from operator import itemgetter			#used at line ..
from random import randint				#used at line ..



##################################
#### CREATING LISTS AND DICTS ####
##################################

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


##################################
####### CREATING THE GRAPH #######
##################################


X=nx.Graph()
#nx.draw_networkx_nodes(X,pos,node_size=3000,nodelist=[0,1,2,3],node_color='r')
X.add_nodes_from(stationposDict.keys())

for x in connectionlist:
    X.add_edge(x[0], x[1], weight=x[2])

for n, p in stationposDict.items():
    X.node[n]['pos'] = p

nx.draw(X, stationposDict,font_size=8,node_size=1,edge_width=0.1,width=0.1)#,with_labels=True

nx.draw_networkx_nodes(X,stationposDict,node_size=150, with_labels=True,nodelist=criticallist,node_color='lightsalmon')
nx.draw_networkx_nodes(X,stationposDict,node_size=150, with_labels=True,nodelist=ncriticallist,node_color='lightgrey')#

edge_labels = nx.get_edge_attributes(X,'weight')
nx.draw_networkx_edge_labels(X, stationposDict,edge_labels=edge_labels,font_size=7)
nx.draw_networkx_edges(X, stationposDict, edge_labels=edge_labels, width=0.1, edge_color='k', style='solid', alpha=1.0, edge_cmap=None, edge_vmin=None, edge_vmax=None, ax=None, arrows=True, label=None)

labels={}
for x in stationposDict.keys():
	if 'Amsterdam' in x:
		labels[x]=x.replace('Amsterdam',"A.")
	elif 'Rotterdam' in x:
		labels[x]=x.replace('Rotterdam',"R.")
	else:
		labels[x]=x
print(labels)
print(stationposDict.keys())

nx.draw_networkx_labels(X,stationposDict,labels,font_size=8,font_weight='normal')


#####################################
########### PLOT THE GRAPH ##########
#####################################

#plt.show(X)


#####################################
############# CLASSES ###############
#####################################

class Station():

	def __init__(self,name,importance,location,neighbours):
		self.name = name
		self.importance = importance
		self.location = location
		self.neighbours = neighbours

	def information(self):
		return '{} {} {} {}'.format(self.name, self.importance, self.location, self.neighbours)


class Connection():
	def __init__(self,stationA,sationB,time):
		self.stationA = stationA
		self.sationB = stationB
		self.time = time

	def information(self):
		return '{} {} {}'.format(self.stationA, self.stationB, self.time)

classesDict={}
for x in finalDict:
	classesDict[x]= Station(x,finalDict[x]['importance'],finalDict[x]['location'],finalDict[x]['neighbours'])

# print(classesDict['Alkmaar'].information())
# print(classesDict['Alkmaar'].location)

# import gc
# for obj in gc.get_objects():
#     if isinstance(obj, Station):
#         print(obj.name)

##################################
##### CODE FOR THE ALGORITHM #####
##################################

def ndict(all_nodes,dict,step):
    list=[]
    for x in dict[step]:
        for y in X[x]:
            if y not in all_nodes:
                list.append(y)
                all_nodes.append(y)
    dict[step+1]=list
    step += 1
    return all_nodes,dict,step

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
    
# TEST
# for x in pathcount('Amsterdam Zuid',15):
# 	print(x,pathcount('Amsterdam Zuid',15)[x])


def path(stationA,stationB):
    path= [(stationB,0)]
    totdistance= 0
    subtest= pathcount(stationA,15)
    endpoint=stationB
    for x in subtest:
        if stationB in subtest[x]:
            endlevel=x
            for i in reversed(range(endlevel)):
                for y in subtest[i]:
                    if y in X[endpoint]:
                        distance= int(X[endpoint][y]['weight'])
                        totdistance += distance
                        path.append((y,distance))
                        endpoint= y
    
    for i in reversed(range(len(path)-1)):
        print(path[i+1][0],'-',path[i][0],path[i+1][1],'minutes')
    print('')
    print('Total traveltime is',totdistance,'minutes')
    
    return path,totdistance   

# print(path('Amsterdam Centraal', 'Dordrecht'))

def firstN(station,allstations):
	allN= pathcount(station,15)
	for station in  allN[1]:
		if station not in allstations:
			return station

def paths(stationA):
    path= [stationA]
    trackline= []
    totdistance= 0
    station= stationA
    for i in range(13):
    	if firstN(station,path) != None:
    		distance= int(G[station][firstN(station,path)]['weight'])
    		totdistance += distance
    		trackline.append([station,firstN(station,path),distance])

    		station= firstN(station,path)
    		path.append(station)
    	else:
    		return stationA,trackline,station,totdistance

def paths_timelimit(stationA):
    path= [stationA]
    trackline= []
    totdistance= 0
    station= stationA
    for i in range(13):
    	if firstN(station,path) != None:
    		distance= int(X[station][firstN(station,path)]['weight'])
    		if totdistance+distance > 120:
    			return trackline,totdistance
    		totdistance += distance
    		trackline.append([[station,firstN(station,path)],distance])

    		station= firstN(station,path)
    		path.append(station)
    	else:
    		return trackline,totdistance

def firstRandom(station,allstations):
	allN= pathcount(station,15)
	n_list= [x for x in allN[1] if x not in allstations]
	if n_list==[]:
		return None
	else:
		index_len= len(n_list)-1
		random_index=randint(0,index_len)
		return n_list[random_index]

def pathsRandom(stationA):
    path= [stationA]
    trackline= []
    totdistance= 0
    station= stationA
    for i in range(20):
    	random_path= firstRandom(station,path)
    	#print(random_path)
    	if random_path != None:
    		distance= int(X[station][random_path]['weight'])
    		if totdistance + distance > 120:
    			return trackline,totdistance
    		totdistance += distance
    		trackline.append([[station,random_path],distance])
    		station= random_path
    		path.append(station)
    	else:
    		return trackline,totdistance


def tracksRandom(r):
	len_nodes= len(X.nodes())
	tracks=[]
	for x in range(r):
		random_index= randint(0,len_nodes-1)
		random_node= [x for x in X.nodes()][random_index]
		random_track= pathsRandom(random_node)
		tracks.append(random_track)
	return tracks

#print(pathsRandom('Dordrecht'))
# print(tracksRandom(7)[0])

#################################################################
########################## SCORE ################################
#################################################################



apct=[]					#all possible critical tracks
uct=[]					#unique critical tracks
for x in finalDict:
	if finalDict[x]['importance']=='critical':
		for y in finalDict[x]['neighbours']:
			n_input=[[x,y[0]],int(y[1])]
			i_input =[[y[0],x],int(y[1])]
			apct.append(i_input)
			apct.append(n_input)
			if i_input not in uct:
				uct.append(n_input)

def score(tracks):
	bvk=[]					
	min=0
	minlist=[]
	t= len(tracks)
	for i in range(t):
		min += tracks[i][1]
		minlist.append(tracks[i][1])
		track= tracks[i][0]
		clist=[x for x in track if x in apct]
		for x in clist:
			inverse_x = [[x[0][1],x[0][0]],x[1]]
			if x not in bvk:
				if inverse_x not in bvk:
					bvk.append(x)
	p= len(bvk)/len(uct)
	S= p*10000 - (t*20 + min/100000)
	return S,len(bvk),min


	# print(len(bvk),bvk)
	# print(min,minlist)


# for x in range(10):
# 	tracks= tracksRandom(7)
# 	tscore= score(tracks)
# 	print(tscore)
# 	for x in tracks:
# 		print(tracks.index(x),x)
# 	print()

def pathmaker(bfs):
    parent_children=[]
    parent_children2=[]
    lenght= len(bfs)
    for i in range(lenght-1):
        #print(i,bfs[i])
        for parent in bfs[i]:
            # print(parent)
            for child in bfs[i+1]:
                if child in X[parent]:
                    parent_children.append([parent+child])
                    #print(parent+child)
                    parent_children2.append([parent,child])
        #print('')
    return parent_children2


def all_shortest_routes(station):
    bfs=pathcount(station,20)
    list1=[x for x in pathmaker(bfs)]
    list2=[x for x in pathmaker(bfs)]
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

# for x in all_shortest_routes('Amsterdam Centraal'):
# 	print(x)

# print(len(all_shortest_routes('Amsterdam Centraal')))
# print(all_shortest_routes('Amsterdam Centraal')[20])

def random_bfs(start):
    tracks= all_shortest_routes(start)
    track_index = len(tracks)
    track_random = tracks[randint(0,track_index)]
    track= track_random

    tracklist=[]
    for i in range(len(track)):
        if i+1<len(track):
            tracklist.append([track[i],track[i+1]])
        
    nontracklist=[]
    for x in connectionlist:
        if [x[0],x[1]] not in track and [x[1],x[0]] not in tracklist:
            nontracklist.append([x[0],x[1]])
            
    return tracklist


def color_path(tracks):
    colors=['green','blue']
    graphs= ['']
    for i in range(len(tracks)):
        H=nx.Graph()
        nx.draw(H, stationposDict)
        nx.draw_networkx_nodes(H,stationposDict,node_size=150, with_labels=True,nodelist=criticallist,node_color='lightsalmon')
        nx.draw_networkx_nodes(H,stationposDict,node_size=150, with_labels=True,nodelist=ncriticallist,node_color='lightgrey')
        nx.draw_networkx_labels(H,stationposDict,labels,font_size=8,font_weight='normal')

        nx.draw_networkx_edge_labels(H, stationposDict,edge_labels=edge_labels,font_size=8)
        nx.draw_networkx_edges(H, stationposDict, edge_labels=edge_labels, edgelist=connectionlist, width=0.1, edge_color='k', style='solid')
        print(tracks[i],colors[i])
        nx.draw_networkx_edges(H, stationposDict, edge_labels=edge_labels, edgelist=tracks[i], width=1.5, edge_color=colors[i], style='solid')
        plt.show()

track1= random_bfs('Den Helder')
track2= random_bfs('Dordrecht')


print(color_path([track1,track2]))

# bfs= pathcount('A',20)
# print(bfs)

print(len(uct))
h_value=0

# y_values=[]
# x_values=[]

# for x in range(2000):
# 	tracks= tracksRandom(4)
# 	tscore= score(tracks)
# 	if tscore[0] > h_value:
# 		print(x,tscore)
# 		x_values.append(x)
# 		y_values.append(tscore[0])
# 		h_value= tscore[0]

# print(x_values)
# print(y_values)


# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

# plt.plot(x_values, y_values, '-o')
# plt.axis([0, 2000, 7500, 10000])
# plt.show()


track1=paths_timelimit('Amsterdam Zuid')
track2=paths_timelimit('Amsterdam Centraal')
track3=paths_timelimit('Amsterdam Sloterdijk')

print('Amsterdam Centraal')


# test=[track1,track2]#,track3]
# print(score(test))

# scorelist=[]
# for i in range(len(stationlist)):
# 	for x in range(len(stationlist)):
# 		if i<x:
# 			scorelist.append([stationlist[i],stationlist[x],score([paths_timelimit(stationlist[i]),paths_timelimit(stationlist[x])])])
			
# from operator import itemgetter
# for x in sorted(scorelist, key=itemgetter(2),reverse=True):
#  	print(x)


