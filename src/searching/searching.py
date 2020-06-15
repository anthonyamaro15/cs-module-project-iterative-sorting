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

    return -1  # not found


# lo = 0
# hi = len(arr)
# while lo < hi:
#    mid = (lo + hi) // 2

#    if arr[mid] == target:
#       return True
#    elif target < arr[mid]:
#       hi = mid
#    else:
#       lo = mid + 1

# return False

# def insertion_sort(arr):
#    for i in range(1, len(arr)):
#       temp = arr[i]
#       j = i
#       while j > 0 and temp < arr[j - 1]:
#          arr[i] = arr[j - 1]
#          j -= 1

#       arr[j] = temp
#    return arr
