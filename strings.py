'''
String is a bunch of letter and character that are stored together. It is an iterable data-type.
There are 3 ways to define a string:
1. use single quotes : name='Priyanka'
2. use double quotes: name ="Priyanka Jha"
3. when we have a statement that use quotes then we could use quotes above it.
    (it's hot): "it's hot"
    he said,"he is a python tutor" : ' he said,"he is a python tutor" '
4. use triple quotes when you have multiple line:
    ex: use are using triple quotes in this example!

5. # is used to provide comment

Strings are immutable. so unless we overide it i.e., after performing string methods we should  save its value into some variable.
otherwise it will not show the changes we made to it.

The basic slice format is: variable[start:end:step]
'''
name="Priyanka"
print(name)

message='He  said "You look beautiful"'
print(message)

message2='''
abc
asjhk
dbhkj
'''
print(message2)

print('___________________________________________________________________________________________')

# Ask user for name
name=input("What is your name?")
# Ask user for age
age=input("May I know yor age?")
# Ask user for city
city=input("Where do you live?")
# Ask user what they enjoy
hobby=input("What you like to do in your free time?")
# Create output text
string="Your name is {} and you are {}yrs old. You live in {} and like to do {} in your free time"
output=string.format(name,age,city,hobby)
# Print output to screen
print(output)

print('__________________________________________________________________________')
print('cool string methods:')
var1="Priyanka"
print(var1.count("a")) # count() method defined here!!
var2='abcdef'
print(var2.upper())
''' .lower(), .upper(), .title() , .capitalize()  :-> these are some methods which we use to change cases in strings.

    .islower() , .isupper() etc to check if strings are in the given case or not
    
    .index() :-> gives us the position of our str.
    
    .find() and .index() :-> both methods works same but when a substring is not present in find() then it will give "-1" as output
    but for index() :-> it will throw an error.
    So basically .find() is used when we want our program to execute smoothly without error
    
    lstrip() will strip things from left side while rstrip() from right-side
    {we need to provide the sub-str which we wanna strip from our string}
    strip() -> will remove the string from both side of the variable.
    if we donot provide anything then strip methid will remove the spaces which are present in our string
    
'''
print(var2.islower())

var3="0000000000000priyanka00000000000000"
print(var3.lstrip('0')) #priyanka00000000000000

var4 =" hakk0000hakk "
print(var4.strip()) # removed extra spaces from var4

print('_________________________________________________________________________________________________________________-')
print('Slicing of strings:')
# variable_name[start:end:step]
# if start is empty it will start from the begininng.
# if end is empty then it will go to the last index
# step: how many steps we want to take
# for reverse : first index= -1
# https://www.journaldev.com/23584/python-slice-string

var5="abcdefghijklmnopqrstuvwxyz"
print(var5[0:5])
print(var5[6:])
print(var5[::3])
print(var5[::-1]) #reverse a string in a one line
print(var5[25:1:-2])
print(var5[var5.index("abc"):var5.index("def")]) #we can do in this way also


print('_________________________________________________________________')
print("email-program:")
# user provides email address
email=input("enter your email please!!").strip()

# slice-out username.
user_name=email[:email.index("@")]

# slice-out domain name.
domain_name=email[email.index("@")+1:]

# format message
output ="Your username is {} and your domain is {}".format(user_name,domain_name)

print(output)