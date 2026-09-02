# Given 2 arrays of ints, a and b, return True if they have the same first
#  element or they have the same last element. 
# Both arrays will be length 1 or more.
#______________________________________________#

# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end(a, b):
  length_a = len(a)
  length_b = len(b)
  return ((length_a > 0 and length_b > 0) 
          and a[length_a-1] == b[length_b-1] 
          or a[0] == b[0])

print(common_end([1,2,3],[1]))
