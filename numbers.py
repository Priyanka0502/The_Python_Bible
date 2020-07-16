'''
Division in python 3.X will always gives us decimal value
1/2=0.5(In python 3)
1/2=0 (In python 2)
float takes 16 byte of memory in python while int takes 14 bytes

modulo operator (%) gives us remainder (5%3=2)

Ordering operations follows BODMAS formula
'''

import random
import math

health=50
print(health)

difficulty=3

potion_health= int((random.randint(25,50))/difficulty)
health=health+potion_health
print(health)

print(math.sqrt(2))
print(math.hypot(3,5))
print(math.log10(1000))
print(math.log2(16))
