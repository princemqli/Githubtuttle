#var 
# name = "Prince Mali" #"string"
# age = 19
# price = 38.6

# print("my name is : ", name)
# print("my age is :", age)

# age2=age
# print(age2)


# # data type 
# #.integers
# #.string
# #.float
# #.boolen
# #.None
# print(type(name))
# print(type(age))
# print(type(price))


# name1 ="sk"
# name2 ='sk'
# name3 = '''sk'''

# print(name1)
# print(name2)
# print(name3)

# age=19
# old=True
# a=None
# print(type(age))
# print(type(old))
# print(type(None))

# # sum
# a=1000
# b=2000
# sum = a - b
# print(sum)

# #comments in python
# #single line comment
# print("hello world"), 

# #multiline comment
# print("""my self Prince mali""")

# #Types of Operators
# # An opertor is a symbol that perfoms a certain operation between operands.
# # .Arithmetic Operators(+,-,*,/,%,**)
# a=4
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)#modules

# print(a**b)#power star
# print(a//b)#floor divison

# # .Relational/comparison Operators(==,!=,>,< , >= ,<=)
# a=50
# b=30
# print(a==b)#false
# print(a !=b)#True
# print(a >=b)#True
# print(a > b)#True
# print(a <= b)#Fasle
# print(a < b)#False

# # Assignment Operators(=,+=,-=.*=,/=,%=.**=)
# a=10
# a=a+10
# print("a :",a)
# a=10
# a/=10
# print("a :", a)

# # Logical Operators(not,and ,or)
# logical operator in pyhton are used to combaind multiple and condation and return boolen reslut 
# a=50
# b=30
# print(not False)
# print(not (a > b))


# val1=False
# vale2=False
# print("AND operator", val1 and val2)

# print("OR operator:",(a == b) or (a > b))


# # Type Conversion
# a=float("5")
# b=5.6


# print(type(a))
# print(a+b)

# a=3.14
# a=str(a)

# print(type(a))

# inputinPython
# input()statement is used to accept values (using keybord)From user
# input() #reslut for input()is always a str
# int(input()) #int
# pfloat(input) #float

# input("enter your name:")
# name = input("enter your age:")
# print("you entered", name)

# int("5")
# val=float(input("enter some value: "))
# print(type(val), val)

# name = input("enter name:")
# age = int(input("enter age: "))
# marks=float(input("enter marks:"))

# print("welcome",name)
# print("age =",age)
# print("marks =",marks)

# write a program to input 2 number & print their sum
# fisrt=int(input("enter the fisrt:"))
# second=int(input("enter the second:"))

# print("sum=", fisrt + second)

# write a program to iput side of square & print its area.
# side= float(input("enter square side : "))
# print("area =",side ** 2)

# a= float(input("enter fisrt : "))
# b= float(input("enter second : "))

# print("avg =",(a+b)/2)

# a=int(input("enter fisrt : "))
# b=int(input("enter second : "))

# print(a>=b)

# string
# str1= "This is a string.\t we are creating it in python."
# print(str1)

# #concatenation
# str1="Prince"
# str2="mali"
# print(str1+str2)

# # Indexing
# # str="Prince mali"
# # print(str[4])
# # Slicing
# str="Apna college"
# print(str[-2])

# StringFunctions
# # str.endswith("er.")
# str="my self prince mali stduying for pyhton fron apna college"
# print(str.endswith("ege"))
# # str.capitaliz()
# str="myselfprince mali stduying pyhton fron apna college"
# str=str.capitalize()90

# print(str)


# majdoor=500
# if majdoor==500:

#     print("mai kaam karunga")
# else:
#     print("mai kaam nai karunga ")

# ram=int(input("enter the amount"))
# shyam=int(input("enter the amount"))
# if ram>=500 and shyam==500:
#     print("hum dono kaam karegne")
# else:
#     print("hum kaam nahi karegne")

# num1=int(input("enter the number"))
# num2=int(input("enter the number"))
# if num1 > num2:
#         print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#         print(f"{num1} is less than {num2}")
# else:
#         print(f"{num1} is equal to {num2}")

# gender=input("enter the gender")
# if gender == "m" or gender =="M":
#  print("goodmornig sir")c
# elif gender == "f" or gender == "F":
#      print("goodmornig mam")

# email_id=input("enter the email id")
# password=input("enter the password")
# if email_id=="Prince mali" and password==9008:
    
#     print("welcome the page")
# else:
#     print("welcome the password")

# # sub1=int(input("enter the marks"))
# # sub2=int(input("enter the marks"))
# # sub3=int(input("enter the marks"))
# # avg=(sub1+sub2+sub3)
# # if avg>=90:
# #     print("grade A")
# # elif(avg>=80 and avg<90):
# #     print("grade B")
# # elif(avg>=70 and avg<80):
# #     print("grade C")
# # elif(avg>=60  and  avg<70):
# #     print("grade D")
# # else:
# #     print("grade F")

# #palindrom
# #loops
# # for i in range(3,31,1):
# #  print(f"3x{i}={i}")

# a="princmali"
# for i in a:
#  print(i)

# a = "prince"
# for i in range(len(a)-1,-1,-1):
#   print(a[i],end="")

# name = "maliprince"
# for i in range(len(name)-1,-1,-1):

# name = "Red and white multimedia"
# for i in range(len(name)-1,-1,-1):
  
#   print(name[i],end=" ")


# n=int(input("enter the table"))
# for i in range(1,11):
#       print(f"{n}x{i}={n*i}")

# n=int(input("enter the no"))
# fact=4
# for i in range(1,n+1):
#     fact=fact*i
#     print(f"your sum is {fact}")

# x="99.9"
# print(type(x))
# y=float(x)
# print(type(y))
# print(y)

# x="Prince mali"
# print(type(x))
# y=bool(x)
# print(type(y))
# print(y)

# type converstion check
# x=0
# print(bool(x))
# x=2.0
# y=int(x)
# print(type(y))

# # implict and explicit
# a=18
# print(a/3)

# fisrt_name="Prince"
# last_name="mali"
# form = "goyali"
# print(fisrt_name,last_name,form)

# # formated string
# fisrt_name="Prince"
# last_name="mali"
# print(f"my name is {fisrt_name} {last_name}")

# len=int(input("enter the l"))
# w=int(input("enter the w"))
# area=len*w
# print(area)

# comparison operators
# a=2
# b=3
# c=2
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)

# num = 15
# rem = num % 2

# if(rem == 0):
#     print("even")
# else:
#     print("0dd")

# a=int(input("enter fisrt number:"))
# b=int(input("enter second number:"))
# c=int(input("enter thrid number:"))

# if(a >= b and a >= c):
#     print("fisrt number is largest",a)
# elif(b >= c):
#     print("second number is largest",b)
# else:
#     print("thrid is largest",c)

# x=int(input("enter number:"))

# if(x % 6 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple")

# list[A bulit-in data type that stores set of values it can store elements of different types(integer, float, string,etc.)] & Tuples
# marks1 = 58.45
# marks2 = 78.57
# marks3 = 96.89
# marks4 = 89.89
# marks5 = 67.78

# marks = [58.45,78.57,96.89,89.89,67.78]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[2])

# student = ["Prince",89.89,19,"rajasthan"]
# print(student[0])
# student[0] = "arjun"
# print(student)

# marks = [89,45,78,90,68]
# print(marks[0:3])

# list Methods
# list = [2,1,5]
# list.append(4) #adds one element at the end . [2.3.3.4]
# list.sort()#sorts in ascending order [1.2.3]
# list.sort(reverse=True)#sorts in descending order [3,2,1]
# list.reverse()reversea list [3,2,1]
# list.insert(idex,el) insert element at indes

# n=int(input("enter a number: "))
# print(f"factors of", {n},"are:")
# for i in range(1,n + 1):
#     if n % i == 0:
#         print(i)

# num=int(input("enter the number"))
# if num % 2 == 0:
#     print("even")
# else:
#     print ("odd")

# # a="prince"
# # for i in a:
# #     print (i)

# if(i=="j"):
#  print("this is something special")

# n=int(input("enter the no"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
#perfect number
# n=int(input("enter the number"))
# sum=0
# if i in range(1,n):
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect numer")


# a="prince"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# for i in range(1,31,2):
#     if i==28: 
#      continue
#     print(i)


# n=int(input("enter the no")) 
# for i in range(1,n+1):
#     if n%0==i

# Interactive personal Data Collector
print("Welcome to the Interactive Personal Data Collector!\n")
    # collect user inputs 
name = input("Please enter your name: ")
age =int(input("Please enter you age:"))
height =float(input("Please enter your height"))
favourite_number = int(input("Please enter your favourite numbe:"))

print("Thank you! Here is the infomation we collected:\n")
    #Display collected data with type and memory address 
print(f"Name: {name} (Type: {type(name)},")
print(f"Memory Address: {id(name)}\n")

print(f"Age: {age} (Type: {type(age)},")
print(f"Memory Address: {id(age)})")

print(f"Height: {height} (Type: {type(height)},")
print(f"Memory Address: {id(height)})")

print(f"Favourite Number: {favourite_number} (Type:{type(favourite_number)},")
print(f"Memory Address: {id(favourite_number)})")

# calculate approximate bith year
current_year = 2026
birth_year = current_year - age

print(f"\nYour birth year is approximately:")
print(f"{birth_year} (based on my age of {age})")

print("\nThank you for using the Personal Data Collector.Goodbye!")










    











    


  



















    











          






















