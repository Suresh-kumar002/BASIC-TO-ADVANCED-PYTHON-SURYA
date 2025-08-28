#Particular range 

#Exp_01:-

marks=[2,5,7,74,4,8,89]
print(type(marks))
print(marks)
print(marks[1:-1])
print(marks[2:3])
print(marks[:])
print(marks[2:])
print(marks[:4])
print(marks[-4:])
print(marks[:-3])
print(marks[0:0])


#Exp_02:-

animal=["cat","cow","elephent","mouse","donkey","goat","house"]
print(animal)
print(type(animal))
print(animal[:])
print(animal[1:-1])
print(animal[2:3])
print(animal[:])
print(animal[2:])
print(animal[:4])
print(animal[-4:])
print(animal[:-3])
print(animal[0:0])


#jump & consecutive value within a given range:-

#exp_01:-
marks=[2,5,7,74,4,8,89]
print(marks)
print(type(marks))
print(marks[::])
print(marks[2:0:8])
print(marks[:1:3])
print(marks[4::3])
print(marks[:5:])
print(marks[3::])
print(marks[2:3:])

#Exp_02:-
#Accepts items with the small letter " koi bhi ho" in the new list generate 

animal=["cat","cow","elephent","mouse","donkey","goat","house"]
animalwith_0=[item for item in animal if "o" in item]
print(animalwith_0)


#Exp_03:-
#Accepts item which have more than "ek perticular number"letter

animal=["cat","cow","elephent","mouse","donkey","goat","house"]
animalwith_o=[item for item in animal if (len(item)>4)]
print(animalwith_o)

