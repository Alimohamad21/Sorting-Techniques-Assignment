import time
from random import randint

from matplotlib import pyplot as pplot


def selection_sort(arr):
    indexing_length = range(0, len(arr) - 1)
    for i in indexing_length:
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]
    return arr


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        entered = False
        for j in range(len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                entered = True
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
        if not entered:
            break


def insertion_sort(arr, left=-10, right=-10):
    if left == -10 and right == -10:
        values = range(1, len(arr))
    else:
        values = range(left + 1, right + 1)
    for i in values:
        j = i - 1
        entered = False
        temp = arr[i]
        while temp < arr[j] and j >= 0:
            entered = True
            arr[j + 1] = arr[j]
            j -= 1
        if entered:
            arr[j + 1] = temp


def merge(arr, start, mid, end):
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            start2 += 1


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


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
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        n = n - 1
        heapify(arr, n, 0)


def calcMinRun(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r


def tim_sort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion_sort(arr, start, end)
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size


if __name__ == '__main__':
    random_arrays = []
    n = 10
    for i in range(4):
        random_array = []
        for j in range(n):
            random_array.append(randint(-10000, 10000))
        random_arrays.append(random_array)
        n *= 10

    sorting_functions = {'Insertion Sort': insertion_sort, 'Bubble Sort': bubble_sort, 'Selection Sort': selection_sort,
                         'Merge Sort': merge_sort, 'Heap Sort': heap_sort, 'Quick Sort': quick_sort,
                         'Built-in Sort': sorted, 'Tim sort': tim_sort}
    runtimes = dict()
    sizes = []
    for function in sorting_functions.keys():
        runtimes[function] = []
    for i in range(len(random_arrays)):
        size = len(random_arrays[i])
        sizes.append(size)
        print(
            f'\n---------------------------------------------------> ARRAY SIZE:{size} <---------------------------------------------------\n\n')
        for function in sorting_functions.keys():
            temp_inplace = random_arrays[i].copy()
            temp2 = random_arrays[i].copy()
            if i == 0:  # only prints for size 10 to avoid extremely long prints
                print(f'Array Before {function}:{temp_inplace}\n')
            start_time = time.time()
            if function == 'Built-in Sort':
                args = [temp2]
            else:
                args = [temp_inplace]
            if function == 'Quick Sort' or function == 'Merge Sort':
                args.append(0)
                args.append(len(temp_inplace) - 1)
            sorting_functions[function](*args)
            runtime = (time.time() - start_time)
            runtimes[function].append(runtime)
            if i == 0:  # only prints for size 10 to avoid extremely long prints
                if function == 'Built-in Sort':
                    print(f'Array After {function}:{sorting_functions[function](*args)}\n')
                else:
                    print(f'Array After {function}:{temp_inplace}\n')
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
