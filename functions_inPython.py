'''
Functions: It is a organised and reusable code that performs an action or give some result.
'''

def add(x,y):
    sum=x+y
    print("{}+{}={}".format(x,y,sum))

num1=int(input("enter first num"))
num2=int(input("add second num"))
add(num1,num2)

def reverse(word):
    rev_word=word[::-1]
    print(rev_word)

word=input('enter the word you wanna reverse!!')
reverse(word)