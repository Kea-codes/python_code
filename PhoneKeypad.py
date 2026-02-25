#CREATING A PHONE KEY PAD WITH A TUPPLE

first_row =(1,2,3)
second_row = (4,5,6)
thrird_row =(7,8,9)
forth_row =("*",0, "#")

keypad = (first_row, second_row, thrird_row, forth_row)

for row in keypad:
    for col in row:
        print(col , end = " ")
    print()