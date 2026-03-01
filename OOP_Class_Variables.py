# class variables => Shared amomg all instances of a class
#                 => Defined outside the constructor
# Allow you to share data among all objects created from that class

class Students:
    
    #CLASS VARIABLES
    Graduation_Date = 2026
    num_Students =0

    #CONSTRUCTOR OF THE CLASS
    #INITIALIZING THE CONSTRUCTOR
    def __init__ (self , name, age):
        self.name = name
        self.age = age
        #IF WE MODIFY THE CLASS VAR, WE USE THE CLASS NAME TO ACCES AND MODIFY THE VAR
        Students.num_Students +=1
    
    
#CREATING AN OBJECT
Student1 = Students("KAM", 24)
Student2 = Students("GIZ", 24)
Student3 = Students("MOSI", 22)

print(f"THE AGE AND NAME OF STUDENT 1: {Student1.age}, {Student1.name}")
print(f"THE AGE AND NAME OF STUDENT 2: {Student2.age}, {Student2.name}")
#ACCESSING THE CLASS VARIABLES VIA THE CLASS NAME ITSELF, NOT VIA OBJECTS
print(f"THE STUDENT'S GARDUATION DATE IS {Students.Graduation_Date}")

print(f"NUMNBER OF STUDENTS: {Students.num_Students}")

