import numpy as np
marks=[10,20,30,40,50,60]
print(marks)
new_marks=[]
for mark in marks:
    new_marks.append(mark+5)
print(new_marks)    

marks=np.array([10,20,30,40,50,60])
print(marks)

marks_array=np.array([10,20,30,40,50,60])
print(marks_array+5)
print(marks_array*6)