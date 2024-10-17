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
    x_rand_array = np.random.uniform(low=0.0, high=math.pi, size=num)

    return x_rand_array

def choice_func(x):
    y = x**2 + x + 1
    return y

def fav_function(x):
    sine_fun = np.sin(x)
    return sine_fun

def fav_choice_fun(x):
    #y_fav = np.sin(x)
    y_fav = -0.4 * x**2 + 1.2 * x + 0.2
    return y_fav

##-----------------------------------------------------------------##
def main():
    # Set up integration limits and parameters
    up_lim = math.pi  # upper limit
    low_lim = 0  # lower_limit
    n = int(1e6)  # number of divisions for integration
    
    # Compute the integral using Trapezoidal rule
    value = trapz_rule_v1(n, up_lim, low_lim, fav_function)
    print(f"Trapezoidal= \t {value}")    
    area_true =  2
    hits = 0
    area_int = 0
    x_rand_array = draw_rand_points(n)
    domain = up_lim - low_lim
    print(domain)
    for i,value in enumerate(x_rand_array):
        area_int += math.sin(value) * domain/n
        
    print(area_int)
    print(2)
 	
    sum_of_px = 0
    for i, value in enumerate(x_rand_array):
        p_x = fav_choice_fun(value)
        sum_of_px += domain/p_x

    c = domain/sum_of_px
    print(c)
    choice_func_integral = 0
    for i, value in enumerate(x_rand_array):
        mini_chunk = fav_function(value) /(fav_choice_fun(value))
        choice_func_integral += mini_chunk

    print(choice_func_integral*c)

    plt.figure()
    plt.xlabel('')
    plt.ylabel('')
    plt.title('')
    plt.legend()
    plt.show()
##-----------------------------------------------------------------##
main()
##-----------------------------------------------------------------##
#small change 
