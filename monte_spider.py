#Monte Carlo assignment
import numpy as np
#integrate probability



    
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
    function = np.ln(random_list[i]*(np.e-1))
    return function


def main():
