def quickSort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()

    item_Greater = []
    item_Lower = []

    for item in array:
        if item > pivot:
            item_Greater.append(item)
            
        else:
            item_Lower.append(item)
    return quickSort(item_Lower) + [pivot] + quickSort(item_Greater)


unSort_array = [12, 42, 75, 85, 33, 1, 5, 4, 8, 67]
print(unSort_array)

print(quickSort(unSort_array))