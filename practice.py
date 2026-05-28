attempts = 3

def check_answer(attempts,number,guess_number):
    attempts = 3
    number = 1000
    if guess_number != number:
        print("your guess is Wrong....! Try again")
        return attempts-1
    else:
        print("your have Won")

guess_number = 0
while guess_number != number:
    print(f"you