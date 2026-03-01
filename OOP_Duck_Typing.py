# DUCK TYPING => ANOTHER WAY OF ARCHIEBING POLYMORPHISM BESIDE INHERITANCE
# OBJECT MUST HAVE MINIMUM NECCESARY ATTRIBUTES/METHODS
# IF IT LOOKS LIKE A DUCK AND QUACKS LIKE A DUCKS, IT MUST BE A DUCK

class Animal:
    alive =True

class Dog(Animal):
    def speak(self):
        print("WOOF")
    
class Cat(Animal):
    def speak(self):
        print("MEOW")

#LETS HAVE A WAY DIFFERENT CLASS BUT RELATED TO ANIMAL/CAT/DOG CLASS WITH SOME ATTRIBUTES

class Car:
    
    alive = False

    def speak(self):
        print("HONK")


# INSTANTIATE

Animal = [Dog(),Cat(),Car()]

for animal in Animal:
    animal.speak()
    print(animal.alive)
