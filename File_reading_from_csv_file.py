# Python reading file (.txt, .json, .csv)

# Creating a file path
# we gonna use the files that we wrote to

import csv #READING THE CSV FILE
#---------------------READING CSV FILE-------------------------

#import csv module to read the csv file

file_path2 = "C:/Users/keamo/Downloads/GitHub_Repo/python_code/input2.csv"

with open(file_path2, "r") as file2:
    content2 = csv.reader(file2)
    for row in content2: #reading every row of the csv file
        print(row)