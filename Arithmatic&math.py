import math

#ARITHMATIC AND MATH
# E.g += is called The AUGMENTED OPARATOR
#max() min() abs()=> absolute funct , pow() => power func , round() => RoundOff
#import a library math to acces special math funtins and values like pi , e , floor(), ceil(), sqrt()





#ADDITION
balls = 1
balls = balls + 1
print(f" we have {balls} balls")

Students = 1
Students += 1
print(f" we have {Students} students")

#SUBTRACTION
friends = 3
friends = friends - 1
print(f" we have {friends} friends")

#MULTIPLICATION
bottles = 2
bottles = bottles * 2
print(f" we have {bottles} bottles")

#DIVISION 
Cups= 6
Cups = Cups / 2
print(f" we have {Cups} Cups")

#EXPONENTS
exp = 2
exp = exp ** 2
print(f" we have {exp} ")

#MODULAS 
Number = 7
remainder = Number % 2
print(f" we have remainder {remainder} of Number {Number} modulas 2")

#********************************

print()
print("****************************************")
print()

x=3.14
y= 4
z=5
t= -4
#ROUNDOFF
xresult = round(x)
print(f"we are rounding of {x} to {xresult}")

#ABSOLUTE VALUE
tresult = abs(t)
print(f"abdolute value of {t} is {tresult}")

#POWER
yresult = pow(y,2)
print(f" {y} to the power 2 is {yresult}")

#MIN MAX
maxNum = max(x,y,x,t)
minNum = min(x,y,x,t)
print(f"The max number between {x,y,z,t} is {maxNum} ")
print(f"The min number between {x,y,z,t} is {minNum} ")

#********************************

print()
print("****************************************")
print()

#Import math library 

#acces pi number
print(f"pi is equal to {math.pi}")
#access e (Euler number)
print(f"e (Euler number) is equal to {math.e}")

#FLOOR AND CEILING OF THE NUMBER
Eg_Num = 9.9
floor_of_num =math.floor(Eg_Num)
ceiling_of_num =math.ceil(Eg_Num)
print(f"the floor of {Eg_Num} is {floor_of_num} and Ceiling is {ceiling_of_num}")

#SQUARE ROOT OF THE NUMBER
square_root_num = math.sqrt(Eg_Num)
print(f"The square root of {Eg_Num} is {square_root_num}")
