#CREATE A WEIGHT CONVERTER

#PROMT THE USER TO ENTER THE WEIGHT TO BE CONVERTED
#kilograms , grams

print("CONVERT YOUR WEIGHT")

user_units_of_weight = input("Is your weight in grams(g) or Kilograms(Kg): ") 
user_weight = float (input("ENTER YOUR WEIGHT: "))

if user_units_of_weight == "Kg" :
    user_Kg_to_g = user_weight * 1000
    print(f"The User's weight from Kilograms to grams is {user_Kg_to_g} grams")
elif user_units_of_weight == "g" :
    user_g_to_Kg = user_weight/1000
    print(f"The User's weight from grams to kilograms is {user_g_to_Kg} Kilos")
else :
    print(f"{user_units_of_weight} is not the correct unit of weight")
