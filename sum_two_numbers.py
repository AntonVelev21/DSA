def two_sum(nums, target):
    reviewed_numbers = {}

    for i in range(len(nums)):
        curr_num = nums[i]
        target_num = target - curr_num
        if target_num in reviewed_numbers:
            return [reviewed_numbers[target_num], i]
        reviewed_numbers[curr_num] = i



print(two_sum(nums = [3, 2, 4], target = 6))