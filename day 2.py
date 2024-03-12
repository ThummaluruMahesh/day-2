'''
a, b=c=7,8
print(a)
print(b)
print(c)
'''


'''
a=b, c=4,2
print(a,b,c)
'''

'''
---> changing of variables
a=7
b=5
Eg:1
temp=a temp=7
a=b    a=5
b=temp b=5

a=5,b=7
print(a,b)
'''
'''
Eg:2
a=7
b=5
a=a+b
b=a-b
a=a-b

print(a,b)
'''

'''
Eg:3

a=7
b=5
a, b=b, a
print(a,b)
'''
'''
Eg:4
a=7
b=5
a=a*b
b=a/b
a=a/b
print(int(a), int(b))
'''

'''
Eg:5
id()--->used to find the memory address of the variable
a=7
b=5
print(id(a)
print(id(b)
'''

'''
--->keywords
keywords are reserved words which provides special meaning to compiler or interpreteor
'''
import keyword   
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

'''
#To check if the string is keyword or not
print(keyword.iskeyword("mahesh"))# false

if = 8
print(if)# error coz if is a keyword
'''
'''
#--->literals
Literal is the constant value assigned  to a variable
A variable is considers to be constant when it is defines
in caps

a= 78 # a is variable
A=78 # A is constant
'''

'''
hash() -->it creates a hash value for constan datatypes and
provides error for non constant datatypes 
n1=89+7j
print(hash(n1))

f1=[7,8,9]
print(hash(f1))# error --> list is non constant or mutable datatype

a=9
b=9
b=90
print(id(a))
print(id(b))

# ---->operators
#operators are symbols which is used to perform various operations between 2 or more operations 

#Arithmatic
#Assignment
#Logical
#Relations or comparison
#Bitwise
#Identity
#Membership


# todo ----> Arithmatic ---> +,-,*,/,%,//,**
#Eg:1

a=8
b=6
c=9
print(a+b+c)


#input() --> used to get the runtime input
n1 = input ("enter the value")
print(n1)


# ! //--> floora = 765433
b = 19
print(a//b)

# ! comparision ---> ==, >,<,!=,<=,>=
a=8
b=7
print(a>b)


a=9
b=5
print(a==b)


# ! bitwise operator ---> &,|,^,~,<<,>>

a=7
b=4
print(a&b)
'''

'''

# AND
 A B A^B
 0 0  0
 0 1  0
 1 0  0
 1 1  1

# OR
 A B A|B
 0 0  0
 0 1  1
 1 0  1
 1 1  1

# X OR
 A B A^B
 0 0  0
 0 1  1
 1 0  1
 1 1  0

 32 16 8 4 2 1
 0  0  1 0 1 0 #--> 10
 1  0  0 1 1 0 #--> 38
------------------------
 1     1 1

print(10^38)

# 2^4 2^3 2^2 2^1 2^0
  8    4   2   1

  0    1   1   1  # -->7
  0    1   0   0  # --> 4  &
----------------------------
  0    1   0   0

# ~ --->

a=9876
print(~a)
'''


# ! Logical --> used to compare the expressions
#and, or , not
'''
a=6
print(a>3 and a<10)
print(a>7 or a<30)
print(not(a>8 and a<10))
'''

'''
#! Identity operator
# is, is not
a=8
b=8
print(a is b) # output = True
print(a==b) # output = True
print(a is not b) # output = False
'''
a=[1, 2, 3]
b=[1, 2, 3]

print(a is b)

false
'''
'''
a=(1, 2, 3)
b=(1, 2, 3)

print(a is b)

true
'''
# ! Membership operator
#in, not in
'''
'''
L1 = [7, 8, 9, 0, 6, 5]
num =55
print(num in L1)
print(num not in L1)

num = 678
print(8 in num )
'''
'''
#Eg: 1

  a=7
if a <8:
    print("hello")

else:
    print("no")
'''
'''
# a number is even or odd
n = int(input("enter the number: "))
if n %2==0:
    print(n, "is even")
else:
    print(n, "is odd")
    '''
'''
#name, age, nationality
# 18 above, indian

name = input("enter the name:")
age = int(input("enter the age:"))
nationality = input("enter the nationality:")
'''










                                                                                                           





























































































































































































































































































































