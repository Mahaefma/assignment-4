from pet import Pet
from mammal import Mammal
from omnivore import Omnivore

class Dog(Mammal, Omnivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        super().__init__(self, legs)
        self.ears = ears


    def __repr__(self) -> str:
        result = '\nSpecies: Dog'
        result = Mammal.__repr__(self) + result #kingdom, class, species info
        result += '\n' + Pet.__repr__(self) #pet
        return result + '\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> str:
        result = 'While the average female dog is physically capable of having two litters per year, this number can vary significantly.'

        print(super().reproduce() + '\n' + result)

    def move(self) -> str:
        print("Dogs have most of the same muscles, tendons, joints, and ligaments as people. All 4 of the dog's limbs are maximized for locomotion, from a steady walk to a rapid sprint.")

    def sleep(self) -> str:
        print('The big difference between dogs and humans is that dogs have short sleep cycles that last just 45 minutes at a time.')

    def eat(self) -> str:
        Omnivore.eat(self)
        print('It is entirely acceptable to feed your dog a pure kibble diet. Or you can mix their diet up with some cooked or raw meat, fish, vegetables and rice.')
        

if __name__ == '__main__':
    d1 = Dog()
    
    print()
    d1.reproduce()

    print()
    d1.sleep()

    print()
    d1.move

    print()
    d1.eat()
