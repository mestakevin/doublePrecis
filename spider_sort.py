
def bubbleSort(a_list):
    length = len(a_list)
    temp_list = []
    for i in range(0, length-1):
        for j in i:
            if a_list[i] > a_list[i+1]
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp

    return a_list
            

def main():
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

#plotting
plt.plot(,random_list)
plt.xlabel('List Size')
plt.ylabel('List Values')
plt.title('Lists as A Function of List Size')
plt.grid()

plt.show()

main()
