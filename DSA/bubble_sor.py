def bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped = False

        for j in range(len(arr)-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [2, 4, 1, 7, 13, 6, 3, 9, 11, 5]
bubble_s = bubble_sort(arr)

print(arr)
