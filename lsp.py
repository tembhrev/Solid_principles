"""
Liskov Substitution Principle
A sub-class must be substitutable for its super-class.
The aim of this principle is to ascertain that a sub-class can assume the place of its super-class without errors. 
If the code finds itself checking the type of class then, it must have violated this principle.
Let’s use our Animal example.
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def leg_count(self):
        pass


class Lion(Animal):
    def lion_leg_count(self):
        return 4


class Mouse(Animal):
    def mouse_leg_count(self):
        return 4


class Pigeon(Animal):
    def pigeon_leg_count(self):
        return 2
    
animals = [
    Lion('lion'),
    Mouse('mouse'),
    Pigeon('snake')
]     
    
def animal_leg_count(animals):
    for animal in animals:
        if isinstance(animal, Lion):
            print(animal.lion_leg_count())
        elif isinstance(animal, Mouse):
            print(animal.mouse_leg_count())
        elif isinstance(animal, Pigeon):
            print(animal.pigeon_leg_count())
            
animal_leg_count(animals)



"""
To make this function follow the LSP principle, we will follow this LSP requirements postulated by Steve Fenton:
If the super-class (Animal) has a method that accepts a super-class type (Animal) parameter. 
Its sub-class(Pigeon) should accept as argument a super-class type (Animal type) or sub-class type(Pigeon type).
If the super-class returns a super-class type (Animal). 
Its sub-class should return a super-class type (Animal type) or sub-class type(Pigeon).
Now, we can re-implement animal_leg_count function:
"""


class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        return 4


class Mouse(Animal):
    def leg_count(self):
        return 4


class Pigeon(Animal):
    def leg_count(self):
        return 2
    
animals = [
    Lion('lion'),
    Mouse('mouse'),
    Pigeon('snake')
]     
    
def animal_leg_count(animals):
    for animal in animals:
        print(animal.leg_count())
            
animal_leg_count(animals)


