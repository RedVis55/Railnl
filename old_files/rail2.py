##################################
############# IMPORT #############
##################################

import csv
import networkx as nx
import matplotlib.pyplot as plt


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


##################################
####### CREATING THE GRAPH #######
##################################

G= nx.Graph()
for x in stationlist:
    G.add_node(x)
    
for x in connectionlist:
    G.add_edge(x[0], x[1], weight=x[2])


fig_size = plt.rcParams["figure.figsize"]
# Prints: [8.0, 6.0]
# print "Old size:", fig_size
 
# Set figure width to 18 and height to 15
fig_size[0] = 18
fig_size[1] = 15
# print "New size:", fig_size

# spring_layout(G, dim=2, k=None, pos=None, fixed=None, iterations=50, weight='weight', scale=1.0)
pos= nx.spring_layout(G,pos=stationposDict)
nx.draw(G,pos,with_labels=True,font_size=15)  #font_size=10

#draw difference between critical and non critical
nx.draw_networkx_nodes(G,pos,with_labels=True,nodelist=criticallist,node_color='red')
nx.draw_networkx_nodes(G,pos,with_labels=True,nodelist=ncriticallist,node_color='lightgrey')

#draw edge labels with the traveltime
edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels=edge_labels)

# SHOW THE PLOT
plt.show()

##################################
##### CODE FOR THE ALGORITHM #####
##################################

def ndict(all_nodes,dict,step):
    list=[]
    for x in dict[step]:
        for y in G[x]:
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
pathcount('Den Helder',15)

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
                    if y in G[endpoint]:
                        distance= int(G[endpoint][y]['weight'])
                        totdistance += distance
                        path.append((y,distance))
                        endpoint= y
    
    for i in reversed(range(len(path)-1)):
        print (path[i+1][0],'-',path[i][0],path[i+1][1],'minutes')
    print ('')
    print ('Total traveltime is',totdistance,'minutes')
    
    return path,totdistance   


def firstN(station,allstations):
	allN= pathcount(station,15)
	#for x in allN:
	#	print x,allN[x]
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
    		if totdistance+distance > 120:
    			print ('TE VEEL')
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
    		distance= int(G[station][firstN(station,path)]['weight'])
    		if totdistance+distance > 120:
    			return stationA,trackline,station,totdistance
    		totdistance += distance
    		trackline.append([station,firstN(station,path),distance])

    		station= firstN(station,path)
    		path.append(station)
    	else:
    		return stationA,trackline,station,totdistance

test=paths_timelimit('Amsterdam Zuid')
list= [x[0] for x in test[1]]
print (list)
print ('')

for x in  test[1]:
	print (x)

print ('Beginstation is',test[0])
print ('Eindstation is',test[2])
print ('Totale reistijd bevat',test[3],'minuten')


# TEST
# DELETE THE PRINT STATEMENTS IN THE FUNCTION "PATH"

#print 'Traject Den Helder - Amsterdam Zuid (shortest route (amount of stations))'
#print ''
#path('Den Helder','Amsterdam Zuid') 


########################################
######### TESTING FUNCTIONS ############
########################################


def pathTest(stationA,stationB):
    path= [(stationB,0)]
    totdistance= 0
    subtest= pathcount(stationA,15)
    endpoint=stationB
    for x in subtest:
        print (x,subtest[x])
        if stationB in subtest[x]:
            print ('')
            endlevel=x
            for i in reversed(range(endlevel)):
                for y in subtest[i]:
                    if y in G[endpoint]:
                        distance= int(G[endpoint][y]['weight'])
                        totdistance += distance
                        path.append((y,distance))
                        print (i,y,distance,[x for x in G[y]])
                endpoint= y
                print ('')
    
    #return path,totdistance   

#path('Den Helder','Leiden Centraal') 

def firstN(station,allstations):
	allN= pathcount(station,15)
	#for x in allN:
	#	print x,allN[x]
	for station in  allN[1]:
		if station not in allstations:
			return station

print ('begin')
print (firstN('Haarlem',['Heemstede-Aerdenhout']))
# print (G[stationA][stationB]['weight'])

def testN(station,stationlist):
	allN= pathcount(station,15)
	for station in  allN[1]:
		print (station)
		#if station not in allstations:
		#	return station


#print testN('Haarlem',['Heemstede-Aerdenhout'])

def paths(stationA):
    path= [stationA]
    trackline=[]
    totdistance= 0
    station= stationA
    print ('Begin station is ',station)
    print ('')
    for i in range(13):
    	if firstN(station,path) != None:
    		print (station,'-',firstN(station,path), G[station][firstN(station,path)]['weight'])
    		distance= int(G[station][firstN(station,path)]['weight'])
    		totdistance += distance
    		trackline.append(station,firstN(station,path),distance)
    		station= firstN(station,path)
    		path.append(station)
    	else:
    		print ('')
    		return stationA,'-',station,'Totale reistijd is',trackline,totdistance




    #subtest= pathcount(stationA,15)
    #for x in subtest:
    #	station= subtest[x]
    #    print 'level',x,station
    #    i=0
    #    if subtest[x] not in path:
    #    	path.append(station)
    #    	print station
        #for y in range(len(subtest[x])):
        #    if subtest[x][i] not in path:
        #        print i,subtest[x][i]
        #        path.append(subtest[x][i])
        #    else:
        #        i+= 1
                
                
                
                
                
                
                #subtest= pathcount(subtest[x][i],15)
                #print subtest
            #else: 
            #    print 'geen nieuwe b'
    #    if stationB in subtest[x]:
    #        print ''
    #        endlevel=x
    #        for i in reversed(range(endlevel)):
    #            for y in subtest[i]:
    #                if y in G[endpoint]:
    #                    distance= int(G[endpoint][y]['weight'])
    #                    totdistance += distance
    #                    path.append((y,distance))
    #                    print i,y,distance,[x for x in G[y]]
    #            endpoint= y
    #            print ''
    
    #return path,totdistance   

 
