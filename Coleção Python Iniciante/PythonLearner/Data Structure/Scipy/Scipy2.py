from scipy import linalg
import numpy as np
a = np.array([[1,3,5], [2,5,1], [2,3,8]])
b = np.array([10,8,3])
print(a)
print(b)
x = linalg.solve(a,b)
print(x)
A = np.array([[1,2],[3,4]])
print(A)
print(linalg.det(A))
A = np.array([[3,4], [7,8]])
eigenvalue, eigenvector = linalg.eig(A)
print(eigenvalue)
print(eigenvector)
