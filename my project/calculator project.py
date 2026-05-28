def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "cannot divide by zero"
    else:
        return a/b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("choose your operation:")
num1 =float(input("Enter the first number:"))
num2 =float(input("Enter the second number:"))

if choice == "1":
    print("results:",num1+num2)
elif choice == "2":
    print("results:",num1-num2)
elif choice == "3":
    print("results:",num1*num2)
elif choice == "4":
    print("results:",num1/num2)
else:
    print("invalid choice")