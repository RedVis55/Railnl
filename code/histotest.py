import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# from main import *

# plt.hist([1,1,1,4,4,3,7,9,9,9,9,20,20,20,60], bins=[x for x in range(100)], range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, hold=None, data=None)
plt.hist([4267, 2063, 4436, 4267, 4775, 4097, 3758, 4267, 2911, 3758, 3758, 2402, 3080, 4097, 4606, 3758, 4436, 4097, 3419, 3758, 2911, 1894, 5453, 4436, 4606, 3758, 4775, 4097, 3758, 3080, 4097, 4267, 4606, 4606, 4097, 3928, 4436, 4097, 2741, 3080, 3758, 2911, 3250, 3080, 3758, 4267, 3928, 3419, 4097, 3758, 4606, 4775, 3589, 3928, 3928, 3419, 4945, 3250, 3589, 4606, 3758, 4436, 4097, 3928, 4267, 3589, 3589, 3589, 3928, 3250, 2911, 4097, 4606, 3419, 4436, 3080, 4267, 3928, 3419, 4267, 3928, 4606, 3589, 3589, 3589, 3250, 4436, 3928, 4775, 3928, 4097, 2741, 4436, 3419, 4267, 3419, 4267, 3419, 3758, 3589, 2572, 3589, 4097, 3080, 4097, 3080, 3419, 3928, 3080, 4436, 3250, 4267, 3589, 3928, 3419, 3419, 4775, 4097, 4606, 2911, 3250, 3589, 3419, 3589, 4267, 2741, 3080, 3080, 3928, 3758, 3419, 4267, 3928, 3250, 2572, 4945, 4436, 3589, 3419, 3758, 4097, 2741, 4097, 3080, 4436, 3419, 4606, 3589, 2063, 3080, 2911, 4097, 3589, 3080, 3758, 3419, 4267, 3250, 4097, 3758, 3928, 2911, 4267, 2741, 3928, 3589, 4097, 3928, 3419, 4097, 3758, 3758, 4606, 4097, 3758, 3758, 4436, 3758, 2741, 4267, 3589, 4775, 4267, 4436, 4097, 3758, 4097, 3589, 3419, 3758, 4775, 4775, 3589, 4097, 3250, 4267, 4097, 1894, 3250, 4097, 4097, 4267, 3419, 3928, 3758, 3080, 3758, 3250, 4606, 4436, 3928, 2741, 3589, 4606, 4436, 3589, 2233, 3250, 4267, 2911, 2402, 3080, 3928, 2911, 3419, 3928, 3758, 4267, 4436, 3250, 3419, 4267, 3419, 3419, 4267, 2741, 3928, 3758, 2911, 3758, 3758, 2063, 4436, 3758, 3250, 4097, 2572, 4436, 3758, 3928, 4436, 2741, 4267, 3080, 4097, 3589, 4267, 4436, 3928, 3080, 3419, 3419, 3758, 2911, 3080, 3758, 2572, 3928, 2572, 3419, 3419, 3758, 4606, 4097, 4097, 3080, 3080, 3758, 3080, 3758, 3419, 3250, 2911, 3758, 2402, 4097, 3928, 4267, 3758, 3589, 2911, 2911, 3419, 3080, 3419, 3928, 2911, 3250, 3250, 4097, 3758, 4945, 3928, 3928, 4436, 3419, 3080, 2911, 3758, 4097, 3419, 3758, 3589, 4097, 3080, 3928, 3758, 2572, 3589, 4267, 3758, 4097, 3419, 3250, 3419, 3758, 3589, 3928, 3419, 3758, 2911, 4267, 2911, 3419, 4436, 3928, 3928, 2911, 2402, 3758, 4097, 4097, 3758, 2402, 3589, 3419, 3928, 3419, 3758, 4097, 3080, 2741, 3419, 4436, 2572, 4097, 3589, 1894, 3928, 4097, 2572, 3080, 3250, 3758, 4097, 3928, 3758, 3758, 3758, 3250, 2402, 4775, 2741, 4267, 3758, 4436, 3250, 3758, 3250, 4775, 4775, 3589, 3589, 4775, 2911, 2402, 4945, 4097, 3758, 3080, 3928, 3250, 3250, 3758, 3589, 3250, 3080, 3080, 4267, 3250, 4436, 4097, 3758, 3080, 3758, 3419, 4775, 4267, 2063, 4267, 4436, 3419, 2741, 3589, 4097, 2402, 2911, 3758, 3928, 4097, 3589, 3928, 2911, 2911, 4267, 3928, 3928, 2911, 4097, 3928, 2911, 3589, 3928, 3250, 3080, 4436, 3928, 2911, 2741, 4436, 4606, 1894, 3589, 4097, 3589, 2911, 4097, 3758, 3589, 2911, 2572, 4097, 4097, 4436, 4267, 3758, 2402, 2911, 3758, 2741, 3250, 3419, 4097, 3758, 3758, 4097, 3589, 3250, 4606, 4097, 3589, 4267, 2741, 3758, 3928, 3928, 3080, 3758, 4606, 3419, 4436, 4267, 3928, 4097, 5284, 4436, 4436, 3928, 2911, 4436, 3080, 4097, 3758, 4267, 3758, 4436, 4606, 2911, 2741, 3758], bins=[x*100 for x in range(100)], range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, hold=None, data=None)

plt.show()