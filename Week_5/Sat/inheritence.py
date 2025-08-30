class people:
    def __init__(self, name, age,   address):
        self.name    = name
        self.age     = age
        self.address = address

class student(people):
    def __init__(self, name, age, address, student_id, academic_record):
        super().__init__(name, age, address)
        self.student_id      = student_id
        self.academic_record = academic_record 

class academics(people):
    def __init__(self, name, age, address, academic_id, tax_code, salary):
        super().__init__(name, age, address)
        self.academic_id = academic_id
        self.tax_code    = tax_code
        self.salary      = salary

class general_staff(people):
    def __init__(self, name, age, address, staff_id, tax_code, pay_rate):
        super().__init__(name, age, address)
        self.staff_id = staff_id
        self.tax_code = tax_code
        self.pay_rate = pay_rate

def main():
    student1   = student("Alice", 20, "123 Main St", "S123", {"Math": "A", "Science": "B"})
    academic1  = academics("Dr. Smith", 45, "456 College Ave", "A456", "TX123", 75000)
    staff1     = general_staff("Mr. Brown", 35, "789 University Rd", "G789", "TX456", 20)

    print("Student")
    print("Name:    ", student1.name)
    print("Age:     ", student1.age)
    print("Address: ", student1.address)
    print("ID:      ", student1.student_id)
    print("Records: ", student1.academic_record)
    print("")

    print("Academic")
    print("Name:      ", academic1.name)
    print("Age:       ", academic1.age)
    print("Address:   ", academic1.address)
    print("ID:        ", academic1.academic_id)
    print("Tax Code:  ", academic1.tax_code)
    print("Salary:    ", academic1.salary)
    print("")

    print("General Staff")
    print("Name:     ", staff1.name)
    print("Age:      ", staff1.age)
    print("Address:  ", staff1.address)
    print("ID:       ", staff1.staff_id)
    print("Tax Code: ", staff1.tax_code)

if __name__ == "__main__":
    main()
