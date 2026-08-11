# CRreate a Factorial function without recursion

# Number will be factorial
factorial_number = 4

starter_numb = 1
calculation = range(starter_numb, factorial_number+1)

for index in calculation:
    starter_numb *= index

print(factorial_number, "!=", starter_numb)
