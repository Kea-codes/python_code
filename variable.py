#PRINTING TO THE CONSOLE
print("STARTING NOW")

#VARIABLES 

#STRINGS =SERIESS OF CHARACTERS 
Firstname = "KAM"
print(Firstname)
Myemail = "KammyKammy@gmail.com"
#Using F-string(Format string)
print(f"Hello {Myemail}")

#INTEGERS = INTEGER NUMBERS
AGE = 25
print(f"YOU ARE: {AGE} YEARS OLD")
Quantity = 25
print(f"YOU ARE BUYING {Quantity} BLICKIES")

#FLOATS = DECIAMAL NUMBERS
price = 99.99
print(f"WE ARE SELLING T SHIRTS FOR ${price}")

#BOOLEAN = TRUE OR FALSE
isStudent = False
name= "KAM"
if isStudent :
    print(f"{name} is a student at UJ")
else :
    print(f"{name} is not a student at UJ")

Temp = True
if Temp: 
    print(f"The temperature is Hot")
else :
    print(f"The temperature is not Hot") 

print()
print("**********************")
print()
    

#CREATING THE NUMBERS GAME
print("GUES THE NUMBER FROM 1 TO 5")

user_input = int(input("CHOOSE A NUMBER: "))

if user_input == 1 or user_input == 3 or user_input == 4:
    print("YOU LOST")
elif user_input == 2 or user_input== 5:
    print("YOU WON")
else :
    print("ENTER THE CORRECT INPUT")