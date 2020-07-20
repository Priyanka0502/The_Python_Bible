'''
classes are templates and when we make instance of that class it is objects
classes are made up of:
1. variables also know as states
2. Functions which are known as methods
'''

class Pound:
    value=1.00
    colour="gold"
    num_edges=1
    diameter=22.5 #mm
    thickness=3.15 #mm
    heads=True

coin1=Pound()
print(coin1)
print('colur of coin1 =',coin1.colour)
coin2=Pound()
coin2.colour="Green"
print('colur of coin2 =',coin2.colour)

print('--------------------------------------------------------')
import  random
class pound_new:
    def __init__(self,rare=False):
        self.rare=rare
        if self.rare:       #  -->> same as if self.rare==True:
            self.value=1.25
        else:
            self.value=1.00

        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5  # mm
        self.thickness = 3.15  # mm
        self.heads = True
    def rust(self):
        self.colour='greenish'

    def clean(self):
        self.colour='gold'

    def flips(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.heads
    #destructor
    def __del__(self):
        print('coin spent!!')


coin_one=pound_new(rare=True)
coin_two=pound_new()
print('value of coin1=',coin_one.value)
print('value of coin2=',coin_two.value)
print(coin_one.colour)
coin_one.rust()
print(coin_one.colour)
coin_one.flips()
print(coin_one.heads)
coin_one.flips()
print(coin_one.heads)
del coin_one

#print(coin_one.heads) ---->>>  we will get error after since coin_one is deleted




