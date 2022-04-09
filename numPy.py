import numpy as np

# a = np.array([1, 2, 3], dtype= 'float64')
# print(a)
# a = np.arange(1, 5, 0.5)
# print(a)
# print(a.dtype)
# print(type(a))
# print(a.shape)
# print(a.ndim)
# b = np.array([np.arange(2), np.arange(2)])
# print(b)
# print(b.shape)
# print(b.ndim)

# a =np.zeros((5,5),dtype='int32')
# b= np.ones((5,5))
# print(a)
# print(b)
# a= np.empty((4,4))
# print(a)
# print(a[1][1])
#
# a = np.linspace(1,2,10)
# print(a)

# a, b = np.indices((5, 5))
# print(a)
# print(b)
#
# d, e = np.mgrid[0:5, 0:5]
# print(d)
# print(e)
#
#
# f= np.diag([x for x in range(5)],k=-1)
# print(f)
#
# g = np.fromiter(range(5),dtype='int')
# print(g)

marcin = 'Marcin'
# mar = np.frombuffer(marcin, dtype='S3')
# print(mar)
# mar_1 = np.array(list(marcin))
# print(mar_1)
#
# mar_3 = np.fromiter(marcin,dtype='S1')
# mar_4 = np.fromiter(marcin,dtype='U1')
# print(mar_3)
# print(mar_4)

# a= np.ones([2,2])
# b= np.ones([2,2])
#
# c = a + b
#
# print(c)

# a = np.arange(10)
# print(a)
#
# s = slice(2,7,2)
# print(s)
# print(a[s])
#
# a = np.arange(25)
# mat = a.reshape((5,5))
# print(mat)
# print(mat[1:, 1:])
# print(mat[:, 1:2])
# print(mat[2:5, 1:3])

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
b= a[rows,cols]
print(b)



