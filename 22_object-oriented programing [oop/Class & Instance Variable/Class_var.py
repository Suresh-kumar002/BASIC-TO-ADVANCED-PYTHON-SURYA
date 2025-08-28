class Myclass:
    class_var=0
    def __init__(self):
        Myclass.class_var +=1
    def print_class_var(self):
        print(Myclass.class_var)
obj1=Myclass()
obj2=Myclass()
fesr=Myclass()

fesr.print_class_var()
obj1.print_class_var()
obj2.print_class_var()