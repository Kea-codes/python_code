import math
#python compound interest calculator

# A => FINAL AMOUNT
# P => INITIAL AMOUNT
# r => INTEREST RATE
# t => NUMBER OF TIME PERIODS ELAPSED
# n => 100 (makes r/n to be %)

# A = P(1 + r/n)^t

#INITIAL VALUE
P = int(input("ENTER THE VALUE OF P: "))
while P < 0 :
    print("INITIAL INVESTMENT COULD NEVER BE NEGATIVE, TRY AGAIN")
    P = int(input("ENTER THE VALUE OF P: "))

#INVESTMENT RATE
r = int(input("ENTER THE RATE: "))
while r < 0 :
    print("INVESTMENT RATE COULD NEVER BE NEGATIVE, TRY AGAIN")
    r = int(input("ENTER THE INVESTMENT RATE: "))

#INVESTMENT TIME PERIOD
t = int(input("ENTER THE INVESTMENT TIME PERIOD IN YEARS: "))
while t < 0 :
    print("INVESTMENT TIME PERIOD COULD NEVER BE NEGATIVE, TRY AGAIN")
    r = int(input("ENTER THE INVESTMENT TIME PERIOD: "))

# A = P(1 + r/n)^t
A = P * pow((1 + r/100), t)
A = math.ceil(A)
print(f"YOUR INITIAL AMOUNT ${P} , WITH INTEREST RATE {r}% OVER {t} YEARS AMOUTS TO ${A}")