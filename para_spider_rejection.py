
## parabola rejection method for e^x

import numpy as np
import math
import matplotlib.pyplot as plt

def draw_rand_points(num,func):
    pointlist = []
    x_rand_array = np.random.uniform(low=0.0, high=1.0, size=num)
    for i in x_rand_array:    
        y_rand_array = np.random.uniform(low=0.0, high=func(i), size=round(num*func(i)) )
        for j in y_rand_array:
            pointlist.append((i,j))

    return pointlist


def func(x):
    return x**2 + x + 1


def main():
    num_points = 10000
    hits = 0
    pointlist = draw_rand_points(num_points,func)
    for i in range(0,len(pointlist)-1,1):
        x_val = pointlist[i][0]
        y_val = pointlist[i][1]
        if (y_val <= (math.e ** x_val) ):
            hits += 1

    efficiency = hits/len(pointlist)
    print(efficiency)    
 

main()
