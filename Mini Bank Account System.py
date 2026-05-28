def get_account_file(account_number):
    return f"Account: {account_number}.txt"

def account_exists(account_number):
    file_name = get_account_file(account_number)
    try:
        file = open(file_name,"r")
        file.close()
        return True
    except FileNotFoundError:
        return False

def create_account():
    try:
        account_number = input("Enter new account number: ").strip()
        if account_exists(account_number):
            print("Account already exists")
            return
        file = open(get_account_file(account_number),"w")
        file.write("ACCOUNT CREATED SUCCESSFULLY: \n")
        file.close()

        print("Account created successfully")

    except Exception as e:
        print("Error creating account:",e)

def deposit():
    try:
        account_number = input("Enter  account number: ").strip()
        if not account_exists(account_number):
            print("Account does not exist")
            return

        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Money cannot be negative")
            return
        file = open(get_account_file(account_number),"a")
        file.write(f"DEPOSIT {amount}\n")
        file.close()

        print("Money deposited successfully")

    except ValueError:
        print("Incorrect amount entered")
    except Exception as e:
        print("Error depositing money:",e)

def withdraw():
    try:
        account_number = input("Enter account number: ").strip()
        if not account_exists(account_number):
            print("Account does not exist")
            return
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount cannot be negative")
            return
        balance = calculate_balance(account_number)
        if amount > balance:
            print("Insufficient balance")
            return

        file = open(get_account_file(account_number),"a")
        file.write(f"WITHDRAW {amount}\n")
        file.close()

        print("Money withdrawn successfully")

    except ValueError:
        print("Incorrect amount entered")
    except Exception as e:
        print("Error withdraw money:",e)

def calculate_balance(account_number):
    balance = 0
    try:
        file = open(get_account_file(account_number),"r")
        for line in file:
            parts = line
            if parts[0] == "DEPOSIT":
                balance += float(parts[1])
            elif parts[0] == "WITHDRAW":
                balance -= float(parts[1])
        file.close()
    except Exception as e:
        pass
    return balance

def show_history():
    try:
        account_number = input("Enter account number: ").strip()
        if not account_exists(account_number):
            print("Account does not exist")
            return

        print("\n-----Transaction History-----")
        file = open(get_account_file(account_number),"r")
        for line in file:
            print(line.strip())
        file.close()

        balance = calculate_balance(account_number)
        print("\n-----Balance History-----")
        print("Current Balance:",balance)

    except Exception as e:
        print("Error getting history:",e)

def menu():
    while True:
        print("\n---------BANK ACCOUNT SYSTEM---------")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show history")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_history()
        elif choice == "5":
            print("Thank you for using this program")
            break
        else:
            print("Invalid choice. Please try again")
menu()












                



