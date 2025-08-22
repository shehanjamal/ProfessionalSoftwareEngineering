from database import create_connection
import sqlite3


class Student:
    def student_menu(self):
        print("\n==== Student Manager ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Delete Student by ID")
        print("5. Exit")

    def add_student(self,stu_name, stu_email, stu_phone, major_id):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT EXISTS(SELECT 1 FROM major WHERE major_id = ?)", (major_id,))
            if not cursor.fetchone()[0]:
                print(" Major ID does not exist.")
                return
        
            cursor.execute("INSERT INTO student (stu_name, stu_email, stu_phone, major_id) VALUES (?, ?, ?, ?)", (stu_name, stu_email, stu_phone, major_id))
            conn.commit()

            print(" User added successfully.")
        except sqlite3.IntegrityError:
            print(" Email must be unique.")
        conn.close()

    def view_students(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def search_student(self,stu_name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE stu_name LIKE ?", ('%' + stu_name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_student(self,student_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE student_id = ?", (student_id,))
        conn.commit()
        conn.close()
        print("🗑️ User deleted.")

class Lecturer:
    def lecturer_menu(self):
        print("\n==== Lecturer Manager ====")
        print("1. Add Lecturer")
        print("2. View All Lecturers")
        print("3. Search Lecturer by Name")
        print("4. Delete Lecturer by ID")
        print("5. Exit")
    
    def add_lecturer(self,lec_name, lec_email, lec_phone):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO lecturer (lec_name, lec_email, lec_phone) VALUES (?, ?, ?)", (lec_name, lec_email, lec_phone))
            conn.commit()
            print(" Lecturer added successfully.")
        except sqlite3.IntegrityError:
            print(" Email must be unique.")
        conn.close()

    def view_lecturers(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lecturer")
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def search_lecturer(self,lec_name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lecturer WHERE lec_name LIKE ?", ('%' + lec_name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def delete_lecturer(self,lecturer_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM lecturer WHERE lecturer_id = ?", (lecturer_id,))
        conn.commit()
        conn.close()
        print("🗑️ Lecturer deleted.")


class Course:
    def course_menu(self):
        print("\n==== Course Manager ====")
        print("1. Add Course")
        print("2. View All Courses")
        print("3. Search Course by Name")
        print("4. Delete Course by ID")
        print("5. Exit")

    def add_course(self,course_name, lec_id, major_id):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT EXISTS(SELECT 1 FROM lecturer WHERE lecturer_id = ?)", (lec_id,))
            if not cursor.fetchone()[0]:
                print(" Lecturer ID does not exist.")
                return
            cursor.execute("SELECT EXISTS(SELECT 1 FROM major WHERE major_id = ?)", (major_id,))
            if not cursor.fetchone()[0]:
                print(" Major ID does not exist.")
                return
            
            cursor.execute("INSERT INTO course (course_name, lecturer_id, major_id) VALUES (?, ?, ?)", (course_name, lec_id, major_id))
            conn.commit()

            print(" Course added successfully.")
        except sqlite3.IntegrityError:
            print(" Course code must be unique.")
        conn.close()

    def view_courses(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def search_course(self,course_name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course WHERE course_name LIKE ?", ('%' + course_name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_course(self,course_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM course WHERE course_id = ?", (course_id,))
        conn.commit()
        conn.close()
        print("🗑️ Course deleted.")

class Major:
    def major_menu(self):
        print("\n==== Major Manager ====")
        print("1. Add Major")
        print("2. View All Majors")
        print("3. Search Major by Name")
        print("4. Delete Major by ID")
        print("5. Exit")

    def add_major(self, major_name):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO major (major_name) VALUES (?)", (major_name,))
            conn.commit()
            print(" Major added successfully.")
        except sqlite3.IntegrityError:
            print(" Major name must be unique.")
        conn.close()

    def view_majors(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM major")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def search_major(self,major_name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM major WHERE major_name LIKE ?", ('%' + major_name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_major(self,major_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM major WHERE major_id = ?", (major_id,))
        conn.commit()
        conn.close()
        print("🗑️ Major deleted.")

class Class:
    def class_menu(self):
        print("\n==== Class Manager ====")
        print("1. Add Class")
        print("2. View All Classes")
        print("3. Search Class by Name")
        print("4. Delete Class by ID")
        print("5. Exit")

    def add_class(self, class_name):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO class (class_name) VALUES (?)", (class_name,))
            conn.commit()
            print(" Class added successfully.")
        except sqlite3.IntegrityError:
            print(" Class name must be unique.")
        conn.close()

    def view_classes(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM class")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def search_class(self,class_name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM class WHERE class_name LIKE ?", ('%' + class_name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_class(self, class_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM class WHERE class_id = ?", (class_id,))
        conn.commit()
        conn.close()
        print("🗑️ Class deleted.")