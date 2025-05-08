from animal import Animal

class Bird(Animal):
    def __init__(self, legs= 0, fins= 0, wings= 2):
        super(). __init__(legs, fins, wings)
        self.wings = wings

    def __repr__(self) -> str:
        return super().__repr__() + "\n Class: Bird"
    
    def __reproduce__(self) -> str:
           return super().__repr__() + "\n Members of this kingdom reproduce by finding a mate of the same species.\
Birds typically reproduce by hatching and incubating their eggs."
    

        