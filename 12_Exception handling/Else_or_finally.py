try:
    file=open("test.txt","r")
    content=file.read()
except FileNotFoundError:
    print("file not found")
else:
    print("file read successfully")
    print(f"file content.\n{content}")
finally:
    file.close()        
