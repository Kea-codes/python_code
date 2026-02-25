#KEY WORD ARGUMENTS= AN ARGUMENT PRECEDED BY AN IDENTIFIER
#HELPS WITH READABILITY
#ORDER OF ARGUMENTS OF THE FUNCTION

def Hello(greeting , tittle , name , surname):
    print(f"{greeting} {tittle} {name} {surname}")

Hello(greeting="HELLO " , tittle="MR-" , name= "KEA " , surname ="MAREMELA" )#HELLO  MR- KEA  MAREMELA
#EVEN IF YOU CHANGE AROUND THE ARGUMENTS, THE OUTPUT WILL BE THE SAME
Hello(greeting="HELLO " , surname ="MAREMELA" , tittle="MR-" , name= "KEA ")#HELLO  MR- KEA  MAREMELA


#A FUCNTION THAT GENERATES A PHONE NUMBER
def gen_phone_num(country_code, area_code , first_dig, last_dig):
    print(f"YOUR PHONE IS: {country_code}-{area_code}-{first_dig}-{last_dig}")



user_country = input("ENTER A COUNTRY CODE: ")
user_area = input("ENTER AN AREA CODE: ")
user_first= input("ENTER A FIRST DIGIT CODE: ")
user_last = input("ENTER A LAST DIGIT CODE: ")

phone = gen_phone_num(country_code=user_country, area_code=user_area, first_dig=user_first, last_dig=user_last)

print("-----------------------------------------")
gen_phone_num(user_country,user_area, user_first, user_last)
print("-----------------------------------------")
