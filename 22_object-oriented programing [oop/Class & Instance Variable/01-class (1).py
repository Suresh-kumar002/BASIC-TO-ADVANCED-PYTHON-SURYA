# Class: Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, father's name etc

# Object: Specific instance created from the template (class.). Eg. Form which contains the data for John Doe

#Exp_01:-

class Employee:
    company = "HP"

    def get_salary(self): # self is important here because self is a way to reference the object of the class which is being created
        return 34000


e1 = Employee() # An Object of class Employee is created here
print(e1.get_salary()) # Employee e's get salary method is called
print(e1.company)

e2 = Employee()
print(e2.get_salary())
print(e2.company)

#Exp_02:-

class person:
    name="suryaa"
    occupation="software Engineer"
    networth=10
    def info(self):
        print(f"{self.name} is {self.occupation}")


a=person()
b=person()
c=person()
d=person()
e=person()
f=person()

a.name="Darshna"
a.occupation="RAS"

b.name="Harshita"
b.occupation="web developer"

c.name="sanju"
c.occupation="DevOPs"

d.name="divya"
d.occupation="App developer"

e.name="nilam"
e.occupation="android developer"

a.info()
b.info()
c.info()
d.info()
e.info()
f.info()