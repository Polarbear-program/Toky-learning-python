def check_number(number):
    if number % 2 == 1:
        return "This is an odd number"
    elif number % 2 == 0:
        return "This is an even number"

print("Type in any integer number you want: ", end="")
number = int(input())

print(check_number(number))
