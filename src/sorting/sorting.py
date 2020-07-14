# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB) 
    merged_arr = [0] * elements

    i = 0 # smallest value in index of the left
    j = 0 # smallest value in index of the right

    # starting at the beginning of `a` and `b`
    while i < len(arrA) and j < len(arrB):
    # compare the next value of each
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else: 
            merged_arr.append(arrB[j])
            j += 1
    # add smallest to `merged_arr`
    merged_arr += arrA[i:]
    merged_arr += arrB[j:]
    

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    # recursively call merge_sort() on LHS
    left = merge_sort(arr[:middle])
    # recursively call merge_sort() on RHS
    right = merge_sort(arr[middle:])
    # merge sorted pieces
    return merge(left, right)

    

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




    