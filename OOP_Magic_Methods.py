# Magic methods => Dunder methods (double underscore) __init__, __str__ , __eq__
# They are automatically called by many of Pythons's built-in operation
# They allow developeer's to define or customize the behavior of OBJECTS

class Book:

    def  __init__(self,tittle, author, num_pages):
        self.tittle = tittle
        self.author =author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"{self.tittle} by {self.author}"
    
    def __eq__ (self, other):
        return self.tittle == other.tittle and self.author == other.author
    
book1 = Book("THE HABBIT", "KAM1 ", 300)
book2 = Book("WHIPS AND CHAINS", "KAM2 ", 400)
book3 = Book("LONG WALK", "KAM3 ", 300)

# THIS WILL ONLY SHOW THE ADDRESS OF THE OBJECT 
print(book1) #SO WE USE __str__ AS THE TRANSLATION 
print(book1 == book3) #False
print(book1.num_pages < book2.num_pages)#TRUE