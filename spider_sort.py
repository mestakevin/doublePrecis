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
  N = 1000 #final  
  lower_bound = 0
  upper_bound = 100
  random_list = generate_random_list(n, lower_bound, upper_bound)
  print(random_list)
  for i in range (len(random_list), N):
      
  return list_size
#plotting
plt.plot(time,list_size)
plt.xlabel('List Size')
plt.ylabel('List Values')
plt.title('Lists as A Function of List Size')
plt.grid()

plt.show()


main()
