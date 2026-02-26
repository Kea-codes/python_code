#ARBITRARY ARGYMENTS

#  *ARGS => ALLOWS YOU TO PASS MULTIPLE NON-KEY ARGUMENTS
#        => ACTS AS A TUPLE
#  **KWARGS (KEY ARGS) => ALLOWS TOU TO PASS MULTIPLE KEYWORD-ARGS
#        => ACTS AS A DICTIONARY


#-------------------------ARGS------------------------
print("#-------------------------ARGS------------------------")
def add_nums(x,y):
    return print(f"ADDED {x} + {y} = {x+y} ")

add_nums(5,6) #THIS FUNCTION ONLY ADDS 2 NUMBERS

#THE FOLLOWING ADDS MULTIPLE
def add(*nums): #nums IS A TUPLE
    total =0
    for num in nums:
        total += num #AUGMENT THE TOTAL BY ARG
    return print(f"THE TOTAL IS: {total}")

add(1,2,3,4,5)

#CREATE A FUNCTION TO DISPLAY SOMEONE NAME
def display_name(*names):
    for name in names:
        print(name, end = " ")
    print()
    
display_name("KEA", "MAREMELA",  "THE", "G")

#--------------------------KWARGS------------------------
print("#--------------------------KWARGS------------------------")
def prin_adress (**kwargs):
    for key ,value in kwargs.items(): #FOR EVERY KEY VALUE IN THE KWARGS ITEMS
        print(f"{key}: {value}") #PRINTS EVERY KEY VALUE ARGUMENTS

prin_adress(street="1515 RAK SEC", city="RUSTY" ,  provence="NW")
