'''
There are only really two types of variable scope in python:
1. One big global scope
2. There are multiple little local scopes
-->> If a variable is in the global scope it's called a global variable and
    can be seen anywhere in our program.
-->> On the other hand if a variable is in local scope it's called a local variable
    and can be seen within the specific local scope that it's in.
In python "functions" create local-scopes whereas "loops and if statements" don't.

'''
a=100

def f1():
    print(a)
def f2():
    print(a)

print('Since a is global varibale so it will be printed twice:')
f1()
f2()

def f3():
    b=200
    print(b)
f3()
'''
def f4():
    print(b)
f4()
print(b)
NameError: name 'b' is not defined

We get error because b is in local scope of f3() and is invisible for f4()

-->> So imagine this little scope being lke a little bubble for each of the functions
 and whatever's inside is protected and anything outside can also come inside the bubble.
'''


def f5():
    print(a)
def f6():
    a=50
    print(a)
f5()
f6()
print("value of a =",a)
'''
We could see that in many functions we changed the value of a but when we
printed the value of a outside the function it's still same,because
you can't change global variables inside of functions automatically and besides this
the local variables are destroyed when the function finishes a case surviving gives the variable some memeory space when the functions runs,
and it just removes that variable from memory


---->>> Functions create local scopes and everything inside of a local scope is only
visible within its own little bubble.
Global variables are visible from everywhere and they can be accessed from everywhere
but they can not by default be changed from inside a local scope.
If you want to change a global variable you either have to be in the global
scope or you can use a trick defined below:
    global var-name
    then do the changes
    
---->>>
'''

xyz=500
def fun1():
    global xyz
    xyz=100 # changed global value
    print(xyz)

def fun2():
    xyz = 250  # local variable xyz will be created and printed below
    print(xyz)
fun1()
fun2()

print('Global variable was 500 , now it is =',xyz)

'''
For lists and dictonaries also we cannot change the whole things but 
we can change part by part as done below. we donot have to use global value here
'''
list_one=[1,2,3,4,5]
def list1():
    print('value of list remained same=',list_one)

def list2():
    list_one[0]=9
    print('value of index[0] changed=',list_one)
list1()
list2()
print('value of list in global scope=',list_one)







