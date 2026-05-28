def converter_menu():
    while True:
     print("********Welcome to converter menu*********")
     print("1. Convert from cm to m")
     print("2. Convert from m to cm")
     print("3. Quit")

     choice = int(input("Enter your choice: "))
     if choice == 1:
         measurement = float(input("Enter measurement value: "))
         meter =measurement/100
         print(f"the converted value is: {meter}m")
     elif choice == 2:
         measurement = float(input("Enter measurement value: "))
         centimeter = measurement*100
         print(f"the converted value is: {centimeter}cm")
     elif choice == 3:
         print("Thank you for using this program")
         break
     else:
         print("Please enter a valid choice")
converter_menu()



