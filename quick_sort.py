array = [5, 7, 3, 1, 8, 9, 2, 4, 6, 10]

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [el for el in arr if el < pivot]
        more = [el for el in arr if el > pivot]

    return quicksort(less) + [pivot] + quicksort(more)




print(quicksort(array))

