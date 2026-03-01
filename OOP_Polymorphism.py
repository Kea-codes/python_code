# POLYMORPHISM => GREEK WORD THAT MEANS TO "HAVE MANY FORMS OR FACES"
# POLY => MANY
# MORPHE => FORM

import abc #LINRARY FOR ABSTRACT METHODS
import math

class Shape(abc.ABC):
    
    @abc.abstractmethod #MAKING THE CLASS ABSTRACT
    def area(self):
        pass

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius
    
    def area(self):
        return 2*math.pi*pow(self.radius,2)

class Square(Shape):
    def __init__(self ,side):
        self.side = side

    def area(self):
        return pow(self.side,2)

class Triangle(Shape):
    def __init__(self,base, height):
        self.height = height
        self.base = base
    
    def area(self):
        return self.base*self.height*0.5

#INSTANTIATING
#circle = Circle() #IHERITS FROM SHAPE, IT IS NOT THE SAME AS SQUARE OR TRIANGLE
#SO ....

#LIST OF ALL SHAPES , THEREFOR IS HAS ALL PROPERTIES OF ALL SHAPES COMBINED
shapes = [Circle(5), Square(3), Triangle(3,2)]
#PRINTING
for i in shapes:
    print(f"{i.area()} cm^2")

