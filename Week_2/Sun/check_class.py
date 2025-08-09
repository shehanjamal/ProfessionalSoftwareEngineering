class person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return print("Hello, ",self.name)
    
    def greet_person(self,name):
        return print("Hello, ", name)
    
if __name__ == "__main__":
    person1 = person("John")
    person1.greet()  # Output: Hello, John!
    
    person2 = person("Jane")
    person2.greet_person("Jane")  # Output: Hello, Jane!

    person2.greet()  # Output: Hello, Jane!
    person1.greet()  # Output: Hello, John!