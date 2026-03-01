# @property => DECORATOR USED TO DEFINE A METHOD AS A PROPERTY (IT CAN BE ACCESSED LIKE AN ATTRIBUTE)
# BENEFIT => ADD ADDITIONAL LOGIC WHEN RAED, WRITE OR DECLARE ATTRIBUTES
# GIVES YOU getter, setter and deleter method

class Rectangle:

    def __init__ (self, width, height):
        self._width = width #THE UNDERSCORE IS FOR MAKING THE VAR PRIVATE
        self._height =height

    @property
    def width (self):
        return f"{self._width:0.1f} cm"
    
    @property
    def height (self):
        return f"{self._height:0.1f} cm"
    
    # DECORATOR , SETTING THE WIDTH and HEIGHT
    @width.setter
    def width(self, new_width):
        if new_width >0:
            self.width= new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self,  new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("The height must be greater than 0")


   
rect1 = Rectangle(4,5)

print(f"The width = {rect1.width} , The Height = {rect1.height}")

