#Exp_01:-
a=[1,2,3]
b=[1,2,3]

print(a is b) # exact location of object in memory
print(a==b)  #value

print('\n')
#Exp_02:-

a=2 
b=2

print(a is b)# constant value is True
print(a==b)# constant value True

print("\n")
#Exp_03:-

a="surya"
b="surya"

print(a is b)
print(a==b)

print("\n")
#Exp_04:-

a=(1,2)
b=(1,2)
print(a is b)
print(a==b)

print('\n')
#Exp_05:-

a=None 
b=None
print(a is b)
print(a is None)
print(a==b)