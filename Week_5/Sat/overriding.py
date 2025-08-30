from person import Person

class student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        # self.name = name
        # self.address = address
        # self.age = age
        self.student_id = student_id


    def display(self):
        print("Greeting and felicitations from maestro " + self.name)


def main():
    person1 = Person("Bob", "456 Elm St", 30)
    person1.display()
    student1 = student("Alice", "123 Main St", 20, "S123")
    student1.display()

if __name__ == "__main__": 
    main()