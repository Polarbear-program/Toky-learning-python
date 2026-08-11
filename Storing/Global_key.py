# Assign my_Var first, but not recall it
my_Var = "This happen later"

# Assign my_Var within def function


def my_fun():
    my_Var = "This happen first"
    print(my_Var)


# my_Var within my_fun() is appear fun then 1st my_Var appear later
my_fun()


def my_fun2():
    global x
    x = "is widely accepted"

#recall my_fun2() to make x appear
my_fun2()
print(my_Var, x)
