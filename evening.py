#split()
#--> it is used to split the given string based on max_splits
#by default it will split the spaces
#syntax:
#--------------
##string.split('character',max_splits)
##s='hello every one'
##print(s.split())
##s='malayalam'
##print(s.split('a'))
###[m,l,y,l ,m]
##print(s.split('a',2))
##print(s.split('a',100))
##print(s.split('z'))

#strip()
#-----------------
        #h   e     l     l       o        
# it is used to remove specified element from both leading and tailing part
# by default it removes space
#syntax
#--------------------
##string.strip('element')
####s='           hello           '
####print(s)
####print(s.strip())
##s='@@@@hello@@@@'
##print(s.strip('@'))

##s='@@#@@he@llo@@@@'
##print(s.strip('@'))

# isupper()
#it return True /False
# if the given string is having completely uppercase characters
#it won't accept any argument
#syntax :
#-----------------
# string.isupper()
#s='HELLO'
#print(s.isupper())    #True
#s='HElLO'
##print(s.isupper())

##s='HELLO1'
##print(s.isupper())
##s='HELL@123'
##print(s.isupper()) 
##s='123456'
##print(s.isupper()) 


#islower()
#------------------------
#it return True /False
# if the given string is having completely lowercase characters
#it won't accept any argument
#syntax :
#-----------------
# string.islower()
#s='hello'
##print(s.islower())
##s='hEllo'
##print(s.islower())
##s='1hello'
##print(s.islower())
##s='@pple'
##print(s.islower())


#isalpha()
#it returns true if the given string is having completely alphabets
#it wont accept any argument
# syntax :
#-----------------------
##string.isalpha()
#s='heLLo'
##print(s.isalpha())
#s='hello1'
##print(s.isalpha())
##s='@pple'
##print(s.isalpha())
##s='hello every one'
##print(s[::2].upper()[::-1].split('O'))
#hloeeyoe.upper()----->HLOEEYOE ---> E|YEE|LH----> [E,YEE,LH]

#isdigit()
# it return true if the string contains only numbers
#it wont accept any argument
#syntax :
#------------------
##string.isdigit()

##s='12345'   
##print(s.isdigit())

##s='123G'
##print(s.isdigit())

#isalnum()
#--------------------------
#it return True if the given string is having completely alphabets
#   or
#it return True if the given string is having completely numbers
# or 
#it return True if the given string is having combination of alphabets and numbers
##s='hello'
##print(s.isalnum())
##s='123'
##print(s.isalnum())
##s='a1h2e3'
##print(s.isalnum())
##s='@'
##print(s.isalnum())

#isspace()
#------------------------
#it return if the given string is having completely space
# it wont accept any argument
#syntax:
#----------
#string.isspace()
##s='             '
##print(s.isspace())
##s='       h        '
##print(s.isspace())
#----------------------------------
#indexing and slicing
#----------------------------------
#upper lower swapcase capitalize title  # --> 
#index find  split  strip,count     
#isupper islower isalpha isdigit isalnum isspace  isidentifer()


# LIST
#-----------------------------------------
# it is a collection of homogeneous and hetrogeneous type of data
# boundaries of list are []
# list is a mutable datatype
#list allows duplicates  [1,2,3,1,2,4,5]
#list is a ordered datatype [1,2,3]     -----> 1   2     3
# list supports indexing and slicing
#default value of list is []
##[1,2,3,4,5]
#    0 1 2 3 4 
# indexing :---->>> ls[index]
#slicing     :------>>>    ls[si:ei:sv]
##print(ls[2])
##print(ls[1:4:2])   #2 4

##lst=['apple','bannana','mango',[1,2,3,4,[5,6]]]
##print(lst[0])   #apple
##print(lst[1].count('n'))
##print(lst[2][3])
##print(lst[2][3])     #'mango'[3] ---'g'

##lst
##lst=['apple', 'bannana', 'mango', [1, 2, 3, 4, [5, 6,'tamarind']]]
##lst[3]
##[1, 2, 3, 4, [5, 6]]
##lst[3][4]
##[5, 6]
##lst[3][4][1]
##6

#D
##print(lst[3][4][2][-1].upper())
# add       # remove     #update

#update
##lst=[1,2,3,4]
##print(id(lst))
#1 --->> 11
#syntax :
#---------------------
# lst[index]=value
#---------------------
##lst[0]=11
##print(lst)
##print(id(lst))

##lst=[1,2,3,4,5,6,7,'hello']
#      0 1 2 3 4 5 6   7
#o/p----->>>   [1,2,3,4,5,6,7,'bye']
##lst[7]='bye'
##print(lst)
##lst[7][1]='f'    # helllo[1] ---->> e ='f'
##print(lst)   #TypeError: 'str' object does not support item assignment
##lst[8]='hi'   #IndexError: list assignment index out of range



#adding of elements
#---------------------------
#1.append
#2.extend
#3. insert

#1.append
#---> it is used to add the element at last
#---> we can pass both collection and individual datatypes
# syntax :
#--------------------
#     lst.append(element)
##lst=[1,2,3]
###4
##lst.append(4)
##lst.append('hello')
##print(lst)

#int float complex boolean

#string list tuple set dictionary

##lst=[1,2,3]
##lst.append(4)  #int
##lst.append(12.2)  #float
##lst.append(True)  #bool
##lst.append(10+2j)  #complex
###collection
##lst.append('string')
##lst.append([1,2,3,4])
##print(lst) #[1,2,3,4,12.2,True,10+2j,string,[1,2,3,4]]


#Extend

# it is also used to add the element at last
# it will accept only collection datatypes
# it will unpack and it will add
# it will do  unpacking only once

#syntax:
#--------------------
# lst.extend(element)

#    'hello'------>>> 'h','e','l','l','o'
##lst=[1,2,3]
##lst.append('hello')
##lst.extend('hello')
####print(lst)
##lst.extend(10)

##lst=[1,2,3]
##lst.extend(['hello'])     #                ['hello']    #---->> []----> 'hello'
##lst.append(['hello'])   #               ['hello']
##
##print(lst)



#insert
#-------------------------------
# we can add the element at specific position
#if the specified element is not present it will add the element at last
# syntax :
##list.insert(index ,element)
##lst=[1,2,3,4,5,6,7,8]#  0 1 2 3 4 5 6 7 
#                                       1 2 3 4 5 6 7 8 
##lst.insert(1,22)
##print(lst)
##lst.insert(100,99)
##print(lst)


# to update the element   -------> >>> lst[index]=value


# remove the element from a list :
#-----------------------------------------
##1.remove() 
# 2.pop()
#3.clear()


#1.remove
#-------------------------------
# it is used to remove the first occured specified element from a list
# it raises valueerror if the specified element is not present
#syntax:
##list.remove(element)
##lst=[1,2,3,1,2,3]
##lst.remove(1)
##print(lst)
##lst.remove('a')   #ValueError: list.remove(x): x not in list

#2.pop()
# ---> it is used to remove the element  based on the index
# if we dont pass any index  by default it removes the last element
# it raises the error if the specified index is not present in a list
#syntax:
#---------------------------
##list.pop(index)
##lst=[11,22,33,44,55,66,77,88]
##lst.pop(5)
##print(lst)   #[11, 22, 33, 44, 55, 77, 88]
##lst.pop()
##print(lst)    #[11, 22, 33, 44, 55, 66, 77]

##lst.pop(100)   #IndexError: pop index out of range


#3.clear()
# it wont accept any argument
# it will remove all the elements from a list
#syntax:
#-------------------
##lst.clear()
##lst=[1,2,3,4,5,6]
##lst.clear()
##print(lst)  # []


# tuple
#-------------------
##it is a collection of homogeneous and hetrogeneous type of data
# boundaries of tuple  are ()
# tuple is a immutable datatype
#tuple allows duplicates  (1,2,3,1,2,4,5)
#tuple is a ordered datatype (1,2,3)    -----> 1   2     3
# tuple supports indexing and slicing
#default value of tuple  is ()
#---------------
#examples
#---------------
##s=(1,2,3,4,5,6,2,2,2,2,2)
##print(s.count(2))   #------>> 6
##print(s.index(2))   #----->>   1
##print(s.index(22))   #ValueError: tuple.index(x): x not in tuple


#set
# it is a collection of homogeneous and hetrogeneous type of data
# boundaries of set is {}
# set does not allows duplicates
# set is a unordered datatype
# set does not support indexing and slicing
#set is a mutable datatype but values present in the set must be immutable
#default value of set is       set()
#s={}#---> inside the set we can store only int float complex boolean ,string ,tuple 

##s={11,22,33,44,55}
##print(s)
##{33, 22, 55, 11, 44}
##s[0]
##Traceback (most recent call last):
##  File "<pyshell#0>", line 1, in <module>
##    s[0]
##TypeError: 'set' object is not subscriptable
##s[::-1]
##Traceback (most recent call last):
##  File "<pyshell#1>", line 1, in <module>
##    s[::-1]
##TypeError: 'set' object is not subscriptable

##s={'hello','hi','hello'}
##print(s)    #{hi,hello}
##s=set()
##print(s)  #set()

##s={11,10.2,True,2+5j,'hi',(1,2,3)}
##print(s)
#add the element

#add()


#it is used to add the element randomly into a set
#syntax:-
#----------
##set.add(element)

##s={1,2,3,4,'hello',(1,2,3)}
##s.add(11)
##print(s)

#remove the element
#remove()
#it is used to remove the specified element  from a set
#it raises error if the specified element is not present in a set
#syntax:
#--------------------
##set.remove(element)
#s={1,2,3,4,5}
##print('before removing',s)
##s.remove(5)
##print(s)
##s.remove(55)    #KeyError: 55


#discard()
##it is used to remove the specified element  from a set
# it wont throws any error if the sepecified element is not present 

#set.discard(element)
##s={1,2,3,4}
##s.discard(4)
#print(s) #{1, 2, 3}
##s.discard(10)
##print(s)

#pop()

#it is used to remove the element randomly
# it wont accept any value
#syntax
#------------------
##s={1,2,3,4}
##s.pop()
##print(s)

#clear()
# it will remove all the elements from a set
#it wont accept any argument 
#syntax :
#-----------
##set.clear()
##s={1,2,3,4}
##s.clear()
##print(s)   #set()

# update the element

#update
#it is used to update the set
# it will add the element by unpacking
#it accept only collection datatype

##set.update(element)

##s={11,22,33,44}
##s.update('hello')
##print(s)
##s={'hi','hello'}
##s.update('hello')  # 'h' 'e'  'l'  'l' 'o'
##print(s)   #{'e', 'hello', 'l', 'h', 'o', 'hi'}



#dictionary
#----------------------
# here we will store the data in a form of key and value pair
#key and value are seperated by :
#key value pairs are seperated by ,
#dupplicate keys are not allowed but duplicate values are allowed
# key must be immutable datatype and values can be any python valid datatypes
#dictionary is a ordered datatype
#dictionary does not support indexing and slicing
#boundaries of dictionary is {}
#default value of dictionary is {}
#syntax:
#----------
##dic={'a':1,2:'b',True:[1,2,3,4]}
##print(dic)
##{'a': 1, 2: 'b', True: [1, 2, 3, 4]}
####lst[index]
###dic[key]
##dic[3]
##Traceback (most recent call last):
##  File "<pyshell#2>", line 1, in <module>
##    dic[3]
##KeyError: 3
##dic['a']
##1
##dic[b]
##Traceback (most recent call last):
##  File "<pyshell#4>", line 1, in <module>
##    dic[b]
##NameError: name 'b' is not defined
##dic[2]
##'b'

##dic={[1,2,3]:'list is my key','a':123}   #TypeError: unhashable type: 'list'
##dic={'a':1,'b':2,'c':1}
##print(dic)

# to acess the element
##dic[key]  #---->>> dic['a']=1   #---->> dic['z']---> keyError:'z'

#to insert the elements into a dictionary
#    dic[key]=value
##dic={'a':1,'b':2,'c':3}
####dic['d']=4
####print(dic)   #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
####dic['e']=5
####print(dic)
##dic['a']=11
##print(dic)


#upper ()
#lower()
#isupper()
#islower()
#isalnum()
#lst.append()
#s.add()
#dic[key]=value



# operators in python
#1.arthemetic operators(+,-,*,/,//,%,**)
# % it is use to get the remainder
#**  exponant --> gives the power of a given number a**b
#/----> True division   5/2 ---->2.5
#// ----> Floor division 5//2  ----> 2
##s='apple'
##print(s[0:len(s)//2])  #ap
##print(s[len(s)//2])    #p

#relational datatypes /comparision (>,<,>=,<=, !=,==)
##print(10>2) #True
#==   (equals equal or double equals) comparision
##a=10
##print(a==10)


##3.assignment operator (=)

##a=20
##b='hello'

#4.logical operators (and or not)
#and :-->>it returns true if all the given conditions are satisfied
##print(10==10 and 20==20)
##print(10==10 and 20!=20)
#       true                    false

##True=1			
##False=0			
##    condition1  condition2	result 
##	1	0	0
##	0	1	0
##	0	0	0
##	1	1	1


#or ---> it returns true if any one of the condition is satisfied
##print(123==1 or 'a'=='a')  #true
##    condition1  condition2	result 
##	1	0	1
##	0	1	1
##	0	0	0
##	1	1	1

#not---> it will reverse the decision
#      ---> it will accept only one argument
##print(not True) #False
##print(not (10==10))   #10!=10


#identity operators
#is
#is not
# are used to check whether given variables are pointing to a same memory address or not
##a=10
##b=10
##c=20
####print(a is b) #True
####print(a is c)    #False 
##print (a is not c)  #True

#member ship operators

# in
#not in
# this operators are used to check whether given character is present in a collection or not
##print('a' in 'aeiou')   #True
##print('b' in 'aeiou')   #False
##print('a' not in 'aeiou')   #False
##print('b' not in 'aeiou')   #True
##print ('hello' in ['hi','hello','bye'])



































































