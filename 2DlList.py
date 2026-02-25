#2D LISTS => IS A LIST MADE UP OF LISTS
#YOU CAN MAKE 2D SETS AND TUPPLES

fruits = ["apple", "orange" , "banana" , "coconut"]
vegies =  ["tomatoes", "potatoes" , "carrots" ]
meat =  ["chicken", "fish" , "cow" ]

#EACH LIST REPRESENTS A ROW AND EACH ELEM REP A COLUMN

#THE FOLLOWING IS A 2D LIS
#groceries =[fruits, vegies, meat]
#       OR
groceries = [["apple", "orange" , "banana" , "coconut"],
                ["tomatoes", "potatoes" , "carrots" ],
                 ["chicken", "fish" , "cow" ]]




#printing out the 2d list
print(groceries)
#PRINTING OUT THE ROWS
print(groceries[0]) #['orange', 'orange', 'banana', 'coconut']
print(groceries[1]) #['tomatoes', 'potatoes', 'carrots']
#PRINTING OUT THE ELEMENTS INT THE 2D LIST
print(groceries[0][0]) #apple
print(groceries[0][1]) #orange
#printing the whole list of lists
for row in groceries:
    print(row)

#ITERATE OVER THE ELEMENTS
for row in groceries:
    for col in row:
        print(col , end = "    ")
    print()




