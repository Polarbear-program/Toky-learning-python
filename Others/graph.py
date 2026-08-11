import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
arr2 = arr[2:, ::2]

arr3 = arr[[1, 1, 0, 3], [2, 1, 0, 1]]
print(arr3)

#Matrix sum of array pos 0 and 1
arr_add = np.add(arr[0], arr[1])
print(arr_add)

#dtype used to know the exact layout, type of data stored within memory
print(arr.dtype)


