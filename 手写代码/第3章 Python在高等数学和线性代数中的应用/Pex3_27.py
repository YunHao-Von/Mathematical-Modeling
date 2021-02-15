import numpy as np
import sympy as sp
A = sp.Matrix(np.arange(1,17).reshape(4,4))
B = sp.eye(4)
print("A的行列式", sp.det(A))
print("A的秩为", A.rank())
print("A的转置矩阵为",A.transpose())
print("所求的逆矩阵为",(A+10*B).inv())
print("A的平方为", A**2)
print("A，B的乘积为",A*B)
print("横联矩阵为",A.row_join(B))
print("纵联矩阵为",A.col_join(B))
print("A1为",A[0:2,0:2])
print("A2为",A.copy().row_del(3))