# Python writing files (.txt , .json, .csv)

#create a 2d data sstructure of employees

import csv

employees = [["NAME", "AGE", "JOB"] ,
            ["KAM", 30 , "COOK"], 
            ["GIZ", 33, "UNEMPLOYED"],
            ["MATSU", 30, "MANAGER"]]

file_path= "C:/Users/keamo/Downloads/GitHub_Repo/python_code/output3.csv"

# for the csv file to not make newline after every row
# make the newline to be an empty charater when opening the file
with open(file_path, "w", newline="") as file3:
    writer = csv.writer(file3)
    for row in employees:
         writer.writerow(row) # WRITING TO EVERY ROW OF THE CSV FILE
    print (f"csv file '{file_path}' was created")