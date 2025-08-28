a= ['apple','banana','mango']
for index,a in enumerate (a):
    print(f"{index+1}:{a}")


#exp_02:-
marks=[12,34,5,4,6,34,6,4]
for index , marks in enumerate(marks,start =1):
   print(marks)
   if(index==3):
    print("surya,awesome!")    