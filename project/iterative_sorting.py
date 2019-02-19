# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) - 1):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = cur
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    n = len(arr)
    if n == 0:
        return arr
    for ele in arr:
        if ele < 0:
            return "Error, negative numbers not allowed in Count Sort"
    if maximum == -1:
        maximum = arr[0]
        for ele in arr:
            if ele > maximum:
                maximum = ele
    m = maximum + 1
    count = [0] * m
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr
