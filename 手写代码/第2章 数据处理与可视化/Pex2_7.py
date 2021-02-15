from numpy import array,nan,isnan
a=array([[1,nan,2],[4,nan,3]])
print(a)
b=a[~isnan(a)]
print(b)
print(b[b>2])
print(b>2)
print(isnan(a))
print(~isnan(a))