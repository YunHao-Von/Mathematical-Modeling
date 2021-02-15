import sympy as sp
A=sp.Matrix([
    [1,-5,2,-3],
    [5,3,6,-1],
    [2,4,2,1]
])
print(A.nullspace())