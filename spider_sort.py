import random

# Function to generate a list of random numbers
def generate_random_list(n):
    random_list = []
    for i in range(n):
        random_number = random.random()  
        random_list.append(random_number)
    return random_list

def main():
  n = 1e3
  random_list = generate_random_list(n)
  print(random_list)
