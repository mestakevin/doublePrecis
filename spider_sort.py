import random
import time
from matplotlib import pyplot as plt

def bubbleSort(a_list):
    length = len(a_list)
    temp_list = []
    time_now = time.time()
    for i in range(0, length-1):
        for j in i:
            if a_list[i] > a_list[i+1]
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp
    time_end = time.time()
    tot_time = time_end - time_now
    return a_list, tot_time
            

# Function to generate a list of random numbers
def generate_random_list(n, lower_bound, upper_bound):
    random_list = []
    for i in range(n):
        random_number = random.randint(lower_bound, upper_bound)  
        random_list.append(random_number)
    return random_list

def main():
  n = int(1e3)
  N = 10 #final  
  lower_bound = 0
  upper_bound = 100
  random_list = generate_random_list(n, lower_bound, upper_bound)
  print(random_list)
  for i in range (0, N):
      length = len(random_list)
  return length
#plotting
    plt.plot(time,length)
    plt.xlabel('Time')
    plt.ylabel('List size')
    plt.title('List size as a Function of Time')
    plt.grid()

    n = int(1e3)
    N = 1000 #final  
    lower_bound = 0
    upper_bound = 100
    random_list = generate_random_list(n, lower_bound, upper_bound)
    print(random_list)
    time_list=[]

    for i in range(1,N,1):
        cur_list = generate_random_list(i, 0, 100)
        sorted_list, tot_time = bubbleSort(cur_list)
        time_list.append(tot_time)

    #plotting
    plt.plot(range(1,N,1), time_list)
    plt.xlabel('List Size')
    plt.ylabel('List Values')
    plt.title('Lists as A Function of List Size')
    plt.grid()

    plt.show()
main()
