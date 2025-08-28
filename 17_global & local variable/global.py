global_var="i am a global"
def print_global():
    print(global_var)
def modify_global():
    global global_var
    global_v="i am modify global"
print_global()
modify_global()
print_global()        

#Exp_02:-

def sum (a,b):
    print("hey i am summing")
    c=a+b
    global z
    z=0
    return c
z=3
print(sum(3,12))
print(z)    