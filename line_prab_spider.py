#proposal function of uniform, line, and prabola.

## rejection method for e^x

import numpy as np
import math
import matplotlib.pyplot as plt

def draw_rand_points(num):
    x_rand_array = np.random.uniform(low=0.0, high=1.0, size=num)
    upper_bound = math.e + 0.01 #upper bound of function
    y_rand_array = np.random.uniform(low=0.0, high=upper_bound, size=num)
    return x_rand_array, y_rand_array


def main():
    num_points = 10000
    rand_x, rand_y = draw_rand_points(num_points)
    kept_xs = []
    kept_ys = []
    for i in range(0,len(rand_x)-1,1):
        x_val = rand_x[i]
        y_val = rand_y[i]
        if (y_val <= (1.71*num_points + 1.01) ):
            kept_xs.append(x_val)
            kept_ys.append(y_val)

 
    plt.figure
    plt.plot(kept_xs,kept_ys)
    plt.show()

main()
