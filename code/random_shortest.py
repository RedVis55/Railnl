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


def pathmaker(graph,bfs):
    parent_children=[]
    parent_children2=[]
    lenght= len(bfs)
    for i in range(lenght-1):
        for parent in bfs[i]:
            # print(parent)
            for child in bfs[i+1]:
                if child in graph[parent]:
                    parent_children.append([parent+child])
                    parent_children2.append([parent,child])
    return parent_children2

def all_shortest_routes(graph,station):
    bfs=pathcount(graph,station,20)
    list1=[x for x in pathmaker(graph,bfs)]
    list2=[x for x in pathmaker(graph,bfs)]
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

def random_track(graph,start,connectionlist):
    tracks= all_shortest_routes(graph,start)
    track_index = len(tracks)
    track_random = tracks[randint(0,track_index)]
    track= track_random

    tracklist=[]
    for i in range(len(track)):
        if i+1<len(track):
            tracklist.append([track[i],track[i+1]])
    track_w=[[[x[0],x[1]],float(x[2])] for x in connectionlist if [x[0],x[1]] in tracklist or [x[1],x[0]] in tracklist]

    nontracklist=[]
    for x in connectionlist:
        if [x[0],x[1]] not in track and [x[1],x[0]] not in tracklist:
            nontracklist.append([[x[0],x[1]],x[2]])
    time= sum([float(x[1]) for x in track_w])
    final_track=track_w,time        
    return tracklist,nontracklist,track_w,time,final_track