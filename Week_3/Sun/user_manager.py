from database import create_connection
import sqlite3



def add_student(stu_name, stu_addrs):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO student (stu_name, stu_addrs) VALUES (?, ?)", (stu_name, stu_addrs))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_student(stu_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student WHERE stu_name LIKE ?", ('%' + stu_name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")



def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
