# even numbers
"""numbers_a = 2, 4, 6, 8, 10
# odd numbers
numbers_b = 1, 3, 5, 7, 9
print(numbers_b, numbers_a)
print(type(numbers_a))
print(numbers_a.index)"""

"""for x in numbers_a:
    for y in numbers_b:
        y = numbers_a - numbers_b
        print(y)"""


# make a list
arr = [12, 34, 53, 22, 13, 32, 35, 64, 75, 54, 67]
# print all value in arr
print("The value of array:", arr)

high_value = arr[0]

for number_arr in arr:
    if high_value < number_arr:
        high_value = number_arr

print("The highest value in array is:", high_value)

