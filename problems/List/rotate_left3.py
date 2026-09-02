#Given an array of ints length 3, return an array with the elements 
# "rotated left" so {1, 2, 3} yields {2, 3, 1}.
#__________________________________________________#

# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
    empty_list = []
    empty_list.insert(0, nums[1])
    empty_list.insert(1, nums[2])
    empty_list.insert(2, nums[0])
    return empty_list


print(rotate_left3([1, 2, 3]))
