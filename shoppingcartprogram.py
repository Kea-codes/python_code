#CREATING A SHOPPING CART PROGRAM USING LISTS



foods = []
prices = []
total = 0

#WHILE TRUE CONTINUE/ EXEC THE CODE
while True:
    food_input = input("ENTER THE FOOD ITEMS (q to quit): ")

    if food_input.lower() == "q" : #cancells for both q ans Q
        print("YOUR CART IS EMPTY")
        break 
    else:
        price_input = float(input(f"Enter the price of  {food_input}: $ "))
        foods.append(food_input) #ADDING USER INPUTS IN THE LIST
        prices.append(price_input) #ADDING USER INPUTS IN THE LIST

print("-----YOUR CART------")

for x in foods :
    print(x)

for y in prices :
    total = total + y

print(f"Your Total is : ${total}")