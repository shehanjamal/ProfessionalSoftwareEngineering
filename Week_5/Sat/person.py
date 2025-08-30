class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def display(self):
        print("Greeting from " + self.name)
