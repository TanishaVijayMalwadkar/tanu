import numpy as np
arr1=np.array([1,2,3,4,5])

#Number of dimension
print("Array of dimension:",arr1.ndim)
#Shape of the array
print("Array of shape:",arr1.shape)
#Number of ele in the array
print("Array of size:",arr1.size)
#Date type
print("Array of Datatype:",arr1.dtype)
#item size
print("item size:",arr1.itemsize)


#array of zero
zeros=np.zeros((3,3))
print(zeros)
#array of one
ones=np.ones((2,4))
print(ones)
#array of identity
identity=np.eye(3)
print(identity)
#array of random
random=np.random.random((2,2))
print(random)
print("Sum of array:",arr1.sum())
print("Mean of array:",arr1.mean())
print("Min of array:",arr1.min())
print("Max of array:",arr1.max())
print("Standard Deviation:",arr1.std())
print("Variance:",arr1.var())
print("Cumulative Sum:",arr1.cumsum())
print("Cumulativ Product:",arr1.cumprod())

arr2=np.array([[1,2,3],[4,5,6]])
#Number of dimension
print(arr2.ndim)
#Shape of the array
print(arr2.shape)
#Number of ele in the array
print(arr2.size)
#Date type
print(arr2.dtype)

#crating array with range of value
range_arr=np.arange(1,10)
print("Range array:",range_arr)

#crating an array with linearly spaced values
linespace_arr=np.linspace(0,1,5)
print("linearly:",linespace_arr)
#ItemSize
#print("Item Size(bytes):",arr1.itemsize())
#Total bytes
#print("Total bytes:",arr1.nbytes())

copy_arr=arr1.copy()
view_arr=arr1.view()
print("original array:",arr1)
print("Copied array:",copy_arr)
print("viewd array:",view_arr)
