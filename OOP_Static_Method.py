# STATIC METHODS => A method that Belong to a class rather than any object from the class (instance)
# USUALLY USED TO GENERAL UTILITY FUNCTIONS

# INSTANCE METHODS => BEST FOR OPERATIONS ON INSTANCE OF THE CLASS (OBJECTS)
#STATIC METHODS = BEST FOR UTILITY FUNCTIONS THAT DO NOT NEED ACCES TO A CLASS DATA

class Employee:

    def __init__(self, name , position):
        self.name =name
        self.position = position
    
    def get_info(self):
        return f"{self.name} => {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Cleaner"]
        return position in valid_positions


# ISNTANTIATING
employee1 = Employee("GIZ", "Cook")
employee2 = Employee("KAM", "Manager")

# WE ACCESS STATIC METHODS WITHOUT CREATING AN OBJECT
print(Employee.is_valid_position("Cook")) #True

# ACCESS CLASS METHODS VIA THE OBJECTS
print(employee1.get_info())
print(employee2.get_info())