# Class Methods => Allow Operation related to the class itself
# Take (cls) as the parameter, which represents the class itself

class Student:

    count = 0 #COUNTING STUDENT ABJECTS WE CREATE
    total_Average =0

    def __init__ (self, name , average):
        self.name = name
        self.average = average
        Student.count +=1
        Student.total_Average += average
    
    def get_info(self):
        return f"NAME => {self.name} , AVERAGE => {self.average}"
    
    @classmethod
    def get_count(cls):
        return f"TOTAL NUMBER OF STUDENTS: {cls.count}"
    
    @classmethod
    def get_total_ave(cls): #Use cls as a parameter as reference to the class itself
        if cls.count == 0:
            return 0
        else:
            return f"TOTAL AVE: {cls.total_Average / cls.count:0.2f}"


# INSTANTIATING 
Student1 =Student("KAM", 75)
Student2 =Student("GIZ", 82)
Student3 =Student("MATSU", 90)

# PRINTING OUT THE INFO ABOUT THE OBJECTS
print(Student1.get_info())
print(Student2.get_info())
print(Student3.get_info())


# ACCESING THE CLASS METHOD
print(Student.get_count())
print(Student.get_total_ave())








