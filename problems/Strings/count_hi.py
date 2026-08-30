# Return the number of times that the string "hi" appears anywhere 
# in the given string.
#____________________________________________#

# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
  count = 0
  for search in range(len(str)-1):
    if str[search] == "h" and str[search + 1] == "i":
      count +=1
  return count