from sympy import Matrix, diag
A=Matrix([
    [0,-2,2],
    [-2,-3,4],
    [2,4,-3]
])
if A.is_diagonalizable():print("A的对角矩阵为:\n",A.diagonalize())
else: print("A不能对角化")