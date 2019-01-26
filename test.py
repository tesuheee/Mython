import numpy as np
a = np.array([0,1,2,3,4,5])
# print a
b = a.reshape((3,2))
c = a.reshape((2,3))
# print b
# print b.ndim
# print b.shape
# a[4] = 10
# print a
# b[1][0] = 77
# print b
# print a
# print a*2
# print a[a**2>4] 
# a[a>4] = 4
print np.dot(c, b)