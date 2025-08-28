class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
my_dog = Dog("Buddy", "Golden Retriever", "Golden")

print(f"Dog's Name: {my_dog.name}")
print(f"Dog's Species: {my_dog.species}")
print(f"Dog's Fur Color: {my_dog.fur_color}")
print(f"Dog's Breed: {my_dog.breed}")



#Exp_02:-

class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())