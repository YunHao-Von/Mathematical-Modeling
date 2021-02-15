import gurobipy as grb
student,chinese,math,english=grb.multidict({
    'student1':[1,2,3],
    'student2':[2,3,4],
    'student3':[3,4,5],
    'student4':[4,5,6]
})
print(student)
print(chinese)
print(math)
print(english)