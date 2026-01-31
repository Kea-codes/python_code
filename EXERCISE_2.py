import math

#CALCULATE THE CIRCUMFERENCE OF A CIRCLE
# C = PI* DIAMETER , OR 2*PI*RADIUS

radius = 5
Cir_R = 2* math.pi * radius
print(f"The Circumference of a Circle with rad {radius} is {Cir_R}")

diameter = 5
Cir_D = math.pi * diameter
print(f"The Circumference of a Circle with diameter {diameter} is {Cir_D}")

#********************************

print()
print("****************************************")
print()

#PROMT THE USER TO ADD THEIR OWN VALUES TO CALCULATE THE CIRCUM..
print("Calculating the Circumference of a Circle")
user_input = float(input("INPUT THE NUMBER OF A RADIUS: ")) #MUST BE A FLOAT
user_Calculates= 2* math.pi * user_input
print(f"User's circumference of the circle of rad {user_input} is = {user_Calculates}")

#********************************

print()
print("****************************************")
print()

#CALCULATING THE HYPOTENUSE OF THE TRIANGLE BUT GETTING THE VALUES FROM THE USER
print("Calculating the Hypotenuse side of a triangle")
#PROMT THE USER TO ENTER THE VALUE OF AND A AND B
# HYPOTENUSE^2 = A^2 + B^2

A = float(input("INPUT THE NUMBER OF SIDE A: ")) 
B = float(input("INPUT THE NUMBER OF SIDE B: "))

#CALCULATING THE HYPOTENUSE
H = math.sqrt((A**2) + (B**2))
print(f"side A is {A} and B is {B} , then the Hypotenuse = {H}")





