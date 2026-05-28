file = open("data.txt","w")
file.write("Hello World\n")
file.write("My name is David")
file.close()

file = open("data.txt","r")
content = file.readlines()
print(content)
file.close()


file = open("data.txt","a")
file.write("\nYour late")
file.close()

file = open("data.txt","r")
content = file.read()
print(content)
file.close()

file = open("data.txt","a")
file.write("\n goodbye brotherhood")
file.close()

with open("data.txt","r") as file:
    content = file.read()
    print(content)