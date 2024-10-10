import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sp

##-----------------------------------------------------------------##
def func(x):
    y = e**x
    return y 


def draw_rand_points(num):
    x_rand_array = np.random.uniform(low=0.0, high=1.0, size=num)
    y_rand_array = np.random.uniform(low=0.0, high=math.e, size=num)

    return x_rand_array, y_rand_array




##-----------------------------------------------------------------##
def main():
    area =  math.e
    hits = 0
    
    x_rand_array, y_rand_array = draw_rand_points(10000)

    for i,value in enumerate(x_rand_array):
        x_val =  value
        y_val = y_rand_array[i]
        if  y_val <= math.e ** x_val:
            hits += 1
   


    integral = area * (hits/10000)
    print(integral)
    print(math.e - 1)
 	
    plt.figure()
    plt.xlabel('')
    plt.ylabel('')
    plt.title('')
    plt.legend()
    plt.show()
##-----------------------------------------------------------------##
main()
##-----------------------------------------------------------------##
 
