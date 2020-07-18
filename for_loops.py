'''
For-loops: for-loop are made up of a variable and an iterable of some kind
and each round of the for-loop the variable becomes the next value in the iterable.
This allows you to perform an operation on each value in the Iterable
and also makes python for-loops easily expandable !!
'''
print("---even numbers---")
# rangle(1,11)=[1,2,3.....,10]
for number in range(1,11):
    if number%2==0:
        print(number)
print('even numbers in one line')
for number2 in range(2,11,2):
    print(number2)

print('----Find Out Vowels and Consonants----')

vowels=0
consonants=0
word=input("Enter your favourite word")
for letter in word:
    if letter.lower() in "aeiou":
        vowels=vowels+1
    elif letter=="":
        pass
    else:
        consonants=consonants+1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
print('---------------------------------------------')

stud={
        "male":["Satyam","Atul","Syed","Subham"],
        "female":["Priyanka","Nisha","Nikki","Vartika"]
}


for keys in stud.keys():
    for name in stud[keys]:
        if "a" in name or "A" in name:
            print(name)
print('---------------------------------------------')
print('----------------------------------------------')
print('----List Comrehensions--------------')
even_numbers=[x for x in range(2,50) if x%2==0]
print(even_numbers)

words=['Priyanka','Nisha','Satyam']
ans=[[w.upper(),w.lower(),len(w)] for w in words]
print('contains list of each words with its upper and lower case and with length')
print(ans)