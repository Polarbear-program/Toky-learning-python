# counting even numbers

# Create even_numbers integer
even_numbers = 0

# Create a range from 2 -> 22
numbers = range(2, 22+1, 2)

# Print out even numbers using list()
print("The even numbers in the list is:", list(numbers))

print("The even number is:", end=" ")
# A loop counting from 2 -> 20
for even_numbers in numbers:
    print(even_numbers, end= " ")

"""odd_number = range(1, 19, 2)
print(len(odd_number))"""
