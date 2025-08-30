class employee:
    def __init__(self, name, age, salary):
        self.name = name       # public​
        self._age = age        # protected​
        self.__salary = salary  # private​

    def get_salary(self):
        return self.__salary
    
    def increase_salary(self, amount):
        self.__salary += amount

class Student:
    def __init__(self, name, age):
        self.name = name       # public​
        self._age = age        # protected​
        self.__grade = 'A'     # private​

    def get_grade(self):
        return self.__grade
    
    def reduce_grade(self):
        self.__grade = 'B'

def main():
    s = Student('Ali', 20)
    print(s.name)         # accessible​
    print(s._age)         # discouraged​
    print(s.get_grade())  # correct way​

    print("Reducing grade...")
    s.reduce_grade()
    print(s.get_grade())  # correct way​

    print("")
    e = employee('John', 30, 50000)
    print(e.name)          # accessible​
    e.name = 'Doe'  # allowed​
    print (e.name)

    print(e.get_salary())          # accessible​
    e.__salary = 60000  # won't change the actual salary​
    e.increase_salary(10000)
    print(e.get_salary())


if __name__ == "__main__":
    main()