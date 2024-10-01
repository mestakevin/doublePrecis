import random

# Function to generate a list of random numbers
def generate_random_list(n, lower_bound, upper_bound):
    random_list = []
    for i in range(n):
        random_number = random.randint(lower_bound, upper_bound)  
        random_list.append(random_number)
    return random_list

def main():
  n = int(1e3)
  lower_bound = 0
  upper_bound = 100
  random_list = generate_random_list(n, lower_bound, upper_bound)
  print(random_list)
  
main()
