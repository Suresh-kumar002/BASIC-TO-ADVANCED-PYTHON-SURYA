class MathUnit:
    @staticmethod
    def add(a,b):
        return a+b
print(MathUnit.add(46,57))
#can also be called on an instance
s=MathUnit()
print(s.add(578578,579759))
