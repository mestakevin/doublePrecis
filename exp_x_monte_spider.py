import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sp

##-----------------------------------------------------------------##
def trapz_rule_v1(n, up_lim, low_lim, func):
    delta_x = (up_lim - low_lim) / n
    k_sum = 0.0
    for i in range(1, n):
        temp_val = func(low_lim + (i * delta_x))
        k_sum += temp_val
    temp_val2 = (func(up_lim) + func(low_lim)) / 2
    final_val = delta_x * (temp_val2 + k_sum)
    return final_val
##-----------------------------------------------------------------##
def func(x):
    y = (math.e)**x
    return y
##-----------------------------------------------------------------##
def draw_rand_points(num):
    x_rand_array = np.random.uniform(low=0.0, high=1.0, size=num)
    y_rand_array = np.random.uniform(low=0.0, high=math.e, size=num)

    return x_rand_array, y_rand_array
##-----------------------------------------------------------------##
def main():
    # Set up integration limits and parameters
    up_lim = 1  # upper limit
    low_lim = 0  # lower_limit
    n = int(1e3)  # number of divisions for integration
    
    # Compute the integral using Trapezoidal rule
    value = trapz_rule_v1(n, up_lim, low_lim, func)
    print(f"Trapezoidal= \t {value}")    
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
 
