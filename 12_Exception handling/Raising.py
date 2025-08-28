# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# if b == 0:
#     raise ValueError("Please dont divide by 0")

# print(f"The division is {a / b}")

# def check_age(age):
#     if age < 18:
#         raise ValueError("age must be 18 or older!")
#     return"access granted"
# try:
#     print(check_age(20))
#     print(check_age(16))
# except ValueError as e:
#     print(f"error:{e}")

a=int(input("enter any value betwen 5 and 9"))
if (a<5 or a>9):
    raise ValueError("value should be between 5 and 9")