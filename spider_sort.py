import random
import time
import matplotlib.pyplot as plt

N = 1000

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

def heapify(arr, n, i):
    """
    This method does the heap tree swapping, and remove the highest number while sorted.
        'n' -- size of the heap binary tree, 
        'i' -- current tree node index
    """
    largest = i  # initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    if left < n and arr[left] > arr[largest]:              # if left child exists and is larger than root
        largest = left

    if right < n and arr[right] > arr[largest]:            # if right child exists and is larger than largest so far
        largest = right

    if largest != i:                                       # if largest is not root

        arr[i], arr[largest] = arr[largest], arr[i]        # swap
        heapify(arr, n, largest)                           # recursion until the tree is heapified


def heap(arr):
    """
    Function to perform heap sort on the input list 'arr'.
    """

    time_start = time.time()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):                     # maxheap

        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):                           # extract elements
        arr[i], arr[0] = arr[0], arr[i]                     # swap the current root (largest element) with the end of the heap
        heapify(arr, i, 0)                                  # call heapify on the reduced heap


    time_end = time.time()                     
    time_tot = time_end - time_start                        # time diff

    return arr, time_tot                                    # return the sorted array and time

def main():
   #initilaize empty time lists 
    bubble_time_list= []
    heap_time_list = []

    for i in range(1,N,1):
        cur_list = generate_random_list(i, 0, 100)
        bubble_sorted_list, bubble_tot_time = bubbleSort(cur_list)
        bubble_time_list.append(bubble_tot_time)
       
        #NOT WORKING CURRENTLY
        heap_sorted_list, heap_tot_time = heap(cur_list)
        heap_time_list.append(heap_tot_time)
        

    #plotting
    plt.plot(range(1,N,1), bubble_time_list, color = '#007ba7', label='Bubble Sort')
    plt.plot(range(1,N,1), heap_time_list, color = '#f6adc6', label='Heap Sort')
    plt.xlabel('List Size')
    plt.ylabel('Time')
    plt.title('Lists as A Function of List Size')
    plt.legend()
    plt.grid()

    plot_destination = "figures/bubble_heap_compare.png"
    plt.savefig(plot_destination, dpi=500)

main()
