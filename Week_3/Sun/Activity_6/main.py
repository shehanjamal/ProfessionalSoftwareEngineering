from database import create_table
from manager import Student, Lecturer, Course, Major, Class

def menu_user():
    print("\n==== Manager ====")
    print("1. Student")
    print("2. Lecturer")
    print("3. Course")
    print("4. Major")
    print("5. Class")
    print("6. Exit")

def main():
    create_table()
    menu = True
    while menu:
        menu_user()
        sub_menu = True
        choice = input("Select an option (1-5): ")
        if choice == '1':
            while sub_menu:
                student = Student()
                student.student_menu()
                sub_choice = input("Select an option (1-5): ")
                if sub_choice == '1':
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    phone = input("Enter phone: ")
                    major_id = int(input("Enter major ID: "))
                    student.add_student(name, email, phone, major_id)
                elif sub_choice == '2':
                    students = student.view_students()
                    for stu in students:
                        print(stu)
                elif sub_choice == '3':
                    name = input("Enter name to search: ")
                    students = student.search_student(name)
                    for stu in students:
                        print(stu)
                elif sub_choice == '4':
                    student_id = int(input("Enter student ID to delete: "))
                    student.delete_student(student_id)
                elif sub_choice == '5':
                    sub_menu = False
                else:
                    print("Invalid choice, try again.")
            
        elif choice == '2':
            while sub_menu:
                lecturer = Lecturer()
                lecturer.lecturer_menu()
                sub_choice = input("Select an option (1-3): ")
                if sub_choice == '1':
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    phone = input("Enter phone: ")
                    lecturer.add_lecturer(name, email, phone)
                elif sub_choice == '2':
                    lecturers = lecturer.view_lecturers()
                    for lec in lecturers:
                        print(lec)
                elif sub_choice == '3':
                    name = input("Enter name to search: ")
                    lecturers = lecturer.search_lecturer(name)
                    for lec in lecturers:
                        print(lec)
                elif sub_choice == '4':
                    lecturer_id = int(input("Enter lecturer ID to delete: "))
                    lecturer.delete_lecturer(lecturer_id)
                elif sub_choice == '5':
                    sub_menu = False
                else:
                    print("Invalid choice, try again.")

        elif choice == '3':
            while sub_menu:
                course = Course()
                course.course_menu()
                sub_choice = input("Select an option (1-4): ")
                if sub_choice == '1':
                    name = input("Enter course name: ")
                    lec_id = int(input("Enter lecturer ID: "))
                    major_id = int(input("Enter major ID: "))
                    course.add_course(name, lec_id, major_id)
                elif sub_choice == '2':
                    courses = course.view_courses()
                    for crs in courses:
                        print(crs)
                elif sub_choice == '3':
                    name = input("Enter course name to search: ")
                    courses = course.search_course(name)
                    for crs in courses:
                        print(crs)
                elif sub_choice == '4':
                    course_id = int(input("Enter course ID to delete: "))
                    course.delete_course(course_id)
                elif sub_choice == '5':
                    sub_menu = False
                else:
                    print("Invalid choice, try again.")

        elif choice == '4':
            while sub_menu:
                major = Major()
                major.major_menu()
                sub_choice = input("Select an option (1-3): ")
                if sub_choice == '1':
                    name = input("Enter major name: ")
                    major.add_major(name)
                elif sub_choice == '2':
                    majors = major.view_majors()
                    for maj in majors:
                        print(maj)
                elif sub_choice == '3':
                    name = input("Enter major name to search: ")
                    majors = major.search_major(name)
                    for maj in majors:
                        print(maj)
                elif sub_choice == '4':
                    major_id = int(input("Enter major ID to delete: "))
                    major.delete_major(major_id)
                elif sub_choice == '5':
                    sub_menu = False
                else:
                    print("Invalid choice, try again.")

        elif choice == '5':
            while sub_menu:
                class_manager = Class()
                class_manager.class_menu()
                sub_choice = input("Select an option (1-3): ")
                if sub_choice == '1':
                    class_name = input("Enter class name: ")
                    class_manager.add_class(class_name)
                elif sub_choice == '2':
                    classes = class_manager.view_classes()
                    for cls in classes:
                        print(cls)
                elif sub_choice == '3':
                    class_name = input("Enter class name to search: ")
                    classes = class_manager.search_class(class_name)
                    for cls in classes:
                        print(cls)
                elif sub_choice == '4':
                    class_id = int(input("Enter class ID to delete: "))
                    class_manager.delete_class(class_id)
                elif sub_choice == '5':
                    sub_menu = False
                else:
                    print("Invalid choice, try again.")
        elif choice == '6':
            print("Goodbye!")
            menu = False
        else:
            print("Invalid choice, try again.")
        
       

if __name__ == "__main__":
    main()
