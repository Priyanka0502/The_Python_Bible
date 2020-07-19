print('-----unpack-arguments-----')
a=[1,2,3,4,5,6]
print(a) # we get a list pop-up = [1, 2, 3, 4, 5, 6]
# We want our output as normal number and for that we will do unpacking
print(*a) #List gets unpacked and we get 1 2 3 4 5 6
'''
What happens now when we unpack arguments is we take each item from an Iterable
data-type like a list and each of those items becomes its own argument to the function.
So,instead of having one big list of five numbers we now have five many arguments. One number each
SO,we can unpack any Iterable data-type before they go into functions. 
This will work for strings as well.
'''
b="abcdef"
print("---Before-Unpacking---:",b)

print("-----After Unpacking----:",*b)

def add(*numbers):
    total=0
    for number in numbers:
        total = total + number
    print(total)
add(1,2,3,4,5,6,7,8,9,10)
'''
What happens is all the arguments  add(1,2,3,4,5,6,7,8,9,10) is passed just as tuple 
and save it in a tuple called numbers. We loop through that tuple and add them all up
Thus, Packing is very useful when we don't know how many arguments will be coming
*-> normal arguments (args)
**->keyword arguments(kwargs)

'''
def about(name,age,like):
    sentence="Meet {},age={},he likes={}".format(name,age,like)
    print(sentence)

dictionary={"name":"Priyanka","age":24,"like":"Book-Reading"}
about(**dictionary) #unpacking  for keyword-arguments
#above code works same as below
about(name="satyam",age=23,like="cricket")

print('-----packing with keyword argument-----')
def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))

foo(priyanka="Female",satyam="male")




