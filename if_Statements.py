#if = is the statement that is conditional
#DO something if the condition is true , then do the opposite if the condition is false

#Check if the user can have a credit card depending on by age

#Let the user's age to be an integer
users_age = int(input("INPUTE YOUR AGE: "))

if users_age < 0:
    print("YOU HAVE NOT BEEN BORN YET")
elif users_age >= 18 and users_age <=99 :
    print("YOU CAN APPLY FOR A CREDIT CARD")
elif users_age >=100:
    print("YOU ARE TOO OLD TO GET  A CREDIT CARD")
else :
    print("YOU ARE TOO YOUNG TO GET A CREDIT CARD")


print()
print("*********************************")
print()

#ASK THE USER IF THEY WOULD LIKE ICE CREAM

print("WOULD YOU LIKE ICE CREAM??")
users_answer = input("ENTER YES (Y) OR NO (N) : ")

if users_answer == "Y":
    print("YES!! I WOULD LIKE ICE CREAM")
elif users_answer == "N":
    print("NO!! I WOULD NOT LIKE ICE CREAM")
else :
    print("ENTER THE CORRECT ANSWER")

print()
print("*********************************")
print()

print("ENTER YOUR NAME")
users_name = input("WHAT IS YOUR NAME: ")

if users_name == "":
    print("YOU DID NOT ENTER YOUR NAME")
else :
    print(f"HELLO! {users_name}")