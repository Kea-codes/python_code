#While Lopp => Executes code WHILE THE CONDITION REMAINS TRUE 

name  = input("ENTER YOUR NAME: ")
while name == "":
    print("YOU DID NOT ENTER TOUR NAME")
    name  = input("ENTER YOUR NAME: ") #WITHOUT THIS , IT WOULD LOOP INFINITLEY
print(f"GOOD DAY {name} ")


Food = input("WHAT FOOD DO YOU LIKE (ENTER q to QUIT): ")
#while the input is not "q" , execute the code
while not Food == "q":
    print(f"YOU LIKE {Food}")
    Food = input("WHAT FOOD DO YOU LIKE (ENTER q to QUIT): ")
print("YOU ENTERED 'q' TO QUIT, BYEEEE!!!!")

num = int(input("ENTER A NUMBER BETWEEN 1 - 10: "))
#WHILE THE NUMBER IS FROM 1 TO 10 , EXECUTE THE CODE
while num < 1 or num > 10:
    print("ENTER A CORRECT NUMBER BETWEEN 1 - 10 ")
    num = int(input("ENTER A NUMBER BETWEEN 1 - 10: "))
print(f"YOUR NUMBER IS {num}")


