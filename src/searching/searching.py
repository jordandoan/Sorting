# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    # TO-DO: add missing code
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        if arr[mid] > target:
            high = mid - 1
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
      return -1 # array empty
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    if arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
