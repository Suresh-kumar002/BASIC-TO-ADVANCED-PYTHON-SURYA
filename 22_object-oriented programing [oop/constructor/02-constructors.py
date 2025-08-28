#Exp_01:-


import abc


class Employee: 

    def __init__(self, salary, name, bond):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")
    

e1 = Employee(34000, "suresh kumar", 4)
# print(e1.get_salary())
e1.get_info()

#Exp_02:-
class person:

    def __init__(self,name,occ):
        print("hey i am a person")
        self.name=name
        self.occ=occ 
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("surya","Software Engineer")
b=person("sanju","web devloper")
a.info()
b.info()            
