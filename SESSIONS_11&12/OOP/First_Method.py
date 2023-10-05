class greeting:
    message = "Welcome" #Attribute of class
    def greet(self, name): #Self refers to the object thaa has been built when you instance the class
        print(self.message + name)
        return

s = greeting()
s.greet(" Alice")


class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year