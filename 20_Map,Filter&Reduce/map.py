numbers = [1, 2, 3, 45, 4, 21]

# def square(x):
#     return x * x 


new = list(map(lambda x: x*x, numbers))
print(new)

#Exp_02:-


def cube(x):
    return x * x * x
print(cube(2))

s=[2,3,5,67,5,7,8,76,7,7]

news=list(map(cube,s))
print(news)

#uper wale same ko lambda function me badala h

# def cube(x):
#     return x * x * x
# print(cube(2))

s=[2,3,5,67,5,7,8,76,7,7]

news=list(map(lambda x: x*x*x,s))
print(news)
