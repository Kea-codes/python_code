#Collections => a single varibale that stores multiple values
#LIST [] => odered and changeable, accepst duplicates
#SETS {} => unordered and immutables, No duplicates
#TUPLES () => odered and unchangeable ,allows duplicates


#LISTS 
#FIRST INDEX IS 0
fruits = ["BANANA","APPLE","ORANGE","COCONUT"]
#print out the list 
print(fruits)  #['BANANA', 'APPLE', 'ORANGE', 'COCONUT']
#print out the first index in that list
print(fruits[0]) #BANANA
#print out the first 3
print(fruits[0:3])
#iterate through the list
for x in fruits :
    print(x , end = " ") #BANANA APPLE ORANGE COCONUT
#USE HELP
#print(help(fruits))
#THE LENGTH OF THE LIST
print(f"There are {len(fruits)} elements in the list")
#Checking if the value is in the list
print("APPLE" in fruits) #True
#Add an elem in the list , Use The append() method
fruits.append("PINEAPPLE")
print(f"ADDED PINEAPPLE: {fruits}")
#Remove an element
fruits.remove("APPLE")
print(f"Removed apple: {fruits}") 
#Insert/add elem in the list
fruits.insert(0, "KIWI")#inserting kiwi in the first index
print(f"Inserted kiwi in the first index: {fruits}")
#sorting the list
fruits.sort()
print(fruits) #SORTS THEM IN ALPHABETICAL ORDER
#REVERSTHE LIST
fruits.reverse()
print(fruits)
#returning the index of KIWI
print(f"the index of kiwi is: {fruits.index("KIWI")}")
#clearing the list
fruits.clear()
print(f"Cleared the set:  {fruits} ")

print("********************************************************")

cars = {"benz", "lambo" ,  "bmw" , "vw"}

#Help funtion
#print(help(cars))
#Length of the set
print(f"the length of the set: {len(cars)}")
#Checking if the element is the set
print("vw" in cars) #True
#adding an elemnt 
cars.add("volvo") #added at any index
print(f"added volvo in the set: {cars}")
#removing
cars.remove("vw")
print(f"removing vw : {cars}")
#Popping an elemt (remove first elem)
cars.pop()
print(f"popped out the firt elem: {cars}")

#SAME THING FOR TUPPLES