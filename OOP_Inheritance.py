#INHERITANCE => ALLOWS A CLASS TO INHERIT ATTRIBUTES AND METHODS FROM ANOTHER CLASS
#            => HELPS WITH CODE REUSABILITY AND EXTENSIBILITY
#            => CLASS CHILD(PARENT)


#--------------- PARENT CLASS ---------------
class Animal:

    def __init__ (self, name):
        self.name = name
        self.is_Alive = True
    
    def eat(self):
        return print(f"{self.name} IS EATING")
    
    def sleep(self):
        return print(f"{self.name} IS SLEEPING")
    
    
#---------------- CHILD CLASS ----------------
#INHERITS FROM CLASS ANIMAL
class dog(Animal): 
    def speak(self):
        print("WOOF")

class cat(Animal):
    def speak(self):
        print("MEOW")

class mouse(Animal):
    def speak(self):
        print("SQUICKS")

dog = dog("SCOOBY DOO")
cat = cat("GARFIELD")
mouse =mouse("MICKEY")

print(dog.is_Alive)
print(dog.name)
dog.speak()
cat.speak()
#CALLING METHODS VIA OBJECTS
cat.sleep()
mouse.eat()