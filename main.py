import time
from random import randint

from matplotlib import pyplot as pplot
from numpy import random


def selection_sort(arr):
    """TODO"""


def bubble_sort(arr):
    """TODO"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        entered = False
        temp = arr[i]
        while temp < arr[j] and j >= 0:
            entered = True
            arr[j + 1] = arr[j]
            j -= 1
        if entered:
            arr[j + 1] = temp


def merge_sort(arr):
    """TODO"""


def quick_sort(arr):
    """TODO"""


def heap_sort(arr):
    """TODO"""


if __name__ == '__main__':
    random_arrays = []
    for i in range(6):
        random_array = random.randint(-10000, 10000, size=randint(100, 10000))
        random_arrays.append(random_array)
    random_arrays.sort(key=len)  # sort according to array size,useful for plot
    sorting_functions = {'Insertion Sort': insertion_sort, 'Bubble Sort': bubble_sort, 'Selection Sort': selection_sort,
                         'Merge Sort': merge_sort, 'Quick Sort': quick_sort, 'Heap Sort': heap_sort}
    runtimes = dict()
    sizes = []
    for function in sorting_functions.keys():
        runtimes[function] = []
    for i in range(len(random_arrays)):
        size = len(random_arrays[i])
        sizes.append(size)
        print(
            f'\n----------------------------------------------------------------------> ARRAY SIZE:{size} <----------------------------------------------------------------------\n\n')
        for function in sorting_functions.keys():
            temp = random_arrays[i].copy()
            runtime = dict()
            # print(f'Array Before {function}:{temp}\n')
            start_time = time.time()
            sorting_functions[function](temp)
            runtime[function] = (time.time() - start_time) * 1000
            runtimes[function].append(runtime[function])
            # print(f'Array After {function}:{temp}\n')
            print(f'{function} Runtime:{runtime[function]} ms\n')
            print('\n\n\n********************************************************************************\n\n\n')
    print(sizes)
    print(runtimes)
    for function in sorting_functions.keys():
        pplot.plot(sizes, runtimes[function])
    pplot.legend(sorting_functions.keys())
    pplot.xlabel('Array Size')
    pplot.ylabel('Run time (milliseconds)')
    pplot.show()
