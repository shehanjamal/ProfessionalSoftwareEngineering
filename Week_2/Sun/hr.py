class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def display_info(self):
        print("Employee Name: ", self.name)
        print("Job Title:     ", self.job_title)
        print("Salary:        ", self.salary)

    def give_raise(self, amount):
        self.salary += amount
        print("New Salary after increase: ", self.salary)

def main():
    employee_one = Employee("John Doe", "Software Engineer", 70000)
    employee_two = Employee("Jane Smith", "Data Scientist", 80000)
    
    exit = True
    while exit:
        user_input = input("Enter '1' to display employee info, '2' to give a raise, or 3 to quit: ")
        print("")
        if user_input == '1':
            print("")
            employee_one.display_info()
            print("")
            employee_two.display_info()
            print("")
            print("")
            
        elif user_input == '2':
            employee_raise = input("Enter '1' to give a raise to Employee One or '2' for Employee Two: ")
            if employee_raise not in ['1', '2']:
                print("Invalid choice. Please enter '1' or '2'.")
                print("")
                continue

            raise_amount = float(input("Enter the raise amount: "))
            if raise_amount <= 0:
                print("Raise amount must be greater than zero.")
                print("")
                continue

            elif type(raise_amount) == int or type(raise_amount) == float:
                if employee_raise == '1':
                    employee_one.give_raise(raise_amount)
                elif employee_raise == '2':
                    employee_two.give_raise(raise_amount)
            
        elif user_input.lower() == '3':
            print("Exiting the program.")
            exit = False

        else:
            print("Invalid input. Please try again. Enter 1 2 or 3.")

        print("")
if __name__ == "__main__":
    main()