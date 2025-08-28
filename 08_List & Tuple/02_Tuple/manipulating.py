a=(1,3,5,6,4,56,5,44,5,5,55,5)
b=list(a)
b.append(5)
b.pop(1)
b[4]=6456
a=tuple(b)
print(a)
