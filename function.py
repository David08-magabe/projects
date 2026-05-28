# message = "hello world"
# def greet():
#     print("local:", message)
# greet()
# print(message)

# def student(name="David",age=20):
#     print(f"i am {name} i have {age} years old")
# student()

# count = 0
# def increase_count():
#     global count
#     count += 1
#     print(count)
# increase_count()
# print(count)

#
# def factorial(n):
#     if n == 4:
#         return n
#     else:
#         return 2 * factorial(n+1)
# print(factorial(2))

# name = ("angel muwe").title()
# print(name)

# class Car:
#
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
# c1=Car("Toyota", "Blue")
# c1.color = "Red"
# print(f"my car is {c1.name} and my color is {c1.color}")

class Area:
    def calculate(self,length,width):
        return length*width
obj=Area()
print(obj.calculate(3,4))


