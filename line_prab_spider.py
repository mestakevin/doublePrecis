#proposal function of uniform, line, and prabola.
import numpy as np
import math
import matplotlib.pyplot as plt

def proposal_func(x):
    #for line
    y = (1.71 * x) + 1.01
    return y

def draw_rand_points(num,func):
    pointlist = []
    x_rand_array = np.random.uniform(low=0.0, high=1.0, size=num)
    for i in x_rand_array:    
        y_rand_array = np.random.uniform(low=0.0, high=func(i), size=round(num*proposal_func(i)) )
        for j in y_rand_array:
            pointlist.append((i,j))

    return pointlist



def main():
    kept_xs = []
    kept_ys = [] 
    num_points = 1000
    hits = 0
    pointlist = draw_rand_points(num_points,proposal_func)
    for i in range(0,len(pointlist)-1,1):
        x_val = pointlist[i][0]
        y_val = pointlist[i][1]
        if (y_val <= (math.e ** x_val) ):
            hits += 1
            kept_xs.append(x_val)
            kept_ys.append(y_val)

    efficiency = hits/len(pointlist)
    print(efficiency) 

    plt.figure()
    plt.plot(kept_xs,kept_ys, '.')
    plt.ylabel('Function')
    plt.xlabel('Random Values')
    plt.title('Fuction Using Random Numbers')
    plt.show()

main()
