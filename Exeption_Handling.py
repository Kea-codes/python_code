# Exception => AN EVENT THAT INTERRUPTS THE FLOW OF THE PROGRAM
# (ZeroDivisionError, TypeError, ValueError)
# 1)try 2)except 3)finally

# try => Try to do the code
# except => Do not do this
# finally => Executes regardless if there is an Exception or not

try:
    number = int(input("ENTER A NUMBER: "))
    print(1/number)
except ValueError:
    print("ENTER A NUMBER")
except ZeroDivisionError:
    print("YOU CANNOT DIVIDE BY 0")
except Exception:
    print("YOU CANNOT DIVIDE BY 0")
finally:
    print("DO SOME CLEAN UP")



