class MyCallableClass:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value * x

# Create an instance of the class
my_object = MyCallableClass(10)

# Call the instance like a function
result = my_object(5)
print(result)