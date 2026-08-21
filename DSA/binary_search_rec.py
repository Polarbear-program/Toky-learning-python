def binarySearch(arr, left, right, target):
    while right >= left:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            return binarySearch(arr, left, mid - 1, target)
        elif arr[mid] < target:
            return binarySearch(arr, mid + 1, right, target)
        else:
            return mid
    return -1

arr = [1, 3, 4, 5, 6, 7, 8, 10, 12, 23, 34, 35, 45, 56, 65, 76, 77, 78, 98, 121]
target = 78
result = binarySearch(arr, 0, len(arr)-1, target)

if result != -1:
    print("The target position at the index:", result)
else:
    print("No target's position found in the array")