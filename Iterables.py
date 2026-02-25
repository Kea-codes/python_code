#ITERABLES => AN OBJECT/ COLLECTION THAT CAN RETURN ITS ELEMENTS ONE AT THE TIME
#ALLOWING IT TO BE ITERATED OVER BY A LOOP


#LISTS
numbers = [1,2,3,4,5,6,7,8,9]

for x in numbers:
    print(x, end= " ")
print()

for x in reversed(numbers):
    print(x, end=" ")
print()

#SETS
fruits = {"BANANAS", "APPLES",  "COCONUTS", "KIWI"}

for f in fruits:
    print(f , end =" ")