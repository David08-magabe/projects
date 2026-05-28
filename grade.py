name = input("Enter your name:")

def math ():
    grade = input("Enter your grade:")
    if grade >= "70":
        print("your grade is:A")
    elif grade >= "50":
        print("your grade is:B")
    elif grade >= "40":
        print("your grade is:C")
    elif grade >= "30":
        print("your grade is:D")
    else:
        print("you have failed")

def Physics ():
    grade = input("Enter your grade:")
    if grade >= "70":
        print("your grade is:A")
    elif grade >= "50":
        print("your grade is:B")
    elif grade >= "40":
        print("your grade is:C")
    elif grade >= "30":
        print("your grade is:D")
    else:
        print("you have failed")

def Biology ():
    grade = input("Enter your grade:")
    if grade >= "70":
        print("your grade is:A")
    elif grade >= "50":
        print("your grade is:B")
    elif grade >= "40":
        print("your grade is:C")
    elif grade >= "30":
        print("your grade is:D")
    else:
        print("you have failed")

def average():
    average = (math()+Physic
    print("your average is:",average)

def menu():
    while True:
        print("1.Math")
        print("2.Physics")
        print("3.Biology")
        print("4.Average")
        print("5.Exit")

        choice = input("Enter your choice:")
        if choice == "1":
            math()
        elif choice == "2":
            Physics()
        elif choice == "3":
            Biology()
        elif choice == "4":
            average()
        elif choice == "5":
            print("-------Your final results-----")
            break
        else:
            print("Please enter a valid choice")

menu()
