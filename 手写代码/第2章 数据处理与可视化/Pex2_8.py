from numpy import array
x=array([[1,2],[3,4],[5,6]])
print("前两行元素为:\n",x[[0,1]])
print("x[0][0]和x[1][1]分别为：",x[[0,1],[0,1]])
print("以下二种格式相同")
print(x[[0,1]][:,[0,1]])
print(x[0:2,0:2])