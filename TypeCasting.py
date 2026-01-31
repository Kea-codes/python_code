
#type casting changes the variable's data type to another

AGE = 25
price = 3.99
name = "KAM"
isPASSED = True

# CHECKING THE TYPE OF THE VARIABLE
print(type(AGE)) #<class 'int'>
print(type(price)) #<class 'float'>
print(type(name)) #<class 'str'>
print(type(isPASSED)) #<class 'str'>

print()
print("***************************************")

#Convert the data types to other data types
AGE=float(AGE)
print(AGE) #25.0

price = int(price) 
print(price) #3

name = bool(name)
print(name) #True , if name was empty character it would be FALSE

isPASSED = str(isPASSED)
print(isPASSED) 

