names = ["surya","darshna","sanju","harshita","nilam"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")