#                                                       (1).list.sort():-
#Exp_01:-

a=(3,5,7,5,76,5,7,5,0)
print(a)
print(type(a))
print(a)
a.sort()
print(a)


#Exp_02:-
name=("suryaa","darshna","harshita","sanju","divyaa","nilam")
print(type(name))
print(name)
name.sort()
print(name)
name.sort(reverse=True)
print(name)


print("\n")

#                                                               (2).reverse():-

#Exp_01:-
a=(3,5,7,5,76,5,7,5,0)
print(a)
print(type(a))
a.reverse()
print(a)

#Exp_02:-
name=("suryaa","darshna","harshita","sanju","divyaa","nilam")
print(name)
name.reverse()
print(name)


print("\n")

#                                                               (3).Index():-

#Exp_01:-
a=(3,5,7,5,76,5,7,5,0)
print(a)
print(type(a))
b=a.index(5)
print(b)
b=a.index(0)
print(b)
b=a.index(7)
print(b)
b=a.index(76)
print(b)

#Exp_02:-
name=("suryaa","darshna","harshita","sanju","divyaa","nilam")
print(name)
c=name.index("suryaa")
print(c)
c=name.index("darshna")
print(c)
c=name.index("harshita")
print(c)
c=name.index("nilam")
print(c)
c=name.index("suryaa")
print(c)
c=name.index("divyaa")
print(c)


#                                                              (4). Count():-

#Exp_01:-

a=(3,5,7,5,76,5,7,5,0,2,6,2,6,4,2,8)
print(a)
print(type(a))
p=a.count(2)
print(p)
print(a.count(7))

#Exp_02:-
name=("suryaa","darshna","harshita","sanju","divyaa","nilam","darshna","divyaa","darshna")
print(type(name))
print(name)
n=name.count("darshna")
print(n)
print(name.count("divyaa"))





print("t")


#                                                        (5).Copy():-

#Exp_01:-

a=(3,5,7,5,76,5,7,5,0)
print(a)
print(type(a))
n=a.copy()
print(n)

print("\n")

#Exp_02:-
name=("suryaa","darshna","harshita","sanju","divyaa","nilam")
print(type(name))
print(name)
c=name.copy()
print(c)
print("\n")

print("\t")

#                                                            (6).insert():-

#Exp_01:-

a=(3,5,7,5,76,5,7,5,0)
print(a)
print(type(a))
a.insert(0,540)
print(a)
a.insert(6,-1)
print(a)

#Exp_02:-
name=("suryaa","darshna","harshita","sanju","divyaa","nilam")
print(type(name))
print(name)
name.insert(5,"falak")
print(name)

#                                                    (7).extend():-

#Exp_01:-

a=(3,5,7,5,76,5,7,5,0)
print(a)
print("\n")
b=[4,7,5,7,9,5,8,0,5,4]
print(b)
print("\n")
a.extend(b)
print(a)

print("\n")
#Exp_02:-
name1=("suryaa","darshna","harshita","sanju","divyaa","nilam")
print(type(name))
print(name1)
name2=('tanwar','bhayal','agarwal','sedariya','mali','rana')
print(name2)
print("\n")
name2.extend(name1)
print(name2)
print(name1)
print("\n")
name1.extend(name2)
print(name1)
print(name2)




print("\n")
#                                        (8).append():-
#Exp_01:-

a=(3,5,7,5,76,5,7,5,0)
print(a)
print(type(a))
a.append(65)
print(a)


#Exp_02:-
name=("suryaa","darshna","harshita","sanju","divyaa","nilam")
print(type(name))
print(name)
name.append("falak")
print(name)