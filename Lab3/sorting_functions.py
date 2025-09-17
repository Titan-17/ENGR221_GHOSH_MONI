"""
Name: Moni Ghosh
sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1
    return A
    pass

def bubble_sort(arr):
# AI Made
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

    pass

def create_random_list(length):
    """ Returns a list of the given length with random values.
        Input: 
            length (int) - Desired length of the list """
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def get_runtime(function_to_run, list_length):
    """ Returns the duration (in seconds) that it took for 
        function_to_run to sort a list of length list_length.
        Input: 
            function_to_run (function) - Name of the function
            list_length (int) - Length of the list to sort """
    # Create a new list to sort
    list_to_sort = create_random_list(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time

if __name__ == '__main__':
    print(get_runtime(bubble_sort, 100))