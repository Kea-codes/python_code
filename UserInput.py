#input() = it is the function used to allow user input from the console
#always returns a string , even if the user types in an integer, use type casting to convert

#ASK THE USER FOR SOME INPUT 
user_name = input("WHAT IS YOUR NAME: ")
#ASK FOR THE USER AGE
user_age = int(input("HOLD ARE YOU: ")) #ONLY ALLOWS (TYPECASTING)

print(f"HELLO! {user_name} , You are {user_age} years old")
