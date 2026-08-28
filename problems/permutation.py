def permutate(array):
    empty_arr = []

    if len(array) == 0:
        return []
    if len(array) == 1:
        return [array]

    for i in range(len(array)):
        elem = array[i]
        rem = array[:i] + array[i+1:]
        for k in permutate(rem):
            empty_arr.append([elem] + k)
    return empty_arr


arr_1 = []
arr_2 = [5, 6, 7, 8]
print([arr_2], "\n")
print(permutate(arr_2))
