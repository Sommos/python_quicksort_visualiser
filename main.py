import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        yield from quicksort(arr, low, pivot_index)
        yield from quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1

        while arr[i] < pivot:
            i += 1
        
        j -=1

        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

        yield arr

