#Monte Carlo assignment

# Function to generate a list of random numbers
def generate_random_list(n, lower_bound, upper_bound):
    random_list = []
    for i in range(0,1):
        random_number = random.uniform(lower_bound, upper_bound)  
        random_list.append(random_number)
    return random_list

