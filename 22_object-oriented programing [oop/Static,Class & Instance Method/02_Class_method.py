class Employee:
    company="apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls,newCompany):
        cls.company=newCompany

e1=Employee()
e1.name="suryaa"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company) 

#Exp_02:-

class Animal:
    species = "Mammal" # Class attribute
    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species  # Modifies class attribute
    @classmethod
    def get_species(cls):
     return cls.species
print(Animal.get_species()) # Mammal
Animal.set_species("Reptile")
print(Animal.get_species()) # Reptile
 # You can also call class methods on instances, but it's less common:
a = Animal()
print(a.get_species())# Reptile
