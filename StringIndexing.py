#Indexing => Accessing elements of the sequence using []
# [] => indexing operator
#[start: end : step]
credit_number = "1234-5678-9012-3456"

#PRINT FROM THE 1ST INDEX TO THE 4TH
print(credit_number[0:4]) #OR print(credit_number[:4])

#PRINT FROM THE 5th INDEX TO THE 9TH
print(credit_number[5:9])

#PRINTING OUT EVERY THIRD CHARACTER
print(credit_number[0:19:3]) #OR print(credit_number[::3])

#NEGATIVE INDEXING => GETS THE CHARACTERS FROM THE BACK
print(credit_number[-1]) #6
print(credit_number[-2]) #5
print(credit_number[-3]) #4

#Print Out the last Digits of the Credit card number
newCreditCard_num = "1479-2380-5173-8360"
LastFourDig = newCreditCard_num[-4:] #Negative indexing
print(f"XXXX-XXXX-XXXX-{LastFourDig}")

#REVERSING THE CREDIT CARD NUMBER STRING
Rev_CreditCard_num = credit_number[::-1]
print(f"Reverse Credit Card Number: {Rev_CreditCard_num}")

