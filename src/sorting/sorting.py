# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB) 
    merged_arr = [0] * elements

    # starting at the beginning of `a` and `b`
    left = [0] * len(arrA)
    right = [0] * len(arrB)
    middle = len(merged_arr) // 2

    for i in range(0, arrA):
        left[i] = merged_arr[1 + i]

    for j in range(0, arrB):
        right[j] = merged_arr[middle + 1 + j]

    i = j = k = 0
    # compare the next value of each

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr[k] = left[i]
            i += 1
        else:
            merged_arr[k] = right[j]
            j += 1
        k += 1

    # add smallest to `merged_arr`
    
    while i < len(left):
        merged_arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        merged_arr[k] = right[j]
        j += 1
        k += 1

    

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        # recursively call merge_sort() on LHS
        merge_sort(left)
        # recursively call merge_sort() on RHS
        merge_sort(right)
        # merge sorted pieces
        merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

