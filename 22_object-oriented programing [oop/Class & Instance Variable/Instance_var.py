class Myclass:
    company="aus" #class attribute
    def __init__(self,name):
       
        self.name=name
       
    def print_name(self):
        print(self.name)

obj1=Myclass("suresh")
obj2=Myclass("sanju")

obj1.print_name()
obj2.print_name()

    

