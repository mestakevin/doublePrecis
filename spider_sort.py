import random
import time
import matplotlib.pyplot as plt

def bubbleSort(a_list):
    length = len(a_list)
    temp_list = []
    time_now = time.time()
    for i in range(0, length-1):
        for j in range(i):
            if a_list[i] > a_list[i+1]:
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

def heap(list):
    """
    Heap Sort
    """
    start_time = time.time()
    build_max_heap(list)
    for i in range (n, 1, -1):
        n -= 1
        heapify(list, i, n)
    end_time = time.time()
    tot_time = end_time - start_time
    return list, tot_time

def build_max_heap(list):
    n = len(list)
    for i in range (n / 2, 1, -1):
        heapify(list, i, n)

def heapify(list, i, n):
    left = 2 * i
    right = 2 * i + 1

    if (left <= n) and (list[left] > list[i]):
        max = left
    else:
        max = i

    if(right <= n) and (list[right] > list[max]):
        max = right
    if (max != i):
        swap = list[i]
        list[i] = list[max]
        list[max] = swap
        heapify(list, max)

def main():
   #initilaize empty time lists 
    bubble_time_list= []
    heap_time_list = []

    for i in range(1,N,1):
        cur_list = generate_random_list(i, 0, 100)
        bubble_sorted_list, bubble_tot_time = bubbleSort(cur_list)
        bubble_time_list.append(bubble_tot_time)
       
       #NOT WORKING CURRENTLY
       #heap_sorted_list, heap_tot_time = heap(cur_list)
       #heap_time_list.append(heap_tot_time)
        

    #plotting
    plt.plot(range(1,N,1), bubble_time_list, label='Bubble Sort')
    #not working currently
    #plt.plot(range(1,N,1), heap_time_list, label='Heap Sort')
    plt.xlabel('List Size')
    plt.ylabel('Time')
    plt.title('Lists as A Function of List Size')
    plt.legend()
    plt.grid()
    plt.show()

main()
