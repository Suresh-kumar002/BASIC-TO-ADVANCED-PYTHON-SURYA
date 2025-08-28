class InvalidAgeError(Exception):
        '''custom exception for invalid age'''
        def __init__(self, message="age must be 18 or older!"): # Corrected __int__ to __init__
            self.message = message
            super().__init__(self,message)
def verify_age(age): # Corrected 'varify' to 'verify_age'
            if age < 18:
             raise InvalidAgeError()
            return "welcome"
try:
    print(verify_age(16))
except InvalidAgeError as e:
    print(f"Error: {e}")