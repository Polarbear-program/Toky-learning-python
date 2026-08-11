def factorial(n):
    ans = 1
    i = 2
    
    #Calculating factorial of number
    while (i <= n):
        ans *= i
        i += 1
    return ans

if __name__ == "__main__":
    num = 5
    print(factorial(num))