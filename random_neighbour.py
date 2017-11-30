######################################
############### IMPORT ###############
######################################


import networkx as nx                   #used at line 88
from random import randint              #used at line ..


def ndict(graph,all_nodes,dict,step):
    list=[]
    for x in dict[step]:
        for y in graph[x]:
            if y not in all_nodes:
                list.append(y)
                all_nodes.append(y)
    dict[step+1]=list
    step += 1
    return all_nodes,dict,step

def pathcount(graph,node,nrange):
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
            ndict(graph,all_nodes,dict,step)

def firstRandom(graph,station,allstations):
    allN= pathcount(graph,station,15)
    n_list= [x for x in allN[1] if x not in allstations]
    if n_list==[]:
        return None
    else:
        index_len= len(n_list)-1
        random_index=randint(0,index_len)
        return n_list[random_index]

def pathsRandom(graph,stationA):
    path= [stationA]
    trackline= []
    totdistance= 0
    station= stationA
    for i in range(20):
        random_path= firstRandom(graph,station,path)
        if random_path != None:
            distance= float(graph[station][random_path]['weight'])
            if totdistance + distance > 120:
                return trackline,totdistance
            totdistance += distance
            trackline.append([[station,random_path],distance])
            station= random_path
            path.append(station)
        else:
            return trackline,totdistance


def tracksRandom(graph,r):
    len_nodes= len(graph.nodes())
    tracks=[]
    for x in range(r):
        random_index= randint(0,len_nodes-1)
        random_node= [x for x in graph.nodes()][random_index]
        random_track= pathsRandom(graph,random_node)
        tracks.append(random_track)
    return tracks


def random_shortest(start):
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