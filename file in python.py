f = open("file.txt","w")
f.write("Hello World\n")
f.write("am python\n")
f.close()

f = open("file.txt","a")
f.write("python is easy")
f.close()
f = open("file.txt","r")
content = f.read()
print(content)
f.close()

