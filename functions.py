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
'''
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def floor_division(a,b):
    print(a//b)
def true_division(a,b):
    print(a/b)
def mod(a,b):
    print(a%b)
def mul(a,b):
    print(a*b)
v1=int(input('enter the value1'))
v2=int(input('enter the value2'))
print('select any one of the operator:==>  +  , - , * , // , / , %')
symbol=input('enter the operator')
if symbol=='+':
    add(v1,v2)
elif symbol=='-':
    sub(v1,v2)
elif symbol=='*':
    mul(v1,v2)
elif symbol=='//':
    floor_division(v1,v2)
elif symbol=='/':
    true_division(v1,v2)
elif symbol=='%':
    mod(v1,v2)
else:
    print('invaid operator')

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











