# Create a list with 10 empty elements
# Each of these elements are bucket in *hash*
list = [None, None, None, None, None,
        None, None, None, None, None]


# In this function we will make each character into Unicode number
# And use modulo 10 operator to get index numbers 0-9
def hash_function(list):
    sum_of_char = 0

    for char in list:
        sum_of_char += ord(char)
        print(ord(char))

        return sum_of_char % 10

print("Bob has hash code:", hash_function('Bob'))