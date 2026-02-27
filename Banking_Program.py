def show_balance():
    print(f"YOUR BALANCE IS {balance}")


def deposit():
    amount = float(input("ENTER AN AMOUNT YPU WANT TO DEPOSIT: "))
    
    if amount < 0:
        print("NOT A VALID AMOUNT:")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("ENTER AN AMOUNT TO WITHDRW: "))
    if amount > balance:
        print("YOU DO NOT HAVE THAT AMOUNT OF MONEY:")
        return 0
    elif amount < 0:
        print("AMOUNT HAS TO BE GREATER THAN 0: ")
        return 0
    else:
        return amount



#--------------MAIN------------
def main():
    balance =0
    is_running = True

    while is_running:
        print("--------------BANKING PROGRAM-----------")
        print()
        print(" 1) SHOW BALANCE")
        print(" 2) DEPOSITE ")
        print(" 3) WITHDRAW")
        print(" 4) EXIT")

        choice = input("ENTER YOUR CHOICE(1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance +=deposit(balance )
        elif choice == '3':
            balance -= withdraw(balance )
        elif choice == '4':
            is_running = False
        else:
            print("INVALID CHOICE")

    print("THANK YOU HAVE A NICE DAY")

if __name__ == '__main__':
    main()