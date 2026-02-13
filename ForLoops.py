#For loops => Executes the code a fixed number of times, 
#          => It also Iterates from a starting point to the ending point

# for counter in range (start, end , step)

#PRINTING FROM 1 TO 10
print("#PRINTING FROM 1 TO 10")
for t in range( 1,11) :
    print(t, end = " ")

print("")
#PRINTING FROM 10 TO 1
print("#PRINTING FROM 10 TO 1")
for c in reversed(range(1,11)):
    print(c , end = " ")

print("")
#PRINTIG FROM 1 TO 10 WITH STEP 2
print("#PRINTIG FROM 1 TO 10 WITH STEP 2")
for x in range( 1,11 , 2) :
    print(x , end = " ")

print("")
#ITERATING THROUGH A STRING
print("#ITERATING THROUGH A STRING") 
CreditCard_num = "1234-5678-9012-3456"
for counter in CreditCard_num :
    print(counter , end = " ")

print("")
#SKIPPING A NUMBER 5 IN THE RANGE
print("#SKIPPING A CERTAIN NUMBER IN THE RANGE")
for s in range(1,11):
    if s == 5 :
        continue
    else :
        print(s , end = " ")

print("")
#BREAK OUT THE LOOP
print("#BREAK OUT THE LOOP")
for B in range(1,11):
    if s == 5 :
        break
    else :
        print(B , end = " ")



