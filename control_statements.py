#formating a string
# print('you got the output as ',10)
# you got the output as 10
# f-string
# print(f'you got the output {10*2}')

# programming


# control statements

# used to control the flow of exicution of a program

#       1.conditional statement
#       2.looping statements


#1.conditional statements
# this satements will tells us what to do if the condition is satisfied
# and what to do if the condition is not satisfied
    #   i. if
    # 2. if else
    # 3, if elif
    #4.nested if

#--------------------
#if
#-----------------

# if condition :
#     TSB

# wap to check given number is even number
# a=20
# if  a%2==0:
#     print(f'{a} is a even number')


# input()
# and this input always we will get in the form of string
# a=int(input('enter the value :'))   #7
# if a %2==0:   # 6 % 2==0: True
#     print(f'{a} is a even number')


#wap to check given number is divisible by 3 and 5
# user=int(input('enter your number:'))
# if user%3==0 and user %5==0:
#     print(f'{user} is divisible by both 3 and 5')

# wap to check given string is  starting with vowel
# s=input('enter the string :')   #Apple    #s[0]--      'a'.lower()   ---> 'A'
# if s[0].lower() in 'aeiou':
#     print('starting with vowel')


#if else
# if condition:
#     TSB
# else:
#     FSB

#wap to check given number is even or odd
# a=int(input('enter the value :'))
# if a%2!=0:
#     print('odd number')
# else:
#     print('even number')


# wap to  check given character is uppercase character or not
# a=input('enter the character')
# if a.isupper():
#     print(f'{a} is a uppercase character')
# else:
#     print(f'{a} is a lowercase character')
#
# variable='c'
# if 'a'<=variable<='z':
#     print('lower case character')
# else:
#     print('upper case ')

#wap to check given character is a special character or not
# a=input('enter the character:')   #    $
# if a.isalnum()==False:     #False == False
#     print('special character')
# else:
#     print('not a special character')


# if elif
'''
if conditon:
    TSB
elif condition:
    TSB
elif condition:
    TSB
.
.
.
else:
    FSB
'''

# wap to check given number is positive or negative or neutral number
# a=20
# if a>0:
#     print('positive')
# elif a<0:
#     print('negative')
# else:
#     print('neutral')
# a=-102
# if a>0 and a<100:
#     print('poisitve')
# elif a<0 and a>-100:
#     print('negative')
# elif a==0:
#     print('neutral')
# else:
#     print('enter the correct value .....')
# print('hello',end=' ')  #\n
# print('hi')


# wap to check
# 1 . if given number is divisible by 3 and 5 ---> FIZZBUZZ
# 2.    if given number is divisible by 3 only ---> FIZZ
#3.  if given number is divisible by 5 only ----> Buzz

# a=int(input('enter the number:'))
# if a%3==0 and a % 5==0:
#     print('FIZZ BUZZ')
# elif a%3==0:
#     print('FIZZ')
# elif a%5==0:
#     print('buzz')
# else:
#     print('invalid input')

'''
if condition:
  if condition:
        TSB
  else 
        FSB
else:
    fsb
'''

#wap to check given number is even or odd
#before checking check whether number is lessthan 10 or not
# a=int(input('enter the number:'))  #3
# if a<10:
#     if a%2==0:
#         print('even number')
#     else:
#         print('odd number')
#
# else:
#     print('given number is greater than or equals to 10 ')


#2.looping
# it is used to run some set of instructions n of times

# while
# it is used to run some set of instructions  n no of times
# --> for while loop looping variable is mandatory
#--> updation is mandatory


# syntax:
#--------
'''
i=0 #---> looping variable
while condition:
    code...
    updation  (increment or decrement the looping variable
'''
#wap 1 to 10 numbers
# i=1
# while i<=10:    # 11<=10   T
#     print(i)
#     i=i+1   #1 + 1  #i+=1 --> i = i + 1
#wap to print 10 to 1 numbers
# i=10
# while i>0:
#     print(i)
#     i-=1  # i=i-1

'''
wap to traverse through a string 
'''
# s=input('enter :')
# #
# i=0
# while i < len(s):
#     print(s[i])
#     i+=1    #string[index]   #index ---> number  --->>i


# wap to print even numbers present in a list
# lst=[1,2,3,4,5,6,7,8,9,10]
# #    0 1 2 3 4 5 6 7 8 9
# a=0
# while a<len(lst):  #0 1 2 3 4 5 6 7 8 9
#     if lst[a]%2==0:  # 1%2==0
#         print(lst[a],end=' ')
#     else:
#         print()#\n
#         print(lst[a],end=' ')
#     a+=1

#wap to create  a new list from an existing list
# lst=[1,2,3,4,5,6,7,8,9,10]
# #    0 1 2 3 4 5 6 7 8 9
# res=[]
# i=0
# while i<len(lst):
#     # to add an element into a list
#         #append  ----> lst.append(value)
#     res.append(lst[i])   #
#     i+=1
# print(res)



# lst=[1,2,3,4,5,6,7,8,9,10]
# #    0 1 2 3 4 5 6 7 8 9
# i=0
# while i<10:
#     # to add an element into a list
#         #append  ----> lst.append(value)
#     lst.append(lst[i]+10)   #
#     i+=1
# print(lst)


#wap to create a list from a old list  if the number is even do square and add
# else cube and add
# lst=[1,2,3,4,5,6,7,8,9,10]
# res=[]
# i=0
# while i <len(lst):
#     if lst[i]%2==0:
#        res.append(lst[i]**2)   #2**2
#     else:
#         res.append(lst[i]**3)
#     i+=1
# print(res)






# for i in collection/range:
#     statement
'''
string 
list
tuple
set 
dictionary 
'''
#wap to create a new list from aold list  if the elements present in the l
# ist starts with uppercase reverse and add to the list else add as it is
# lst=['apple','Bannana','Grapes','neem']
# res=[]
# for i in lst:
#     # i=apple
#     first_char=i[0]   #a
#     if first_char.isupper():
#         #i[::-1]
#         #to add the element into a list ----> lst.append(element)
#         res.append(i[::-1])
#     else:
#         res.append(i)
# print(res)

# wap to create a dictionary from a list with key as elements and value as index of the element
# lst=['apple','Bannana','Grapes','neem']
# #     0        1          2       3
# dic={}
# for i in range(len(lst)):   #0    1    2   3
#     key=lst[i]
#     value=i
#     #to add the element into a dictionary
#     dic[key]=value
# print(dic)

#apple:0,bannana:1

#  to add the element into a list -----> lst.append(element)
#  to add the element into a dictionary ---->> dic[key]=value


#wap create a dictinary from a string if the character is uppercase
# add character and index of the character
#else add character and uppercase character
# s='hElLo'   #h:H    E:1    l    L   o
# dic={}
# for i in range(len(s)):  # 0 1 2 3 4    #s[0]
#     if s[i].isupper():   #h
#         dic[s[i]]=i
#     else:
#         dic[s[i]]=s[i].upper()
# print(dic)

#s[0]   s[1]    s[2]    s[3]  s[4]


# wap to count how many alphabets are present in a given string
# s='hello123444'
# count=0   #5
# for i in s:
#     if i.isalpha():   False
#         count=count+1
# print(count)

#wap to count how many digits are presnet in a given string
# s='hello123444'
# c=0
# for i in s:
#     if i.isdigit():
#         c=c+1
# print(c)

# #wap to count how many special characters are present in a given string
# s='hel123lo@@@#'
# c=0
# for i  in s:
#     if i.isalnum()==False:
#         c=c+1
# print(c)


#wap to find sum of a given number

# a=1234
# b=str(a)   #'1234'
# s=0
# for i in b:   # 1     2      3    4
#     s=s+int(i)
# print(s)

# a=input('enter the number')  # '12345'
# dic={}
# s=0
# for i in a:
#     s=s+int(i)
# dic[a]=s    # {12345:15}
# print(dic)



# a=input('enter the number')  # '12345'
# lst=[]
# s=0
# for i in a:
#     s=s+int(i)
# lst.append(s)
# print(lst)



















