# Creating a function for selection sort
def selec_sor(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        min_value = arr.pop(min_idx)
        arr.insert(i, min_value)

# Improve version of selec sort
def selec(arr):
    m = len(arr)
    for i in range(m-1):
        min_idx = i
        for j in range(i+1, m):
            if arr[j] < arr[min_idx]:
                arr[j], arr[min_idx] = arr[min_idx], arr[j]


arr = [5, 3, 1, 6, 12, 25, 32, 65, 75,
       23, 21, 12, 15, 11, 90, 98, 85, 31, 7, 2]
arr2 = arr
selec(arr2)

print(arr2)
