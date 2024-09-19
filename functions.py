# it is a block of code or set of instructions which are
# used to perform some  specific task when ever we call
'''
syntax:
def function_name(parameters) :  #function declaration
    statement1
    statement2
    return data1,data2,.....
function_name(arguments)   # function calling
'''
from os import remove

'''
waf to add 2 numbers
'''
# def add(a,b):
#     print(a+b)
# a=int(input('enter the number:'))  #10
# b=int(input('enter the number:'))  #11
# add(a,b)   #add(10,11)

# def add(a,b):
#     #instead of printing we will use return keyword to return the
#     #value to fucntion calling
#     return a+b    #9
# print(add(5,4)+4)

'''
waf to print hello if the given number is even else print bye 
'''
# def even_odd(a):     # a==100
#     if a%2==0:
#         return 'hello'
#     else:
#         return 'bye'
# u_n=int(input('enter the number:')) #100
# print(even_odd(u_n) ) #100
'''
waf to check given string is palindrome or not 
'''

# def palindrome(s):  #s='malayalam'
#     if s==s[::-1]:
#         print('palindrome')
#     else:
#         print('not a palindrome')
# a=input('enter the string ')
# palindrome(a)

'''
waf to create a calculator
# add  sub   mul   floor division   true division modules
ask user to enter 2 values along with ask the operator 
  +    -    *    // / %
# '''
# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def floor_division(a,b):
#     print(a//b)
# def true_division(a,b):
#     print(a/b)
# def mod(a,b):
#     print(a%b)
# def mul(a,b):
#     print(a*b)
# v1=int(input('enter the value1'))
# v2=int(input('enter the value2'))
# print('select any one of the operator:==>  +  , - , * , // , / , %')
# symbol=input('enter the operator')
# if symbol=='+':
#     add(v1,v2)
# elif symbol=='-':
#     sub(v1,v2)
# elif symbol=='*':
#     mul(v1,v2)
# elif symbol=='//':
#     floor_division(v1,v2)
# elif symbol=='/':
#     true_division(v1,v2)
# elif symbol=='%':
#     mod(v1,v2)
# else:
#     print('invaid operator')

'''
name_password={'dinga':1234,'dingi':4567}
name_amount={'dinga':1000,'dingi':500}

# u_n:==
pass:==

# if both are correct 
welcome to the bank
1.deposit    2.withdraw     3.balance check 

deposit:-
a=enter the money:
name_amount[key]=name_amount[key]+a
###update the database

witdraw:-
a=enter the amount
if a <=name_amount[key]:
     deduct 
name_amount[key]=name_amount[key]-a

balance check :
  display the balance 

'''

'''
oops---> object oriented programming system
class
---> it is a blue print or templete which is used to create the object
---> to create the class we need to use the  keyword called class
syntax:
class class_name:
        statements
object 
===>> it is a real time entity or instance of a class 
===>> we can create more than one object for a single class
===>> every object is independent 
class class_name:
    statement
    
# to create the object
variable_name=class_name()
'''

# class Sample:
#     def add(self,a,b):
#             print(self)
#         print(a+b)
#     def sub(self,a,b):
#         print(a-b)
# o1=Sample()   # object creation
# a=int(input('enter the first number:'))
# b=int(input('enter the second number:'))
# o1.add(a,b)   # o1.add(ox11,4,5)
# o1.sub(a,b)   #   sub(ox12,3,1)
'''
inheritance
# inheriting the properties from parent to child class 
    1.single level inheritance
'''
# class Father:  # parent
#     def land(self):
#         print('50 acres of  land')
# class Son(Father):   #child
#     #land()
#     def propeties(self):
#         print('3 bhk house')
# f=Father()
# f.land()
# s.propeties()

# class whatasapp_v1:   # grandfather
#     def chatting(self):
#         print('10000 chatting')
#     def status(self):
#         print('10000 status')
# class whatsapp_v2(whatasapp_v1):   # Father
#     #chatting
#     #status
#     def vdocall(self):
#         print('1000 vdocall')
# class whatsapp_v3(whatsapp_v2):    # son
#     #chatting   #status   # vdocall
#     def payment(self):
#         print('payment code..')


# class Father:
#     def land(self):
#         print('land')
# class Mother:
#     def gold(self):
#         print('gold')
# class Son(Father,Mother):
#     #gold    land
#     def house(self):
#         print('house')
#
# class Father:
#     def land(self):
#         print('land')
# class son1(Father):
#     #land()
#     def gold(self):
#         print('gold')
# class Son2(Father):
#       # land
#     def house(self):
#         print('house')
# s=Son2()


# class Animal:
#     def sound(self):
#         print('animal sound')
# class lion(Animal):
#     #sound
#     def hunting(self):
#         print('hunting')
# class tiger(Animal):
#     #sound
#     def running(self):
#         print('running')
# class liger(lion,tiger):
#    #running hunting sound
#     def height(self):
#         print('height')
'''
polymorphisam 
poly ---->>> many      morphisam  ---->> forms
---> an object showing diff behaviours at diff stages of its life cycle 
print(10+20) ----->> addition 
print('hi'+'good')  ----->> concatination 
'''
#method overriding
# declaring a method with the same name but with diff implimentation in the sub class
# in method overriding  sub class implimentation will hide the super class implimentation
#to get the super class implimentation also we needd to use a class  called super
# class whatsapp:
#     def chat(self):
#         print('chatting')
#     def status(self):
#         print('status')
# class whatsapp_v2(whatsapp):
#     def chat(self):
#         print('payment')
#         super().chat()
#     def vdocal(self):
#         print('vdocall')
#
# w=whatsapp_v2()
# w.chat()


# class Animal:
#     def sound(self):
#         print('animal sound')
# class Dog(Animal):
#     def sound(self):
#         print('dog sound')
#         super().sound()
# class cat(Animal):
#     def sound(self):
#         print('cat sound')
# class rat(Animal):
#     def sound(self):
#         print('rat sound')
#         super().sound()
# #variable_name=class_name()
# d=Dog()
# c=cat()
# r=rat()
# print('enter the option :d  for dog     c for cat     r for rat')
# user_input=input('enter the character:').lower()
# if user_input=='c':
#     c.sound()
# elif user_input=='d':
#     d.sound()
# elif user_input=='r':
#     r.sound()
# else:
#     print('invaid character...')

'''
abstraction
#  we can create  2 types of methods 
1.concrete methods
#method declaration will present as well as method implimentation 
def function_name():   #-------->> declaration
     code......        # -------->> implimentation

2.abstract methods

#only method declaration will present but not implimentation 
def function_name():   #-------->>> declaration 
    pass

######
we have 2 types of classes 
1.concrete class---->>> only concreate methods 
2.abstract class----->>> we can create both abstract and concrete methods 
                ------>> we can not create the object for abstract class

                --->> we need to inherit the abstract class and provide the 
                #     implimentation in the sub class
syntax :
from abc import ABC,abstractmethod
class class_name(ABC):
    @abstractmethod
    def function_name(self):
            pass
'''

'''
instagram
1.vdocall
2.filter
3.reels
'''
'''
abstraction:
#------------------------
declare all the imp funtions in the abstract class and prividing  implimentation in 
the sub class to achieve 100 % of the implimentation 
'''
# from abc import ABC ,abstractmethod
# class sample(ABC):
#     @abstractmethod
#     def vdocall(self):
#         pass
#     @abstractmethod
#     def filter(self):
#         pass
#     @abstractmethod
#     def reels(self):
#         pass
#     def gifs(self):
#         print('gifs')
# class Instagram(sample):
#     def vdocall(self):
#         print('1000 lines')
#     def filter(self):
#         print('1000 lines')
#     def reels(self):
#         print('1000 lines ')
# i=Instagram()
'''
encapsulation
#-----------------------------
declaring a public variable into private and restricting acess from one class to another
#acess specifier
#--------------
1.public acess specifier  (cycle)
2.protected acess specifier (bike)
3.private acess specifier   (car)
'''
# __init__()   # inbuilt or magic method
# when ever we are creating a object
# class Sample:
#     def __init__(self,name,age):
#         self.name=name  #ox11.name='dinga'    #ox12.name='dingi'
#         self.age=age   #ox11.age=21            # ox12.age=22
# s=Sample('dinga',21)    #(ox11,dinga,21)
# s1=Sample(age=22,name='dingi')  #(ox12,dingi,22)

#public acess specifier
# class a:
#     def __init__(self,age):
#         self.age=age
# q1=a(21)
# print(q1.age)
# class b:
#     print(q1.age)
# q2=b()

#protected acess specifier
#-----------------------------

# class a:
#     def __init__(self,age):
#         self._age=age
# q1=a(21)
# print(q1._age)
# class b:
#     print(q1._age)
# q2=b()

#private acess specifier
#---------------------------------

# class a:
#     def __init__(self,age):
#         self.__age=age
# q1=a(21)
# print(q1.__age)
# class b:
#     print(q1.__age)
# q2=b()


# encapsulation
#-------------------------
# class Bank:
#     def __init__(self,name,atmpin):
#         self.name=name
#         self.__atmpin=atmpin  #1233
#     def get_atmpin(self):
#         return self.__atmpin   #ox11.__atmpin
#     def set_atmpin(self,newpin):
#         self.__atmpin=newpin  #2344
# b=Bank('dinga',1233)   #(ox11,dinga,1233)
# c=Bank('dingi',2345)


'''
class Bank:
    def __init__(self,name,atmpin):
        self.name=name
        self.__atmpin=atmpin  #1233
    def get_atmpin(self):
        return self.__atmpin   #ox11.__atmpin
    def set_atmpin(self,newpin):
        self.__atmpin=newpin  #2344
b=Bank('dinga',1233)   #(ox11,dinga,1233)
c=Bank('dingi',2345)
print('select one option : 1.to show atmpin   2. to update atmpin')
u_i=int(input('enter the option :'))
if u_i==1:
    password= input('enter the password')
    if password=='dinga123':
        print(b.get_atmpin())
    else:
        print('error')
elif u_i==2:
    pin=int(input('enter the pin'))
    if pin ==1233:
        new_pin=int(input('enter the new pin'))
        b.set_atmpin(new_pin)
        print(b.get_atmpin())
'''

'''creation of atmpin'''
# dic={}
# user_name=input('enter your u_name:')
# password=input('enter your password')
# if user_name=='dinga':
#     if password=='qwerw':
#         atm_Pin=input('enter your new pin :')
#       dic[user_name]=atm_Pin

'''
# file -handling 
#acessing the files from software to hardware and hardware to soft ware 
to perform CRUD operation 
C-create
R-read
U-update
D=delete 
'''
# import os
# os.chdir(r'C:\Users\pnsan\Desktop')
# 2 ways to open a file

# variable_name=open('file_name',mode)
# variable_name.close()

# a=open('neeraj.txt','r')
# print(a.read())
# a.close()

#2.  by using with open
# with open('neeraj.txt','r') as file :
#     print(file.read())



# with open('evening.txt','w') as file :
#     file.write('hello every one')

# with open('123.txt','w') as file:
#     file.write('\n\thello bye\ngooddddddd')

# with open('123.txt','r') as f:
#    print( list(f).pop(4))
    # print(f.read())
'''
r--->> read -->> used to read the data from a file 
w---->> write ---->> used to update the file if file is not not present ceate the file  
a---->> APPEND---->> used to add the file if the file is not present it will create the file
'''







print('hi')
try:
    a=10
    print(a[0])
except:
    print('error is present')
print('hello')





