#CREATE A BASIC CALCULATOR 

user_operator = input("ENTER THE OPERATOR (+ - * /): ")
first_num = float(input("ENTER THE FIRST NUMBER: "))
second_num = float(input("ENTER THE SECOND NUMBER: "))

if user_operator == "+":
    answer = first_num + second_num
    print(f"THE ANSWER IS: {answer}")
elif user_operator == "*":
    answer = first_num * second_num
    print(f"THE ANSWER IS: {answer}")
elif user_operator == "-":
    answer = first_num - second_num
    print(f"THE ANSWER IS: {answer}")
elif user_operator == "/":
    answer = first_num / second_num
    print(f"THE ANSWER IS: {answer}")
else :
    print(f"{user_operator} is not the correct operator")
