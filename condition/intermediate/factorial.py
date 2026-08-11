# Create a factorial function without using recursion

factorial_number = 5
factorial_base = 1

for i in range(factorial_base, factorial_number+1):
    factorial_base *= i

print(str(factorial_number) + "!= " + str(factorial_base))