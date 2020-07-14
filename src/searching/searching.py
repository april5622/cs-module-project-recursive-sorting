# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # BASE CASE
    # A loop that will continue while the start is less than or equal to the end
    if end >= start:
        # find the middle by averaging the start and end and dividing by 2
        middle = (start + end) // 2
        # guess is the middle index needed to retreive the target with the index from the arr
        guess = arr[middle]
        # if the guess is equal to the target, the middle index is correct and will be returned
        if guess == target:
            return middle
        # if guess is greater than the target, binary search into LHS
        elif guess > target:
            # RECURSIVE CASE
            return binary_search(arr, target, start, middle - 1)
        # if guess is lesser than the target, binary search into RHS
        else:
            # RECURSIVE CASE
            return binary_search(arr, target, end, middle + 1)
    else:
        return -1  # not found




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
