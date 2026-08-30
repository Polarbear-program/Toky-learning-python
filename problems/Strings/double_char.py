# Given a string, return a string where for every char in the original, 
# there are two chars.
#______________________#

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    empty_str = ""
    for i in range(0, len(str)):
        empty_str += str[i] + str[i]
    return empty_str

a = "Hello"
print(double_char(a))
