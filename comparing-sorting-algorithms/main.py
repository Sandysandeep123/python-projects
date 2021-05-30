import random
import time as t
import sys
import numpy as np

sys.setrecursionlimit(5000)

times_without_numpy = {'bubble sort': {}, 'merge sort': {}, 'insertion sort': {}, 'quick sort': {}}
times_with_numpy = {'bubble sort': {}, 'merge sort': {}, 'insertion sort': {}, 'quick sort': {}}


class TimeCheck:

    @staticmethod
    def for_bubble_sort():
        array1 = array_sorted_in_ascending_order.copy()
        array2 = array_sorted_in_descending_order.copy()
        array3 = array_with_random_elements.copy()
        array4 = array_with_ascending_descending_elements.copy()
        array5 = array_with_ascending_descending_elements.copy()
        t1 = t.time()
        bubble_sort(array1)
        t2 = t.time()
        bubble_sort(array2)
        t3 = t.time()
        bubble_sort(array3)
        t4 = t.time()
        bubble_sort(array4)
        t5 = t.time()
        bubble_sort(array5)
        t6 = t.time()
        bubble_sort_times = {'ascending order': t2 - t1,
                             'descending order': t3 - t2,
                             'random order   ': t4 - t3,
                             'asc-descending ': t5 - t4,
                             'desc-ascending ': t6 - t5
                             }
        times_without_numpy['bubble sort'] = bubble_sort_times

    @staticmethod
    def for_merge_sort():
        array1 = array_sorted_in_ascending_order.copy()
        array2 = array_sorted_in_descending_order.copy()
        array3 = array_with_random_elements.copy()
        array4 = array_with_ascending_descending_elements.copy()
        array5 = array_with_ascending_descending_elements.copy()
        t1 = t.time()
        merge_sort(array1)
        t2 = t.time()
        merge_sort(array2)
        t3 = t.time()
        merge_sort(array3)
        t4 = t.time()
        merge_sort(array4)
        t5 = t.time()
        bubble_sort(array5)
        t6 = t.time()
        merge_sort_times = {'ascending order': t2 - t1,
                            'descending order': t3 - t2,
                            'random order   ': t4 - t3,
                            'asc-descending ': t5 - t4,
                            'desc-ascending ': t6 - t5
                            }
        times_without_numpy['merge sort'] = merge_sort_times

    @staticmethod
    def for_insertion_sort():
        array1 = array_sorted_in_ascending_order.copy()
        array2 = array_sorted_in_descending_order.copy()
        array3 = array_with_random_elements.copy()
        array4 = array_with_ascending_descending_elements.copy()
        array5 = array_with_ascending_descending_elements.copy()
        t1 = t.time()
        insertion_sort(array1)
        t2 = t.time()
        insertion_sort(array2)
        t3 = t.time()
        insertion_sort(array3)
        t4 = t.time()
        insertion_sort(array4)
        t5 = t.time()
        bubble_sort(array5)
        t6 = t.time()
        insertion_sort_times = {'ascending order': t2 - t1,
                                'descending order': t3 - t2,
                                'random order   ': t4 - t3,
                                'asc-descending ': t5 - t4,
                                'desc-ascending ': t6 - t5
                                }
        times_without_numpy['insertion sort'] = insertion_sort_times

    @staticmethod
    def for_quicksort():
        array1 = array_sorted_in_ascending_order.copy()
        array2 = array_sorted_in_descending_order.copy()
        array3 = array_with_random_elements.copy()
        array4 = array_with_ascending_descending_elements.copy()
        array5 = array_with_ascending_descending_elements.copy()
        t1 = t.time()
        quicksort(array1)
        t2 = t.time()
        quicksort(array2)
        t3 = t.time()
        quicksort(array3)
        t4 = t.time()
        quicksort(array4)
        t5 = t.time()
        bubble_sort(array5)
        t6 = t.time()
        quicksort_times = {'ascending order ': t2 - t1,
                           'descending order': t3 - t2,
                           'random order   ': t4 - t3,
                           'asc-descending ': t5 - t4,
                           'desc-ascending ': t6 - t5
                           }
        times_without_numpy['quick sort'] = quicksort_times


class TimeCheckWithNumPy:

    @staticmethod
    def for_bubble_sort():
        array1 = array_sorted_in_ascending_order_numpy.copy()
        array2 = array_sorted_in_descending_order_numpy.copy()
        array3 = array_with_random_elements_numpy.copy()
        array4 = array_with_ascending_descending_elements_numpy.copy()
        array5 = array_with_descending_ascending_elements_numpy.copy()
        t1 = t.time()
        bubble_sort(array1)
        t2 = t.time()
        bubble_sort(array2)
        t3 = t.time()
        bubble_sort(array3)
        t4 = t.time()
        bubble_sort(array4)
        t5 = t.time()
        bubble_sort(array5)
        t6 = t.time()
        bubble_sort_times = {'ascending order': t2 - t1,
                             'descending order': t3 - t2,
                             'random order   ': t4 - t3,
                             'asc-descending ': t5 - t4,
                             'desc-ascending ': t6 - t5
                             }
        times_with_numpy['bubble sort'] = bubble_sort_times

    @staticmethod
    def for_merge_sort():
        array1 = array_sorted_in_ascending_order_numpy.copy()
        array2 = array_sorted_in_descending_order_numpy.copy()
        array3 = array_with_random_elements_numpy.copy()
        array4 = array_with_ascending_descending_elements_numpy.copy()
        array5 = array_with_descending_ascending_elements_numpy.copy()
        t1 = t.time()
        merge_sort(array1)
        t2 = t.time()
        merge_sort(array2)
        t3 = t.time()
        merge_sort(array3)
        t4 = t.time()
        merge_sort(array4)
        t5 = t.time()
        bubble_sort(array5)
        t6 = t.time()
        merge_sort_times = {'ascending order': t2 - t1,
                            'descending order': t3 - t2,
                            'random order   ': t4 - t3,
                            'asc-descending ': t5 - t4,
                            'desc-ascending ': t6 - t5
                            }
        times_with_numpy['merge sort'] = merge_sort_times

    @staticmethod
    def for_insertion_sort():
        array1 = array_sorted_in_ascending_order_numpy.copy()
        array2 = array_sorted_in_descending_order_numpy.copy()
        array3 = array_with_random_elements_numpy.copy()
        array4 = array_with_ascending_descending_elements_numpy.copy()
        array5 = array_with_descending_ascending_elements_numpy.copy()
        t1 = t.time()
        insertion_sort(array1)
        t2 = t.time()
        insertion_sort(array2)
        t3 = t.time()
        insertion_sort(array3)
        t4 = t.time()
        insertion_sort(array4)
        t5 = t.time()
        bubble_sort(array5)
        t6 = t.time()
        insertion_sort_times = {'ascending order': t2 - t1,
                                'descending order': t3 - t2,
                                'random order   ': t4 - t3,
                                'asc-descending ': t5 - t4,
                                'desc-ascending ': t6 - t5
                                }
        times_with_numpy['insertion sort'] = insertion_sort_times

    @staticmethod
    def for_quicksort():
        array1 = array_sorted_in_ascending_order_numpy.copy()
        array2 = array_sorted_in_descending_order_numpy.copy()
        array3 = array_with_random_elements_numpy.copy()
        array4 = array_with_ascending_descending_elements_numpy.copy()
        array5 = array_with_descending_ascending_elements_numpy.copy()
        t1 = t.time()
        quicksort(array1)
        t2 = t.time()
        quicksort(array2)
        t3 = t.time()
        quicksort(array3)
        t4 = t.time()
        quicksort(array4)
        t5 = t.time()
        bubble_sort(array5)
        t6 = t.time()
        quicksort_times = {'ascending order ': t2 - t1,
                           'descending order': t3 - t2,
                           'random order   ': t4 - t3,
                           'asc-descending ': t5 - t4,
                           'desc-ascending ': t6 - t5
                           }
        times_with_numpy['quick sort'] = quicksort_times


def bubble_sort(array):
    for num in range(len(array) - 1, 0, -1):
        for i in range(num):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        nxt_element = array[i]
        while (array[j] > nxt_element) and (j >= 0):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = nxt_element
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


# default arrays
array_sorted_in_ascending_order = [i for i in range(0, 1600, 1)]
array_sorted_in_descending_order = [i for i in range(1600, 0, -1)]
array_with_random_elements = [random.randint(1, 1600) for i in range(1600)]

# first 800 elements are ascending, last 800 - descending
array_with_ascending_descending_elements = [i for i in range(0, 800, 1)]

# first 800 elements are descending, last 800 - ascending
array_with_descending_ascending_elements = [i for i in range(800, 0, -1)]
tmp = [i for i in range(800, 0, -1)]
for i in range(800):
    array_with_ascending_descending_elements.append(tmp[i])
    array_with_descending_ascending_elements.append(tmp[799 - i])

print('tutaj1')
# using numPy library
array_sorted_in_ascending_order_numpy = np.arange(0, 1600, 1)
array_sorted_in_descending_order_numpy = np.arange(1600, 0, -1)
array_with_random_elements_numpy = np.random.randint(1600, size=1600)
array_with_ascending_descending_elements_numpy = np.arange(0, 800, 1)
array_with_ascending_descending_elements_numpy = np.append(array_with_ascending_descending_elements_numpy,
                                                           np.arange(800, 0, -1), axis=0)
array_with_descending_ascending_elements_numpy = np.arange(800, 0, -1)
array_with_descending_ascending_elements_numpy = np.append(array_with_descending_ascending_elements_numpy,
                                                           np.arange(0, 800, 1), axis=0)
print('tutaj2')

check = TimeCheck()
check.for_bubble_sort()
check.for_merge_sort()
check.for_insertion_sort()
check.for_quicksort()
print('tutaj3')

checkNP = TimeCheckWithNumPy()
checkNP.for_bubble_sort()
checkNP.for_merge_sort()
checkNP.for_insertion_sort()
checkNP.for_quicksort()
print('tutaj4')


def saving_times_to_file(times, times_numpy, file):
    for sortingAlgorithm in times.keys():
        file.write(sortingAlgorithm + '\t\t\t\twithout numPy\t\t\twith numPy:\n')
        for name, time in times[sortingAlgorithm].items():
            file.write('\t' + name + ' \t' +
                       str(round(time, 17)) + '\t\t' +
                       str(round(times_numpy[sortingAlgorithm].get(name), 17)) + '\n')
        file.write('\n')


times_file = open('times.txt', 'w')
saving_times_to_file(times_without_numpy, times_with_numpy, times_file)
