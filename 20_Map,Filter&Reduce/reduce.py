#Exp_01:-

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
#         [3, 3, 4, 5, 6]
#         [6, 4, 5, 6]
#         [10, 5, 6]
#         [15, 6]
#         [21]

def sum(a, b):
    return a + b 

c = reduce(sum, numbers)
print(c)

#Initializer_Reduce

e_l_sum=reduce(lambda x,y:x+y,[],0)
print(e_l_sum)

#Equivalent_Reduces
number=[1,2,3,86,86558]
total=0
for x in number:
    total=x
print(total)