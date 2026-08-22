# Create an empty array
arr = []
sum = 0

# Input the given number to print out the list
print("Enter the amount of number you want: ", end="")
num_input = int(input())

# For number in a range start from 0 to the given number*5, step 5
for numbers in range(0, num_input*5, 5):
    # Sum start with 0
    if num_input > 0:
        sum += numbers
        arr.append(numbers)

print(list(arr))
print("The sum of list given by your number: " + str(sum))