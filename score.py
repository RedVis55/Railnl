


def unique(dict):
	apct=[]					#all possible critical tracks
	uct=[]					#unique critical tracks
	for x in dict:
		if dict[x]['importance']=='critical':
			for y in dict[x]['neighbours']:
				n_input=[[x,y[0]],float(y[1])]
				i_input =[[y[0],x],float(y[1])]
				apct.append(i_input)
				apct.append(n_input)
				if i_input not in uct:
					uct.append(n_input)
	return apct,uct

def score(tracks,apct,uct):
	bkv=[]					#bereden kritieke verbindingen				
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
			if x not in bkv:
				if inverse_x not in bkv:
					bkv.append(x)
	p= len(bkv)/len(uct)
	S= p*10000 - (t*20 + min/100000)
	# print(bkv)
	return S,len(bkv),min