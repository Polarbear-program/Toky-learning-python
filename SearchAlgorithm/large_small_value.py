# A function where array given will find the largest or lowest value
def largestValue(arr):
    large = arr[0]
    small = arr[0]
    for index in range(0, len(arr)):
        if arr[index] > large:
            large = arr[index]
        elif arr[index] < small:
            small = arr[index]
    return large, small

# even-odd function to find if the number given are divisible by 2
def evenOdd(n):
    if (n % 2 == 0):
        return "Even"
    else:
        return "Odd"


arr = [-200, -100, -34, -85, -22, -10, -5]
arr.insert(3, -40)
arr.extend([-3, -1])
result = largestValue(arr)

print("The largest and smallest value found:",result)
print(arr)
