# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# s1=student("James",25)
# s2=student("David",20)
# print(f"my name is {s1.name} i am {s1.age} years old")
# print(s2.age)


class Bike:
    name = " "
    gear = 0

bike1 = Bike()
bike1.gear = 1
bike1.name = "motorbike"

print(f"{bike1.name}'s bike is {bike1.gear}")