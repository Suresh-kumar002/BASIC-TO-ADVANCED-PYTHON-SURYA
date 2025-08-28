class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split(" ") 
        return l[0]
    
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}" 
        self.name = new_name

e = Employee("Suryaa Kumar", 34555)
# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

print(e.first_name)
e.first_name = "Suresh"
print(e.name)

print('\n')

#                                                              Exp_02:-

class MyClass:
    def __init__(self, value):
        self._value = value

    @property  # Getter:- Used to retrieve or "get" the value of a class attribute.
    def value(self):
        return self._value

    @value.setter  # Setter:- Used to modify or "set" the value of a class attribute.
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            print("Value cannot be negative.")

# Usage:
obj = MyClass(10)
print(obj.value)  # Access like an attribute (getter) - Output: 10
obj.value = 20    # Assign like an attribute (setter)
print(obj.value)  # Output: 20
obj.value = -5    # Output: Value cannot be negative.