class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
      return f"Person({self.name}, {self.age})" # User-friendly
    def __repr__(self):
      return f"Person(name='{self.name}', age={self.age})" # Unambiguous, for debugging
p = Person("surya",18)
print(str(p)) # Person(surya,18)
print(repr(p)) # Person(name='surya', age=18)
print(p) # Person(surya, 18)  # print() uses __str__ if 