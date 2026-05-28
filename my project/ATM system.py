balance = 1000
pin = "1234"
# check balance
def check_balance():
    print("Your balance is:",balance)

# depisit
def deposit():
    global balance
    amount = int(input("Enter the amount to deposit:"))
    balance+=amount
    print("Deposit successful.New balance is:",balance)

def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw:"))
    if amount > balance:
        print("Insufficient balance")
    else:
        balance-=amount
        print("Withdraw successful.New balance is:",balance)

def change_pin():
    global pin
    pin = input("Enter your previous PIN:")
    new_pin = input("Enter your new PIN:")
    if new_pin == pin:
        print("PIN already taken")
    else:
        print("PIN has been changed successfully")

def atm_menu():

        print("\n===ATM MENU===")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            change_pin()
        elif choice == 5:
            print("Thank you for using ATM system")

        else:
            print("Invalid choice")

print("===WELCOME TO THE ATM SYSTEM===")
user_pin = input("Enter your PIN:")

if user_pin == pin:
    atm_menu()
else:
    print("Invalid PIN")