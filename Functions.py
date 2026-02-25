import time
import math


#FUNCTIONS = A BLOCK OF REUSABLE CODE, IT takes in ARGUMENTS 

#defining the functin
def happyBday(name , age):
    print(f"HAPPY BIRTH DAY {name}" )
    print(f"You are {age} years old")
    print()


#declearing the function
happyBday("KEA", 45)
happyBday("MOSI", 22)

#defining the functin
def display_invoice(name , salary , due_date):
    print(f"HELLO {name} , HOPE YOU ARE GOOD!")
    print("-----------------------------------")
    print(f"YOUR SALARY IS $ {salary}")
    print("-----------------------------------")
    print(f"IT IS DUE {due_date}")


#declearing the function
display_invoice("KEA", 400000 , "20 FEB 2026")


#defining a function
def add_nums(x,y):
    return x+y

def subtract_nums(x,y):
    return x-y

def multiply_nums(x,y):
    return x*y

def divide_nums(x,y):
    return x/y

print(f" SUBTRACTING: {subtract_nums(5,8)}")
print(f" ADDING: {add_nums(5,8)}")
print(f" MULTIPLYING: {multiply_nums(5,8)}")
print(f" DIVIDING: {divide_nums(5,8)}")

#CREATE A FUNCYION THAT CREATE A FULL NAME 
def create_name(surname, name):
    surname = surname.capitalize()
    name= name.capitalize()
    return surname + " " + name

full_name = create_name("MAREMELA" ,"KEA")
print(f"MY FULL NAME IS: {full_name}")

#DISCOUNT CALCULATION
#promt the user to input the values
def discount_calc(fullprice, discount):
    discounted_amount = fullprice -(fullprice*(discount/100))
    return discounted_amount

user_fullprice = float(input("ENTER THE PRICE OF AN ITEM:$ "))
user_dicount = float(input("ENTER THE DISCOUNT OF THE ITEM: "))

print("-----------------------------------")
print(f"THE DISCOUNT IS: {user_dicount}%")
print(f"THE FULL PRICE IS: {user_fullprice}")
print(f"THE DISCOUNTED AMOUNT IS: $ {discount_calc(user_fullprice, user_dicount)}")
print("-----------------------------------")

#TIME COUNTING FUNCTION
#import time

def count_time(start, end):
    for x in range(start, end):
        print(x)
        time.sleep(1)#COUNT WITH 1 SECOND
    print("DONE COUNTING TIME")

count_time(0,10) 

