'''
Tuple is similar data-type in python which is very similar to list.
The only difference between a tuple and a list is tuples are immutable data-type
i.e., once a tuple is created it cannot be changed!!!
Tuples are iterable data-type ,this means we can iterate on tuples and take slices of it

So, We use tuples to protect our data from change!!
'''

print('----tuple-create-----')
our_tuple=(1,2,3,'A','B','C')
our_tuple2=4,5,6,'D','E','F'
print(type(our_tuple))
print(type(our_tuple2))
print(our_tuple2[0:3])
print('---Difference between tuples and list----')
mylist=[1,2,34,5,6]
print('insert value 100 at index 2')
mylist.insert(2,100)
print(mylist)

print('we cannot insert values in tuples ')
'''
our_tuple2[2]=100
print(our_tuple2)

our_tuple2[2]=100
TypeError: 'tuple' object does not support item assignment

same thing happens with string too!!
s='abcdef'
s[2]='z'
print(s)
ERROR:
    s[2]='z'
TypeError: 'str' object does not support item assignment
'''
# we use tuple() function to convert a data-type into tuple

A=[1,2,3]
print(type(A))
print('List Converted to Tuple!!')
B=tuple(A)
print(type(B))

# we can do multiple assingment if we have tuple at one side and any
# other iterable data-type at the other side.
print('------multiple assingment-----')
(A,B,C)=1,2,3
print(A)
print(B)
print(C)
D,E,F=[4,5,6]
print(D)
print(E)
print(F)
G,H,I="789"
print(G)
print(H)
print(I)




