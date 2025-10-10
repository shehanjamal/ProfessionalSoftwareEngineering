import unittest
class Expense:
    def __init__(self, amount, description):
        self.all_expenses = []
        self.amount = amount
        self.description = description

    def add_expense(self, amount=None, description=None):
        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        self.all_expenses.append({"amount": self.amount, "description": self.description})

    def total_expense(self):
        total = sum(expense["amount"] for expense in self.all_expenses)
        return total
    
    def list_expenses(self):
        return self.all_expenses
    
class TestExpenseOperations(unittest.TestCase):
    def test_add_expense(self):
        expense = Expense(50, "Groceries")
        expense.add_expense(50, "Groceries")
        self.assertEqual(len(expense.all_expenses), 1)
        self.assertEqual(expense.all_expenses[0]["amount"], 50)
        self.assertEqual(expense.all_expenses[0]["description"], "Groceries")

    def test_total_expense(self):
        expense = Expense(50, "Groceries")
        expense.add_expense()
        expense2 = Expense(30, "Transport")
        expense2.add_expense()
        total = expense.total_expense() + expense2.total_expense()
        self.assertEqual(total, 80)

    def test_list_expenses(self):
        expense = Expense(50, "Groceries")
        expense.add_expense()
        expense2 = Expense(30, "Transport")
        expense2.add_expense()
        all_expenses = expense.list_expenses() + expense2.list_expenses()
        self.assertEqual(len(all_expenses), 2)
        self.assertEqual(all_expenses[0]["description"], "Groceries")
        self.assertEqual(all_expenses[1]["description"], "Transport")
    

if __name__ == "__main__":
    user_input = input("1.testing or 2.using application: ")
    if user_input == "1":
        unittest.main()
    elif user_input == "2":
        # Run the actual application code
        expense_main = Expense(0, "")
        while True:
            action = input("Enter 'add' to add expense, 'list' to view expenses, 'total' to get all expense or 'quit' to exit: ")
            if action == "add":
                amount = float(input("Enter expense amount: "))
                description = input("Enter expense description: ")
                expense_main.add_expense(amount, description)
                print("")
            elif action == "list":
                all_expenses = expense_main.list_expenses()
                for exp in all_expenses:
                    print(f"Amount: {exp['amount']}, Description: {exp['description']}")
                print("")
            elif action == "total":
                total = expense_main.total_expense()
                print(f"Total Expense: {total}\n")
            elif action == "quit":
                break
            else:
                print("Invalid action. Please try again.")
    else:
        print("Invalid input. Please enter '1' or '2'.")


