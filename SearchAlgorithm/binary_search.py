def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


# Array must be sorted before using binary search
arr = [2, 4, 6, 7, 8, 12, 23, 45, 59]
# target will be set
target = 59

result = binary_search(arr, target)
if result != -1:
    print("The target is present at index: ", result)
else:
    print("The target is not present in array")
