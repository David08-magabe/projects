def game():
    winning_number = 1000
    total_attempts = 3

    number = input("Guess the number between 0 and 1000: ")
    while number != winning_number:
        total_attempts = total_attempts -1
    if  total_attempts <=0:
        print("out of attempts")
        return
    elif number == winning_number:
        print('"Won"')
game()



         
    
   
        
    