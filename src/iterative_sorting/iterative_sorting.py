# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                unsorted = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

print(bubble_sort([5,4,2,3,1]))