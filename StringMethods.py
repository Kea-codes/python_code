#String => It is an array of characters

name = input("ENTER YOUR NAME: ")

#NUMBER OF CHARCTERS IN THE NAME
numOfCharacters = len(name)
print(f"Number of characters in the name is {numOfCharacters}")

#THE INDEX OF A LETTER IN THE NAME 
indexOfLetter = input("LETTER YOU WANT TO FIND THE INDEX OF: ")
result = name.find(indexOfLetter)
print(f"THE INDEX OF THE LETTER IS {result}")

#CAPITALIZED THE FIRST LETTER OF THE NAME 
capitalized_name = name.capitalize()
print(f"CAPITALIZED NAME : {capitalized_name} ")

#ALL CHARACTERS IN UPPERCASE and LOWERCASE
lowercase_name = name.lower()
uppercase_name = name.upper()
print(f"{name} IN CAPITAL LETTERS : {uppercase_name}  || SMALL LETTERS : {lowercase_name}")

#CHECKING IF THE NAME/STRING IS DIGITS
isdigit_name =  name.isdigit()
print(f"IS {name} DIGITS: {isdigit_name}")
