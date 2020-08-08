def linear_search(arr, target):
    # Your code here
    for a, i in enumerate(arr):
        if i == target:
            return a
    
    return -1   # not found

linear_search([-2, 7, 3, -9, 5, 1, 0, 4, -6], -6)


# Write an iterative implementation of Binary Search
def binary_search_test(arr, target):
    new_arr = sorted(arr)

    if target in new_arr:
        return new_arr.index(target)
    else:
        return -1

def binary_search(my_list, search_item):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = my_list[middle]
        if guess == search_item:
            return middle
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def binary_search_recursive(arr, target):
    
    if len(arr) > 1:
        middle_item = arr[int(len(arr)/2)]
    else:
        return arr

    left = []
    right = []

    # checking if the middle item is the target
    if middle_item == target:
        return arr.index(middle_item)

    # adding everything to the left and right side to its own list
    else:
        for i in arr:
            if i < middle_item:
                left.append(i)
            else:
                right.append(i)
        return binary_search(left, target) + binary_search(right, target)
    
    return -1  # not found




def binary_search_test3(arr, target):
    while len(arr) > 1:
        middle_item = arr[int(len(arr)/2)]
        if middle_item == target:
            return arr.index(middle_item)
        elif middle_item < target:
            # re-define arr
            arr = arr[:middle_item]
            # repeat the process from beginning
            binary_search(arr, target)
            return arr.index(middle_item)
        elif middle_item > target:
            # redefine arr
            arr = arr[middle_item:]
            # repeat the process from beginning
            binary_search(arr, target)
            return arr.index(middle_item)
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


#binary_search([-2, 7, 3, -9, 5, 1, 0, 4, -6])

a = [-2, 7, 3, -9, 5, 1, 0, 4]
b = int(len(a)/2)
c = a[b]
a[int(len(a)/2)]

