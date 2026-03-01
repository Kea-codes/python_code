# MULTIPLE INHERITANCE => INHERIT FROM MORE THAN ONE PARENT CLASS
# C(A, B)

# MULTILEVEL INHERITANCE => INHERIT FROM A PARENT WHICH INHERITS FROMM ANOTHER PARENT
# C(B) <- B(A) <- A



# _______ GRAND PARENT CLASS ______

class Animal:

    #CONSTRUCTOR
    def __init__ (self ,name):
        self.name = name

    def eat(self):
        print("THIS ANIMAL EATS! ")
    def sleep(self):
        print("THIS AMIMAL SLEEPS! ")

# ________ PARENT CLASSES ________

class Prey(Animal): # INHERITS FROM ANIMAL
    def flee(self):
        print(f"{self.name} IS FEEING! ")

class Predator(Animal): # INHERITS FROM ANIMAL
    def hunt(self):
        print(f"{self.name} HUNTS! ")

# _______ CHILD CLASSES ______

class Rabbit(Prey): # Inherits from Prey class
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # Multiple inheritance
    pass

#INSTATIATING / CREATING AN OBJECT
rabbit = Rabbit("BUGS")
hawk = Hawk("TONY")
fish = Fish("NEMO")


#INHERITS FROM PARENTS CLASS PREY/ PREDATOR
rabbit.flee()
hawk.hunt()
fish.flee() #fish can also hunt()
#INHERITS AN ATTRIBUTE FROM THE GRAND PARENT CLASS ANIMAL
fish.eat() 
hawk.sleep()




