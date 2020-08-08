def linear_search(arr, target):
    # Your code here
    for a, i in enumerate(arr):
        if i == target:
            return a
    
    return -1   # not found

linear_search([-2, 7, 3, -9, 5, 1, 0, 4, -6], -6)


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    middle_item = arr[int(len(arr)/2)]
    if middle_item == target:
        return middle_item
    elif middle_item < target:
        binary_search(arr[:middle_item], target)
    elif middle_item > target:
        binary_search(arr[middle_item:], target)
    else:
        return -1  # not found













def binary_search_test(arr, target):

    # Your code here
    # find the length of the arr, then divide it by 2, and then use that number to find the index of the middle value
    middle_item = arr[int(len(arr)/2)]
    #left_items = arr[:middle_item] 
    #right_items = arr[middle_item:]
    #left_middle = left_items[int(len(left_items)/2)]
    #right_middle = right_items[int(len(right_items)/2)]

    if middle_item == target:
        return middle_item
    elif middle_item < target:
        binary_search(arr[:middle_item], target)
    else:
        binary_search(arr[middle_item:], target)

    return -1  # not found


binary_search([-2, 7, 3, -9, 5, 1, 0, 4, -6])

a = [-2, 7, 3, -9, 5, 1, 0, 4]
b = int(len(a)/2)
c = a[b]
a[int(len(a)/2)]

