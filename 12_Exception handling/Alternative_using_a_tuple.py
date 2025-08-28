try:
    num=int(input("enter the number!"))
    result=10/num
except (ZeroDivisionError,ValueError) as e:
    print(f"an error occurred: {e}")
