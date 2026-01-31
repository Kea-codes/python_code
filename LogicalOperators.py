#Logical Operators = They Evaluate Conditions (not , or , and )
#or => at least one condition must be true
#and =>both conditions must be true
#not => the condition must NOT be true

#AND
Pass_Mark = float(input("ENTER YOUR MARK (0-100): " ))
Student_Studied = True 

if Pass_Mark >= 50 and Student_Studied :
    print(f"The student got {Pass_Mark}% and its {Student_Studied} that He studied")
elif Pass_Mark < 50 and Student_Studied :
    print(f"The student got {Pass_Mark}% and its {Student_Studied} that He studied")
