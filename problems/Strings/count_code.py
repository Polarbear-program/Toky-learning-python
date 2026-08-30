# Return the number of times that the string "code" appears anywhere 
# in the given string, except we'll accept any letter for the 'd', 
# so "cope" and "cooe" count.
#_______________________________#

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
    count = 0
    for search in range(len(str)):
         if str[search:search+2] == 'co' and str[search+3:search+4] == 'e':
            count += 1
    return count

string = "codecobecodecobe"
print(count_code(string))
