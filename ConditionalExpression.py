#Conditional Expression => is the Oneline shortcut of the IF-ELSE statement
# X if CONDITION else Y

#CHECKING IF THE NUBER ENTERED IS POS OR NEG
num_input = float(input("ENTER A NUM TO CHECK IF POSITIVE OR NEGATIVE: "))
print("POSITIVE " if num_input > 0 else "NEGATIVE ")

#DETERMINING IF THE PERSON IS OLD OR YOUNG
Age = int(input("ENTER YOUR AGE: "))
print("YOU ARE OLD" if Age >=18 else "YOU ARE YOUNG")

user_access = input("ENTER admin OR guest: ")
print("FULL ACCESS" if user_access== "admin" else "LIMITED ACCES")