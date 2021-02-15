import numpy as np
import numpy.linalg as LA
A=np.arange(1,17).reshape(4,4)
B=np.eye(4,4)
print("A的行列式为",LA.det(A))
print("A的秩",LA.matrix_rank(A))
print("A的转置为",A.transpose())
print("A的逆矩阵为：",LA.inv(A+10*B))
print("A的平方为：\n",A.dot(A))
print("A，B的乘积为：",A.dot(B))
print("横联矩阵为",np.c_[A,B])
print("纵联矩阵为：",np.r_[A,B])
print("A1为",A[0:2,0:2])
