'''
We do some kind of comaprison and if the vvalue is postive we will get True else False
Comparison operator are defined below
:- we cannot use (=) operator for comprison. It is an assignment operator.

comparison-operators: use to compare piece of information to make condition
>,<,>=,<=,!=,==

Logical-operators: combine and modify the conditions to make bigger conditions.
not


'''

abc=True
print(type(abc))  #Boolean data-type

xyz="True"
print(type(xyz))  # string data-type
print('-------------------------------------------')
print(2>3) # we did comaprison and got the boolean value
print(type(2>3))
print('To check equality we should use "==" operator')
print(2==3) #False
print(3==3) #True
print(2!=3) #True
print(4>=3) #True
print(5>=6) #False
print(10<=11) #True
print('-------------------------------------------')
print('-------------------------------------------')
print('If Statements:')
'''
if condition: 
    print()
else:
    print()
'''
print('example_One')
if 2==2:
    print('2==2')
else:
    print('2!=2')

print('------example_2---------------')
num1=100
num2=50
if num1>=num2:
    print('if condition satisfied: num1>=num2')
else:
    print('else condition ')

print('------------------------------------------')
print('------If Else-------')
'''
if condition:
    print()
elif condition:
    print()
else:
    print()
'''

num_one=input('enter the first number')
num_two=input('enter the second number')

if num_one>num_two:
    print('first number is greater')
elif num_two>num_one:
    print('second number is greater')
else:
    print('Both numbers are equal')

print('-------------------------------------')
print('-------------------------------------')
print('Logical-Operators in Python:')
print(not(2<3)) #False
print('------not-operator----')
x=10
y=20
if not y<x:   # not y<x gives true
    print('it worked')

print('-----and operator-----')
if x>10 and y<30:  # if false and true = false : so no output
    print('and operator worked')

print('----combine not with and----------')

if not(x>10 and y<30):
    print('not with and ')

print('----or operator----')

if x>10 or y<30:
    print('or worked well')

print('-------not with or-----------')
if not(x>10 or y>30):
    print('not with or worked well')



