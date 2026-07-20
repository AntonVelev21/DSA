numbers = [4, 5, 2, 7, 9, 10, 3, 8, 1, 6]

def finds_smallest_num_index(list_of_nums: list):
    smallest_num = list_of_nums[0]
    index = 0
    for i in range(len(list_of_nums) - 1):
        num = list_of_nums[i]
        if num < smallest_num:
            smallest_num = num
            index = i

    return index


def selection_sort(list_of_nums: list):
    result = []
    for _ in range(len(list_of_nums) - 1):
        smallest_num_index = finds_smallest_num_index(list_of_nums)
        num = list_of_nums[smallest_num_index]
        list_of_nums.pop(smallest_num_index)
        result.append(num)

    return result

print(selection_sort(list_of_nums=numbers))



