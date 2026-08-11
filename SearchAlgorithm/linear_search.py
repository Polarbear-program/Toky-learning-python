
arr = [2, 4, 6, 1, 8, 24, 23, 12, 25, 9]

high_val = 0

for index in range(0, len(arr)):
    if high_val < arr[index]:
        high_val = arr[index]

print(high_val)