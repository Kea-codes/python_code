#NESTED LOOP => LOOP WITHIN ANOTHER LOOP (INNER AND OUTER LOOP)
# OUTER LOOP:
#    INNER LOOP:

#IT PRINT 1 TO 4 , 4 TIMES
for x in range(4):
    for y in range(1,5):
     print(y, end = " ")
    print()

#MAKING A RECTANGLE 
rows = int(input("ENTER THE NUMBER OF ROWS: "))
cols = int(input("ENTER THE NUMBER OF COLUMNS: "))

for x in range(rows):
    for y in range(cols):
        print(y, end = " ")
    print(" ")
    