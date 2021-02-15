from numpy import arange,cross,inner
from numpy.linalg import norm
a=arange(1,4);b=arange(4,7)
print("a的二范数为：",norm(a))
print("a点乘b为：",a.dot(b))
print("a,b的内积为：",inner(a,b))
print("a叉乘b为:",cross(a,b))
