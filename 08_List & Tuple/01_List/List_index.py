  #                                           #Positive Index:-

#Exp_01:-
marks=[2,5,7,74,4,8,89]
print(marks[0])
print(marks[1])
print(marks[4])

 #                                            #Negative Index:-
#Exp_02:-
marks=[2,5,7,74,4,8,89]
print(marks[-3])
print(marks[-1])
print(marks[-4])



#Exp:- Check wether an item in persent in the list?

marks=[2,5,7,74,4,8,89,"surya","darshna",True]
print(marks[5])
if "darshna" in marks:
    print("yes")
else:
    ("no")   
if "mukesh" in marks:
    print("yes")
else:
    print("no")         



name = "Harry" 

# name = "H   a   r  r   y"
#         0   1   2  3   4
#        -5  -4  -3 -2  -1

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4]) # name[-4+5] name[1]
print(name[-5])   