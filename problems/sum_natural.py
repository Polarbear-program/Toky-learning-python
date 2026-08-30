def sum_of_natural(number_input: int):
    for i in range(1, number_input):

        # Number input will summarize from 1 to itself
        result = num_input + i
        print(i, "+", end=" ")
        i += 1

    # After the loop end, close it with the last index of element and "="
    print(i, "= ", end="")
    return result


print("Please enter any positive integer:", end="")
num_input = int(input())

print(sum_of_natural(num_input))
