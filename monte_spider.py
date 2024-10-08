#Monte Carlo assignment
import numpy as np
import matplotlib.pyplot as plt
import random

# list of random numbers
def generate_random_list(n, lower_bound=0, upper_bound=1):
    random_list = [random.uniform(lower_bound, upper_bound) for _ in range(n)]
    return random_list

# CDF function
def inverse_cdf(random_list):
    function = [np.log(num * (np.e - 1)+1) for num in random_list]
    return function

def main():
    n = 1000  
    random_list = generate_random_list(n)
    function = inverse_cdf(random_list)

    # x values for plotting
    x = np.linspace(0, 1, n)

    function_sorted = np.sort(function)

    plt.hist(function_sorted, bins = 50, color='darkblue', density = True, alph$
    plt.ylabel('Inverse CDF Values')
    plt.xlabel('Random Values')
    plt.title('Inverse CDF of Random Numbers')

    plt.grid()
    plt.show()

main()


