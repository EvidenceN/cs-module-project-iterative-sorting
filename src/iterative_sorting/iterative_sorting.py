# TO-DO: Complete the selection_sort() function below
# https://www.youtube.com/watch?v=B5m3L8aZifo&feature=youtu.be
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        index_to_right = cur_index + 1
        for a in range(index_to_right, len(arr)):
            if arr[a] < arr[smallest_index]:
                smallest_index = a

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr
    
def selection_sort_practice(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        index_to_right = cur_index + 1
        if index_to_right < smallest_index:

            # swap the positions of the 2 integers
            arr[smallest_index] = index_to_right
            arr[index_to_right] = smallest_index
        else:
            # the current number remains in it's position
            # then the next number becomes the current index
            cur_index = index_to_right

    return arr


def selection_sort_test2(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for a in arr[i:-1]:
            if a < smallest_index:
                new_smallest_index = a
                cur_index = new_smallest_index

                #print(new_smallest_index)

        # current element, 
        # find element smaller than current element
        # swap current element with smallest element

        # if the "i" is less than cur_index, then cur_index = i

        #for index 0, find items in everything to the right of index 0 that is bigger than zero. replace 0 with that item and move 0 into the position of the other item. 
        #Then move on to index 2. find item on the right of it that is smaller than it. If nothing on the right of 2 is smaller than 2, then just leave 2 where it is

        # TO-DO: swap
        # Your code here


    return arr



def selection_sort_test(arr):
    for i in arr:
        current = arr[i]
        for a in range(arr[i:-1]):
            if a < current:
                arr[current] = arr[a]
                arr[a] = arr[current]

        # current element, 
        # find element smaller than current element
        # swap current element with smallest element

        # if the "i" is less than cur_index, then cur_index = i

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0, len(arr) - 1):
        current = arr[i]
        next_current = arr[i+1]

        if next_current > current:
            arr[i] = next_current
            arr[i+1] = current
        else:
            current = arr[0]

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
