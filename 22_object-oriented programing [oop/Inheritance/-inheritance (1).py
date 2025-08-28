class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now....")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        super().speak() # We are using the speak function of the parent class
        print("Woof!")

# a = Animal("Dog")
# a.speak()
d = Dog("Bruno")
d.speak()
# print(d.location)


#Exp_02:-
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"the name of employee:{self.name} is {self.id}")

class programmer(Employee):
    def showLanguage(self):
        print("the defualt Language is python")

class codder(Employee):
    def showCodding(self):
        print("the default codder is java")
                

e1=Employee("suresh kumar",578758) 
e1.showDetails()
e2=programmer("darshna bhayal",65779) 
e2.showDetails()
# e2.showLanguage()      
e3=Employee("sanju ",578587)
e3.showDetails()          
# e3.showCodding() 
        
