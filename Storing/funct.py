# Creating a function
def my_function():
    print("Hello new function")


def my_Sum(a, b):
    result = 0
    result = a + b
    print(result)


def greet(name, birthday_Today):
    if birthday_Today:
        msg = "Happy birthday " + name
    else:
        msg = "Hey " + name
    return msg


def f(r):
    return 3.14 * r**2


def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myFun(2, 45)
