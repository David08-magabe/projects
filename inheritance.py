class Human:
    def __init__(self,name):
        self.num_eyes=1
        self.nose=1
    def eat(self):
        print("I am eating.")
    def drink(self):
        print("I am drining.")

class Male(Human):
    def work(self):
        print("I am working.")
        super().eat()
    def eat(self):
        print("I am eating rice.")
    def __init__(self,name):
        super().__init__(name)
        self.name=name
male1 = Male("name")
print(male1.num_eyes)
# male1.eat()
# male1.drink()
# male1.work()