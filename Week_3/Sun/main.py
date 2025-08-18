from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, add_student, view_students, search_student, delete_student

def menu_user():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")

def menu_student():
    print("\n==== Student Manager ====")
    print("1. Add Student")
    print("2. View All Student")
    print("3. Search User by Student Name")
    print("4. Delete User by ID")
    print("5. Exit")

def main():
    create_table()
    menu_choice = input("Select 1: User or 2: Student : ")
    while True:
        if menu_choice == '1':
            menu_user()
            choice = input("Select an option (1-5): ")
            if choice == '1':
                name = input("Enter name: ")
                email = input("Enter email: ")
                add_user(name, email)
            elif choice == '2':
                users = view_users()
                for user in users:
                    print(user)
            elif choice == '3':
                name = input("Enter name to search: ")
                users = search_user(name)
                for user in users:
                    print(user)
            elif choice == '4':
                user_id = int(input("Enter user ID to delete: "))
                delete_user(user_id)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        elif menu_choice == '2':
            menu_student()
            choice = input("Select an option (1-5): ")
            if choice == '1':
                name = input("Enter name: ")
                email = input("Enter address: ")
                add_student(name, email)
            elif choice == '2':
                users = view_students()
                for user in users:
                    print(user)
            elif choice == '3':
                name = input("Enter name to search: ")
                users = search_student(name)
                for user in users:
                    print(user)
            elif choice == '4':
                user_id = int(input("Enter user ID to delete: "))
                delete_student(user_id)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        else:
            print("Invalid choice, try again.")
       

if __name__ == "__main__":
    main()
