# Given 2 ints, a and b, return their sum. However, 
# sums in the range 10..19 inclusive, are forbidden, 
# so in that case just return 20.
#__________________________________#

# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21

def sorta_sum(a, b):
  if 10 <= (a + b) < 20:
    return 20
  else:
    return a + b

print(sorta_sum(2,6))
print(sorta_sum(5, 7))
print(sorta_sum(5,5))
print(sorta_sum(10,23))