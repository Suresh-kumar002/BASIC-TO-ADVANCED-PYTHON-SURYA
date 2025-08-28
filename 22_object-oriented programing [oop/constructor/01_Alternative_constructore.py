class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,data):
        name,age=data.split("-") #("_"),("-")
        return cls (name,int(age))    
p= person.from_string("surya-18")
print(p.name,p.age)