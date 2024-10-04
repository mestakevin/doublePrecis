#Monte Carlo assignment
import numpy as np
import matplotlib.pyplot as plt
import random

    
# Function to generate a list of random numbers
def generate_random_list(n, lower_bound, upper_bound):
    lower_bound = 0
    upper_bound = 1
    random_list = []
    for i in range(n):
        random_number = random.uniform(lower_bound, upper_bound)  
        random_list.append(random_number)
    return random_list

#inverse cdf function
def inverse_cdf(random_list):
    function = [np.log(num * (np.e - 1)) for num in random_list]
    return function


def main():
