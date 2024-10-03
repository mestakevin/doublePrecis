#Monte Carlo assignment

# Function to generate a list of random numbers
def generate_random_list(n, lower_bound, upper_bound):
    lower_bound = 0
    upper_bound = 1
    random_list = []
    for i in range(n):
        random_number = random.uniform(lower_bound, upper_bound)  
        random_list.append(random_number)
    return random_list

