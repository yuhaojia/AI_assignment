# from digit_classification import digit_clasification
import numpy as np

# c = classifydigit(1)
# print(c.str1)

# a = []
# b1 = [0, 1, 2]
# b2 = [3, 4, 5]
# b3 = [6, 7, 8]
# a.append(b1)
# a.append(b2)
# a.append(b3)
# a = np.asarray(a)
# print(a.shape)

# a = np.arange(500000000)
# b = a[::2]
# np.set_printoptions(threshold='nan')
# # print(b)


# a = [0, 1, 0 ,1 , 0, 2, 0 , 0]
# for index, label in enumerate(a):
# 	if label == 1:
# 		print(index)

# a = np.ones((3, 4), dtype= int)
# a[1][1] += 1
# a[1] = a[1]/0.5
# print(a)
a = np.array([9, 6, 5, 3, 7, 4, 9, 1, 7]).reshape(3,3)
b = np.array([9, 6, 5, 3, 7, 4, 9, 1]).reshape(2,2,2)
# ind = np.argpartition(a, -1)[-1]
# print(ind)

# x = np.array([8, 7, 5, 10])
# a = x[np.argpartition(x, 0)]
# a = np.argpartition(x, 1)
# print(a.shape[0] * a.shape[1], 'dasdsf')

# a = a.flatten()
# ind = np.argpartition(a, -4)[-4:]
# print(ind)


# k = 5
# print(2 % 3)

# print((a==b).all())
# print(1-a)
# b = np.absolute(1-a)
# print(b)

a = 0.1
while a < 1:
	a = a + 0.1
	print(a)
