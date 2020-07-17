print('-----Lists-------')
our_list=[27,56,87,89]
print(our_list)
'''
List in python contains variables of different data-types.
and it is iterable in nature.
'''
myList=['a','b','c',1,2,3,'Do','Rey',True,False]
print(myList)
print(myList[2])
print(type(myList))
print(myList[0:3])


print('--------------------')
print('List inside list')
ourList=[1,2,[3,4,5],6,7]
print(ourList[2])
print('--printing the value of 3 --')
print(ourList[2][0]) # [2] for taking small list [3,4,5] and [0] for position of 3 inside that list
print(ourList[2][1:]) # slicing inside list

print('--------------------')
our_table=[[1,2,3],[4,5,6],[7,8,9]]
print(our_table[0])
print(our_table[1])
print(our_table[2])
print(our_table[0][0])
print(our_table[0][1])
print(our_table[0][2])
print(our_table[0][1:])
print('--------------------')
print('---solving projects------')
known_users=['alice','bob','claire','dan','emma','fred','harry']
print('how many elements are there:')
print(len(known_users))
user_name=input('what is your name?').strip().lower()
if user_name in known_users:
    print('Hello {}!'.format(user_name))
    remove=input('would you like to be renoved from the system(Y/N)?').lower()
    if remove == 'y':
        print(known_users)
        known_users.remove(user_name)   # it will remove the first occourence of the user_name
        print(known_users)
    elif remove=='n':
        print('No problem, I did not want you to leave')
else:
    print("Your name is not present in the  list {}".format(user_name))
    add_name=input("would you like to get added to the list(Y/N)?").lower()
    if add_name=='y':
        print(known_users)
        known_users.append(user_name)
        print(known_users)
    elif add_name=='n':
        print('No Worries')
# sometime we just want to delete some specific index from our list
# at that time we use del keyword
print('--use del keyword----')
list1=[1,2,3,4,5,6]
del list1[0]
print(list1)
del list1[1:3]
print(list1)

print('--------adding to list-------------')
# we can add list with list only nothing else
# there are two ways to do this 1.append() method 2.add with list
print('---method-one-----')
myList_two=[1,2,3,4]
myList_two=myList_two+[5,6,7]
print(myList_two)
print('-----method-two-----')
myList_two.append(8)
print(myList_two)

'''
We can add strings to list since strings are iterable in nature.
but we cannot do the same with integers as they are not iterable.
below two works in different way!!
'''
myList_two.append('abc')
print(myList_two)
myList_two=myList_two+list('abc')
print(myList_two)

# to add integers we have to first convert it and then append
myList_two=myList_two+list(str(91))
print(myList_two)


print('adding list inside list')
myList_two=myList_two+[[12,13,14,15]]
print(myList_two)
print(myList_two[-1]) # it will print the last element we appended

print('insert element at some particular position')
myList_two.insert(2,100) # donot use myList_two=myList_two.insert(2,100)
print(myList_two)
myList_two.remove(1)
print(myList_two)

