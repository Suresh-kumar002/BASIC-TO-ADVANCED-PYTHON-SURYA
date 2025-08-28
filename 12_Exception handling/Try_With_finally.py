# def fun():
#  try:
#   a=[1,2,34,4,34,4]
#   print(a(a))
#   return 1
#  except:
#   print("some error occurred")
#   return 0 
#  finally:
#   print("i am always executed")
# x=fun()
# print(x)
     


#exp_02:-

def fun():
 try:
   s = [1,3,5,6,4,65,5]
   i = int(input("Enter the index: "))
   print(s[i])
   return 1
 except:
   print("some error occured")
   return 0
 finally:
  print("i am always executed")
  # print("i an always executed")

x=fun() 
print(x) 

