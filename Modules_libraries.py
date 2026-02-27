#MODULES => A FILE CONTAINING CODE YOU WANT TO INCLUDE IN YOUR PROGRAM
#USE 'import' TO INCLUDE A MODULE (BUILT IN )
#useful to braesk up a large program reusable separate files


#print(help("modules"))

#nickname of the module m => alias
import math as m
import Modules_Example as me

print(m.pi) #3.141592653589793

result =me.square(5)
print(f"THE SQUARE OF 5: {result}")