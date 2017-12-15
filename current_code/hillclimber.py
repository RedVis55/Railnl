import create_tracks as ct

from random import randint


def score():
	pass


def hillclimber(graph,track,limit): #other_tracks
	S=0
	adjustment_list=[]
	start= track[0]
	all_tracks= ct.combine_all_timelimit(graph,start,limit)
	random_index= randint(1,len(track)-1)
	print(track)
	print(track[:random_index])
	for x in all_tracks:
		if track[:random_index]==x[:random_index]:
			adjustment_list.append(x)

	i=len(adjustment_list)*2
	print(i)
	for x in range(i):
		random_index=randint(0,len(adjustment_list)-1)
		test_track= adjustment_list[random_index]
		#total_tracks= [other_tracks + test_track]
		#S= score(total_tracks,.....)
		#if score>S:



		#print(adjustment_list[x])
