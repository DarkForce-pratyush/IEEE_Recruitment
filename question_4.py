import numpy as np

matrix_5x5=np.random.randint(1,101,size=(5,5))

middle_3x3 = matrix_5x5[1:4, 1:4]
print("Middle 3x3 matrix:")
print(middle_3x3)

first_row = middle_3x3[0, :] #extracting the first row of the 3x3 matrix
last_column = middle_3x3[:, -1] #extracting the last column of 3x3 matrix

dot_product = np.dot(first_row, last_column)
print("Dot product of the first row and last column:")
print(dot_product)