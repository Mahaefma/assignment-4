from bird import Bird
from omnivore import Omnivore
from pet import Pet

class parrot(Bird, Omnivore, Pet):

    def __init__(self, legs = 0, fins = 0, wings= 2):
        super(). __init__(legs, fins)
        self.wings = wings
        
    def __repr__(self) -> str:
        result = super(). __repr__() + "\n Species: Parrot" + Pet.__repr__(self) + Omnivore.__repr__(self)
        return result
         

    def eat(self) -> str:
        return super().eat() + "\n l eat both plant and animal matter.\
xMy natural diet includes a variety of foods like seeds,\
nuts, fruits, vegetables, flowers, buds, and insects."

    def __repr__(slef) -> str:
        return super(). reproduce() +  "\n Members of this kingdom reproduce by finding a mate of the same species.\
Birds typically reproduce by hatching and incubating their eggs. Parrots often take a few days to lay a full \
clutch of eggs. This can be as many as three to four eggs."
    
    def move(self) -> str:
        return "print('l can move in various ways. I can fly, walk, climb and even use a unique method\
called beakiation to traverse narrow branches."
    
    def sleep(self) -> str:
        return "Parrots sleep around 10 to 12 hours each night, often tucked under their wings. They may also take naps during the day."
    
    def pet(self) -> str:
        return super().pet()
