class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
p=person("surya",18)
print(p.__dict__)
