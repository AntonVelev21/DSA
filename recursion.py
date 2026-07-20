def recursive_function(num):
    print(num)
    if num == 0:
        return
    else:
        recursive_function(num - 1)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)



array = [1, 2, 3, 4, 5, 1, 10, 4]
start_index = 0

def sum_nums(i, arr):
    if i == len(arr) - 1:
        return arr[i]
    else:
        return arr[i] + sum_nums(i + 1, arr)



low = 0
high = len(array) - 1
middle = (high - low) // 2 + low
target = 6

def binary_search_recursion(arr, lowest, highest, mid, actual_num):
    if lowest > highest:
        return None

    if actual_num == arr[mid]:
        return arr[mid]

    elif actual_num < arr[mid]:
        highest = mid - 1

    else:
        lowest = mid + 1

    mid = (highest - lowest) // 2 + lowest
    return binary_search_recursion(arr, lowest, highest, mid, actual_num)


index = 0
max_num = 0

def max_num_recursion(arr, i, biggest_num):
    if i == len(arr):
        return biggest_num

    if arr[i] > biggest_num:
        biggest_num = arr[i]


    return max_num_recursion(arr, i + 1, biggest_num)


print(max_num_recursion(array, index, max_num))