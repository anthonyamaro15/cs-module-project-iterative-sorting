def linear_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    l = 0
    h = len(arr)
    while l < h:
        mid = (l + h) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            h = mid
        else:
            l = mid + 1

    return -1  # not found

