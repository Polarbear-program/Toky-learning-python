# Given an array of ints, return True if 6 appears as either the first
#  or last element in the array. The array will be length 1 or more.
#_____________________________________________#

# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False


def first_last6(nums):
  while nums:
    if nums[0] == 6 or nums[-1] == 6:
      return True
    else:
      break
  return False 

print(first_last6([2,5,6,1]))
print(first_last6([2,5,8,9,6]))