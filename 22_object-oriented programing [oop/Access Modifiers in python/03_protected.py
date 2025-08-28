class student:
    def __init__(self):
     self._name="surya"
    def _funname(self): #protected method
       return"code with suyraa"
class subject(student): #inherited class
   pass
obj1=student()
obj1=subject()
obj2=subject()
obj2=student()

#calling by object of student class
print(obj1._name)
print(obj1._funname())

#calling by object of subject class
print(obj2._name)
print(obj2._funname())

