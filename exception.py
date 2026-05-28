balance = 10000

try:
    amount = int(input("Please enter the amount you want to pay: "))
    if amount > balance:
        raise ValueError("Insufficient balance")

    balance -= amount
    print("Payed successfully")

except ValueError as e:
    print("Error:",e)

finally:
    print("\nBalance:",balance)