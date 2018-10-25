import numpy as np

# Generate some random data
data = np.random.randn(2,3)
print('data: \n',data)
print('data * 10: \n', data * 10)
print('data + data: \n', data + data)
print('data shape: \n', data.shape)
print('data dtype: \n', data.dtype)

# Create array
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.dtype)
print(np.zeros(10))
print(np.zeros((3,6)))
print(np.empty((2,3,2)))
print(np.arange(15))

# Change the dtype of ndarray
arr1 = np.array([1,2,3],dtype = np.float64)
arr2 = np.array([1,2,3],dtype = np.int32)
print(arr1.dtype)
print(arr2.dtype)

arr = np.array([1,2,3,4,5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
print(arr.astype(np.int32))

numeric_strings = np.array(['1.25','-9.6','42'],dtype = np.string_)
print(numeric_strings.astype(np.float64))

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype = np.float64)
print(int_array.astype(calibers.dtype))

empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)
print(empty_uint32.dtype)

# Operation on ndarray
arr = np.array([[1.,2.,3.],[4.,5.,6.]])
print(arr)
print(arr * arr)
print(arr - arr)
print(1/arr)
print(arr ** 0.5)
arr2 = np.array([[0.,4.,1.],[7.,2.,12.]])
print(arr2)
print(arr2 > arr)

# Broadcasting
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])
print(a)
print(b)
print(a+b)

# Indexing of ndarray
arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8]=12
print(arr)
arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr)
arr_slice[:] = 64
print(arr)
arr_slice = arr[5:8].copy()
print(arr_slice)
arr_slice[1] = 12345
print(arr)
arr_slice[:] = 64
print(arr)
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[2])
print(arr2d[0][2])
print(arr2d[0,2])
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
old_values = arr3d[0].copy()    # backup arr3d[0]
arr3d[0] = 42
print(arr3d)
print('==========分割线==========')
arr3d[0] = old_values
print(arr3d)
print(arr3d[1,0])
print('==========分割线==========')
x = arr3d[1]
print(x)
print(x[0])
