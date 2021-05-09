import time

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


def merge(a, b):
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    while a:
        c.append(a[0])
        a.pop(0)

    while b:
        c.append(b[0])
        b.pop(0)

    return c


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    arrayOne = []
    arrayTwo = []

    for i in range(0, len(arr) // 2):
        arrayOne.append(arr[i])

    for i in range(len(arr) // 2, len(arr)):
        arrayTwo.append(arr[i])

    arrayOne = merge_sort(arrayOne)
    arrayTwo = merge_sort(arrayTwo)

    return merge(arrayOne, arrayTwo)


def quick_sort(arr):
    """TODO"""


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    max = i
    if left < n:
        if arr[left] > arr[i]:
            max = left
        else:
            max = i

    if right < n:
        if arr[right] > arr[max]:
            max = right

    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        heapify(arr, n, max)


def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        n = n - 1
        heapify(arr, n, 0)


if __name__ == '__main__':
    random_arrays = []
    n = 10
    for i in range(4):
        random_array = random.randint(-10000, 10000, size=n)
        random_arrays.append(random_array)
        n *= 10
    sorting_functions = {'Insertion Sort': insertion_sort, 'Bubble Sort': bubble_sort, 'Selection Sort': selection_sort,
                         'Merge Sort': merge_sort, 'Quick Sort': quick_sort, 'Heap Sort': heap_sort,
                         'Built-in Sort': sorted}
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

            # print(f'Array Before {function}:{temp}\n')
            start_time = time.time()
            sorting_functions[function](temp)
            runtime = (time.time() - start_time)
            runtimes[function].append(runtime)
            # if function == 'Merge Sort' or function == 'Built-in Sort':
            # print(f'Array After {function}:{sorting_functions[function](temp)}\n')
            # else:
            # print(f'Array After {function}:{temp}\n')
            print(f'{function} Runtime:{runtime} s\n')
            print('\n\n\n********************************************************************************\n\n\n')
    print(sizes)
    print(runtimes)
    i = 0
    for function in sorting_functions.keys():
        pplot.plot(sizes, runtimes[function])

    function_names = tuple(sorting_functions.keys())
    pplot.legend(function_names)
    pplot.xlabel('Array Size')
    pplot.ylabel('Run time (in seconds)')
    pplot.ylim([0, 1])
    pplot.show()
