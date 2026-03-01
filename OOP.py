#OBJECT ORIENTED PROGRAMMING

# OBJECT => A BUNDLE OF RELATED ATTRIBUTES(VARIABLES) AND METHODS(FUNCTIONS)
# METHOD => A FUNTION INSIDE OF A CLASS
# YOU NEED A CLASS TO CREATE MANY OBJECTS

# CLASS => (BLUEPRINT) USED TO DESIGN THE STRUCTURE AND LAYOUT OF AN OJECT

class car:
    
    #CONSTRUCTOR METHOD
    #SELF => MEANS THE OBJECT WE ARE CREATING RIGHT NOW!(CAR)
    def __init__ (self, model, year , color , for_sale):
        #IS THE SAME AS this.variable IN JAVA
        self.model = model 
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"YOU ARE DRIVING A {self.color} {self.model}")
    
    def stop(self):
        print(f"YOU ARE STOPING A {self.color} {self.model}")
       

# OBJECTS
car1 = car("MUSTANG", 2025, "RED", True)
car2 = car("BMW", 2026, "BLUE", False)
car3 = car("BENZ", 2024, "GREEN", True)

# MAIN FUNCTION
def main():

    print("------------------------------------")
    print(f"the Model of the car is : {car1.model}")
    print(f"The year of the car: {car1.year}")
    print(f"The color of the car: {car1.color}")
    print(f"Is the car for sale?: {car1.for_sale}")
    print("------------------------------------")
    print(f"the Model of the car is : {car2.model}")
    print(f"The year of the car: {car2.year}")
    print(f"The color of the car: {car2.color}")
    print(f"Is the car for sale?: {car2.for_sale}")
    print("------------------------------------")
    print(f"the Model of the car is : {car3.model}")
    print(f"The year of the car: {car3.year}")
    print(f"The color of the car: {car3.color}")
    print(f"Is the car for sale?: {car3.for_sale}")
    print("------------------------------------")
    
    #ACCESSING THE METHODS FOR THE CLASS CAR VIA THE OBJECT
    car1.drive()
    car2.stop()
    car3.drive()

if __name__ == '__main__':
    main()
