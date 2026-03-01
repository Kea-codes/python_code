# super() => Function used in a child class to call methods from a parent class (superclass)
#         => Allows you to exyend functionality of the inherited methods

import math

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"IT IS {self.color} and  IS IT FILLED?({self.is_filled})")

class Circle(Shape):
    def __init__ (self, color, is_filled, radius):
        super().__init__(color, is_filled) #calls missing atributtes from parent class
        self.radius = radius
    
    # METHOD OVERIDING 
    def describe(self):
        print(f"THE AREA OF THE CIRCLE IS : {2*math.pi*pow(self.radius,2)}")


class Square(Shape):
    def __init__ (self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    
    # METHOD OVERIDING
    def describe(self):
        print(f"THE AREA OF THE SQUARE IS: {pow(self.width,2)}")

class Triangle(Shape):
    def __init__ (self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height =height

    def describe(self):
        print(f"THE AREA OF THE TRIANGLE IS: {(self.width * self.height)/2}")




def main():
    #INSTANTIATE / CREATE OBJECTS
    circle =Circle("RED", True, 5)
    square = Square("BLUE", False, 10)
    triangle = Triangle("GREEN", True, 5,7)

    #PRINTING
    print(f"THE COLOUR OF THE CIRCLE IS {circle.color}")
    print(f"IS THE CIRCLE FILLED: {circle.is_filled}")
    print(f"THE RADIUS IS: {circle.radius}")
    square.describe()
    circle.describe()


if __name__ == '__main__':
    main()



