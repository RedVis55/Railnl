import create_tracks as ct

from random import randint


def score():
	pass


def hillclimber(graph,track,other_tracks,limit,apct,utc): 
	highest_score=0
	adjustment_list=[]
	start= track[0]
	all_tracks= ct.combine_all_timelimit(graph,start,limit)
	random_index= randint(1,len(track)-1)
	print(track)
	print(track[:random_index])
	for x in all_tracks:
		if track[:random_index]==x[:random_index]:
			adjustment_list.append(x)
	iterations=len(adjustment_list)*2
	print(i)
	for i in range(iterations):
		random_index=randint(0,len(adjustment_list)-1)
		test_track= adjustment_list[random_index]
		total_tracks= [other_tracks + test_track]
		new_score= score(total_tracks,apct,utc)
		if new_score>highest_score:
			print(i,new_score)


		#print(adjustment_list[x])
