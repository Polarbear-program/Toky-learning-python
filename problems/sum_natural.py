def sum_of_natural(number_input: int):
    if number_input == 1:
        return 1

    for i in range(1, number_input):

        # Number input will summarize from 1 to itself
        number_input += i
        print(i, "+", end=" ")
        i += 1

    # After the loop end, close it with the last index of element and "="
    print(i, "= ", end="")
    return number_input


def recursion_sum(number_input: int):
    if number_input == 1:
        return 1
    else:
        return number_input + recursion_sum(number_input-1)


print("Please enter any positive integer:", end="")
num_input = int(input())

print(recursion_sum(num_input))
