import sympy as sp
A=sp.Matrix([
    [1,1,-3,-1],
    [3,-1,-3,4],
    [1,5,-9,-8]
])
b=sp.Matrix([1,4,0])
b.transpose()
C=A.row_join(b)
print(C.rref())