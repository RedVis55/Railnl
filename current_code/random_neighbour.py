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
    track_single=[stationA]
    totdistance= 0
    station= stationA
    for i in range(20):
        random_path= firstRandom(graph,station,path)
        if random_path != None:
            distance= float(graph[station][random_path]['weight'])
            if totdistance + distance > 120:
                return track_single#trackline,totdistance
            totdistance += distance
            trackline.append([[station,random_path],distance])
            track_single.append(random_path)
            station= random_path
            path.append(station)
        else:
            return track_single#,totdistance


def tracksRandom(graph,r):
    len_nodes= len(graph.nodes())
    tracks=[]
    for i in range(r):
        random_index= randint(0,len_nodes-1)
        random_node= [x for x in graph.nodes()][random_index]
        random_track= pathsRandom(graph,random_node)
        tracks.append(random_track)
    return tracks


