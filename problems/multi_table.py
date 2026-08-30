# input: 5
# expected: 5 * 1 = 5, 5 * 2 = 10.... 5 * 10 = 50
def multiplication_table(number: int):
    # Using the for loop statement
    range_number = range(1, 10+1)
    for i in range_number:
        print(f"{number} * {i} =", number * i)

    # Using the while loop statement    
    """i = 1
        while number:
            print(f"{number} * {i} =", number * i)
            i += 1
            if i == 11:
                break"""


num_input = int(input())
result = multiplication_table(num_input)
