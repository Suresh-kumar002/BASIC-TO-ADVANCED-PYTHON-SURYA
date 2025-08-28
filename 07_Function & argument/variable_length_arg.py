# TYPE:- 
        #(1) Tuple    (2).Dictionry

#(1).Tuple:-
#Exp_01:-

def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    print("average is:",sum/len(number))
average(5,9,1)    


#Exp_02:-
def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    print("average is:",sum)
average(5,9,1)    


#Exp_03:-

def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    print("average is:",sum*5%2)
average(5,9,1)    



#Exp_)4:-
def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    print("average is:",sum-15)
average(5,9,1)    

#Exp_05:-
def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    print("average is:",sum*len(number))
average(5,9,1)    

#Exp_06:-
def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    print("average is:",sum//len(number))
average(5,9,1)

#Exp_07:-
def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    print("average is:",sum+len(number)-len(number)*len(number)/len(number)//len(number)%len(number))
average(5,9,1)   


#Exp_08:-
def name(*name):
    print("hello",name[0],name[1],name[2])
name("surya","tanwer","megh")    




#(2).Dictionary:-

#Exp_01:-
def name(**name):
    print(type(name))
    print("hello",name["fname"],name["mname"],name["lname"])
name(mname="surya",lname="tanwer",fname="meg")


        
