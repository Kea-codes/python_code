#MEMEBERSHIP OPERATORS => USED TO TEST WHETHER A VALUE OR VARIABLE IS FOUND IN A SEQUENCE
#(STRING , LIST , TUPLE , SET , OR FDICTIONARY)


#CHECK IF THE  STUDENT ISS IN THE LIST
students = {"KEA", "MOSI", "GIZ", "KAM"}
user_student = input("ENTER THE STUDENT YOU ARE LOOKING FOR: ")


if user_student in students:
    print(f"{user_student} IS A STUDENT")
else:
    print(f"{user_student} WAS NOT FOUND")
 
