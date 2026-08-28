# a quick sort example using define function and loop

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low_value, high_value):
    # make a pivot, every time value of arr see a high value, it will become the pivot
    pivot = arr[high_value] 

    # Index start at the lowest value and then moving on
    i = low_value - 1

    for j in range(low_value, high_value):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # move pivot after smaller elements
    # return its position
    swap(arr, i + 1, high_value)
    return i + 1

# Quicksort function implementation
def quickSort(arr, low_value, high_value):
    if low_value < high_value:

        # pi is the partition return index of pivot
        pi = partition(arr, low_value, high_value)

        #recurcsion call for smaller elements
        # and greater or equals elements
        quickSort(arr, low_value, pi - 1)
        quickSort(arr, pi + 1, high_value)

if __name__ == "__main__":
    arr = [54, 12, 42, 23, 11, 64, 22, 34, 67, 52, 13, 97, 76, 63, 72, 17]
    n = len(arr)

    quickSort(arr, 0, n - 1)

    for val in arr:
        print(val, end= " ")
    print('\n')

    test = [1,2,3]
    print(len(test))