# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    curr = a = b = 0
    while a <= len(arrA) - 1 and b <= len(arrB) - 1:
        if arrA[a] < arrB[b]:
            merged_arr[curr] = arrA[a]
            a += 1
        else:
            merged_arr[curr] = arrB[b]
            b += 1
        curr += 1
    if a >= len(arrA):
        merged_arr[curr:] = arrB[b:]
    else:
        merged_arr[curr:] = arrA[a:]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) == 1:
        return arr
    mid = (len(arr)) // 2
    LHS = merge_sort(arr[:mid])
    RHS = merge_sort(arr[mid:])
    return merge(LHS, RHS)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    print(start, mid, end)
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if r - l == 1 or l == r:
        return l
    mid = (l + r) // 2
    LHS = merge_sort_in_place(arr, l, mid)
    RHS = merge_sort_in_place(arr, mid, r)
    merge_in_place(arr, LHS, mid, RHS)
    # return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr


arr = [10, 8, 5, 3]
# print(merge_sort(arr))
# print(merge_sort_in_place(arr, 0, len(arr)))