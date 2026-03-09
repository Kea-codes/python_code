# Python writing files (.txt , .json, .csv)

# OUPUTINH THE DATA TO A TXT FILE
txt_data = "I LIKE FOOD"

file_path = "C:/Users/keamo/Downloads/GitHub_Repo/python_code/output1.txt"

# THE TEXT FILE CREATED WILL BE ON THE SAME FILE PATH AS THE PYTHON FILE
# THIS OPENS THE FILE
# AFTER FINISHING WITH THE  FILE
# THE with statement WILL CLOSE THE FILE TO AVOID UNWANTED BEHAVIOURS
# open() => returns the file object
# 1st arg => is the file path
# 2nd arg => is the mode (w = write , x= create a file if it DNE, a= append a file, r =read the file )

#WE CAN ALSO USE A TRY-EXCEPTION BLOCK FOR CATCHING ERRORS

with open(file_path, "w") as file:
    file.write(txt_data) #writing the text data to the file
    print(f"text file '{file_path}' was created")


# --------------SECOND EXAMPLE-----------------

file_path2 = "C:/Users/keamo/Downloads/GitHub_Repo/python_code/output2.text"
employees = ["KAM" , "GIZ" , "GENZU", "MATSU"]

#writing a list to a file need a for-loop

with open(file_path2, "w") as file2:
    for employee in employees:
        file2.write(employee + "\n") #Outputing the employees in a new line to a file
    print(f"text file for employees'{file_path2}' was created") 






