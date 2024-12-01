#Python Banking Program

def show_balance(balance):
    print("Your balance is $", balance)

def deposit():
    amount = float(input("Enter amount to deposit:"))
    if amount > 0:
        print("Amount deposited successfully")
        return amount

    else:
        print("Invalid amount")

def withdraw(balance):
    amount = float(input("Enter amount to withdraw:"))
    if amount >balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        print("Amount withdrawn successfully")
        return amount
def main():
    balance =0
    is_running=True

    while is_running:
        print("Welcome to the banking program")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice:"))

        if choice==1:
            show_balance(balance)

        elif choice==2:
            balance+=deposit()
        
        elif choice==3:
            balance-=withdraw(balance)

        elif choice==4:
            is_running=False

        else:
            print("Invalid choice")

    print("Thank you, have a nice day")

if __name__=="__main__":
    main()
        

        
