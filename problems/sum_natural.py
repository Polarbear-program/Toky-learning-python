def sum_of_natural(number_input: int):
    for i in range(1,number_input):
        number_input += i
    return number_input
        


print("Please enter any positive integer:", end="")
num_input = int(input())

print(sum_of_natural(num_input))
