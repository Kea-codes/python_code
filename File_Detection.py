#PYTHON FILE DETECTION

import os #FOR FILE HANDLING

#INITIALIZING THE FILE PATH
file_path = "File_Detection.txt"

#CHECK IF THE FILE EXISTS
if os.path.exists(file_path):
    print("THE FILE EXISTS")

    if os.path.isfile(file_path):#CHECLING IF IT IS A FILE
        print("THAT IS A FILE") 
    elif os.path.isdir(file_path):# CHECKING IF IT IS A FOLDER/DIRACTORY
        print("THAT IS A DIRACTORY")

else:
    print("DOES NOT EXIST")
    

