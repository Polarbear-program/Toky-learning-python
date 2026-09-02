def rotate_left3(nums):
    empty_list = []
    empty_list.insert(0, nums[1])
    empty_list.insert(1, nums[2])
    empty_list.insert(2, nums[0])
    return empty_list


print(rotate_left3([1, 2, 3]))
