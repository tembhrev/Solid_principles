"""
Open-Closed Principle
Software entities(Classes, modules, functions) should be open for extension, not modification.
"""

class Animal:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        pass
    
animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
            
        elif animal.name == 'mouse':
            print('squeak')
            
"""
The function animal_sound does not conform to the open-closed principle because it cannot be closed against new kinds of animals.
If we add a new animal, Snake, We have to modify the animal_sound function.
You see, for every new animal, a new logic is added to the animal_sound function. 
This is quite a simple example. When your application grows and becomes complex, 
you will see that the if statement would be repeated over and over again 
in the animal_sound function each time a new animal is added, all over the application.
"""

animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]

def animal_sound(animals):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')
            
animal_sound(animals)

"""
How do we make it (the animal_sound) conform to OCP?
"""

class Animal:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        pass
    
    def make_sound(self):
        pass

   
class Lion(Animal):
    def make_sound(self):
        return 'roar'
    
class Mouse(Animal):
    def make_sound(self):
        return 'squeak'
    
class Snake(Animal):
    def make_sound(self):
        return 'hiss'
    
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())
 
animals = [
    Lion('lion'),
    Mouse('mouse'),
    Snake('snake')
] 
        
animal_sound(animals)








