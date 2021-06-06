def binary_searching(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        guess = arr[mid]
        if guess == item:
            return mid
        elif item < guess:
            high = mid - 1
        else :
            low = mid + 1
    return None


def linear_searching(arr, item):
    for i in arr:
        if i == item:
            return i
    return None
