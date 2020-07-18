'''
while loops repeats itself over and over while some conditions is true!!
while condition:
    do what you wnat!!
'''

print('-------Even Numbers----')

number=1
while number<=20:
    if number%2==0:
        print(number)
    number=number+1

print('------Add Name To List----------')
L=[]
while len(L)<3:
    new_name=input("Please add a new name:").strip().capitalize()
    L.append(new_name)
print("Sorry List IS Full !!")
print(L)

print("------Baby Simulator Project------")
from random import choice
questions=["Why is the sky blue?","why is there a face on the moon?"]
questions=choice(questions)
# it will ask a random question from our questions list
answer=input(questions).strip().lower()
while answer!="donot know":
    answer=input("why?").strip().lower()
print("ohh... okay !!")




