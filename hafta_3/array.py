import numpy as np

# arr= np.array([[1,2,3], [4,5,6]])
# print(arr)
# print(arr[0][2])

# arr2= np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
# print(arr2)

arr= np.array([[1,2,3], [4,5,6]])

for x in arr:
    for y in x:
        print(y)