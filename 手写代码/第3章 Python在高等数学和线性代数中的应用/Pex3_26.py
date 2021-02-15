import sympy as sp
A = sp.Matrix([[1],[2],[3]])
B = sp.Matrix([[4],[5],[6]])
print("A的模长为：",A.norm())
print("A的模长的浮点数为，", A.norm().evalf())
print(A.T)
print(A.dot(B))
print(A.cross(B))