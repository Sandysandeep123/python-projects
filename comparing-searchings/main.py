import random
import time as t
import sys
from searchings import *
from binary_search_tree import BinarySearchTree
from avl_tree import AVLTree

sys.setrecursionlimit(10000)

searching_times = {
    'linear search': {
        'adding': {
            'asc order': float,
            'randomly': float
        },
        'searching': {
            'asc order': 0.0,
            'randomly': 0.0
        },
    },
    'binary search': {
        'adding': {
            'asc order': 0.0,
            'randomly': 0.0
        },
        'searching': {
            'asc order': 0.0,
            'randomly': None
        },
    },
    'bst search': {
        'adding': {
            'asc order': 0.0,
            'randomly': 0.0
        },
        'searching': {
            'asc order': 0.0,
            'randomly': 0.0
        },
    },
    'avl tree search': {
        'adding': {
            'asc order': 0.0,
            'randomly': 0.0
        },
        'searching': {
            'asc order': 0.0,
            'randomly': 0.0
        },
    }
}

arr_adding_elements_in_asc_order = []
arr_adding_elements_randomly = []

avl_adding_elements_in_asc_order = AVLTree()
avl_adding_elements_randomly = AVLTree()

bst_adding_elements_in_asc_order = BinarySearchTree()
bst_adding_elements_randomly = BinarySearchTree()


def appending_time_checker():
    times = []
    times.append((t.time()))
    for i in range(0, 5000, 2):
        avl_adding_elements_in_asc_order.insert(i)
    times.append(t.time())
    for i in range(0, 5000, 2):
        bst_adding_elements_in_asc_order.insert(i)
    times.append(t.time())
    for i in range(0, 5000, 2):
        arr_adding_elements_in_asc_order.append(i)
    times.append(t.time())
    for i in range(0, 5000, 2):
        avl_adding_elements_randomly.insert(random.randint(0, 5000))
    times.append(t.time())
    for i in range(0, 5000, 2):
        bst_adding_elements_randomly.insert(random.randint(0, 5000))
    times.append(t.time())
    for i in range(0, 5000, 2):
        arr_adding_elements_randomly.append(random.randint(0, 5000))
    times.append(t.time())
    searching_times['avl tree search']['adding']['asc order'] = format(times[1] - times[0], "1.18f")
    searching_times['bst search']['adding']['asc order'] = format(times[2] - times[1], "1.18f")
    searching_times['linear search']['adding']['asc order'] = format(times[3] - times[2], "1.18f")
    searching_times['binary search']['adding']['asc order'] = format(times[3] - times[2], "1.18f")
    searching_times['avl tree search']['adding']['randomly'] = format(times[4] - times[3], "1.18f")
    searching_times['bst search']['adding']['randomly'] = format(times[5] - times[4], "1.18f")
    searching_times['linear search']['adding']['randomly'] = format(times[6] - times[5], "1.18f")
    searching_times['binary search']['adding']['randomly'] = format(times[6] - times[5], "1.18f")


def searching_time_checker():
    element_to_search_in_asc_order = 5000
    element_to_search_randomly = 5000
    times = []
    times.append(t.time())
    avl_adding_elements_in_asc_order.search(element_to_search_in_asc_order)
    times.append(t.time())
    bst_adding_elements_in_asc_order.search(element_to_search_in_asc_order)
    times.append(t.time())
    binary_searching(arr_adding_elements_in_asc_order, element_to_search_in_asc_order)
    times.append(t.time())
    linear_searching(arr_adding_elements_in_asc_order, element_to_search_in_asc_order)
    times.append(t.time())
    avl_adding_elements_randomly.search(element_to_search_randomly)
    times.append(t.time())
    bst_adding_elements_randomly.search(element_to_search_randomly)
    times.append(t.time())
    linear_searching(arr_adding_elements_randomly, element_to_search_randomly)
    times.append(t.time())
    searching_times['avl tree search']['searching']['asc order'] = format(times[1] - times[0], "1.15f")
    searching_times['bst search']['searching']['asc order'] = format(times[2] - times[1], "1.15f")
    searching_times['binary search']['searching']['asc order'] = format(times[3] - times[2], "1.15f")
    searching_times['linear search']['searching']['asc order'] = format(times[4] - times[3], "1.15f")
    searching_times['avl tree search']['searching']['randomly'] = format(times[5] - times[4], "1.15f")
    searching_times['bst search']['searching']['randomly'] = format(times[6] - times[5], "1.15f")
    searching_times['linear search']['searching']['randomly'] = format(times[7] - times[6], "1.15f")


def saving_to_file(file):
    file.write('\t\t\t\tin ascending order\t\t\t\trandomly ordered\n')
    for key in searching_times.keys():
        file.write(key + ':' + '\n')
        for add_or_search in searching_times[key].keys():
            file.write('\t\t\t\t')
            for how_added, time in searching_times[key][add_or_search].items():
                if time is None:
                    file.write(add_or_search + ' None\t\t')
                else:
                    file.write(add_or_search + ' ' + str(time) + '\t\t')
            file.write('\n')
        file.write('\n')


my_file = open('times.txt', 'w')
appending_time_checker()
searching_time_checker()
saving_to_file(my_file)
