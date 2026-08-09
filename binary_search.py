list_of_numbers = [i for i in range(100)]
number = 5

def binary_search(list_of_nums: list):
    low = 0
    high = len(list_of_nums) - 1

    while low <= high:
        middle = (high - low) // 2 + low
        guess = list_of_nums[middle]
        if guess == number:
            return guess
        elif number < guess:
            high = middle - 1
        else:
            low = middle + 1

    return None


print(binary_search(list_of_numbers))
