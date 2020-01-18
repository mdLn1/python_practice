import random

print(random.random())
print(random.randint(10,20))

members = ["brandon","madalin","kamil","greg"]
print(random.choice(members))

class Dice:
    def __init__(self, maxVal):
        self.maxVal = maxVal
    
    def roll(self):
        print(f"({random.choice(range(1,self.maxVal))},{random.randint(1,self.maxVal)})")

dice = Dice(6)
dice.roll()