# Python reading file (.txt, .json, .csv)

# Creating a file path
# we gonna use the files that we wrote to

File_path = "C:/Users/keamo/Downloads/GitHub_Repo/python_code/input1.txt"

# THE with statement WILL CLOSE THE FILE TO AVOID UNWANTED BEHAVIOURS
# open() => returns the file object
# 1st arg => is the file path
# 2nd arg => is the mode (w = write , x= create a file if it DNE, a= append a file, r =read the file )

# we can use a try-block to catch exceptions

try:
        
    with open(File_path, "r") as file:
        content = file.read()
        print(f"\n{content}") # printing the content
except FileNotFoundError:
    print("The file was not found")
 
