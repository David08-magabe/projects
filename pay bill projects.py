import random
names = input("Enter the names separated by comma: ")
name_split = names.split(",")
print(name_split)
length = len(name_split)
random_choice=random.randint(0,length-1)
print(f"{name_split[random_choice]} will pay the bill")