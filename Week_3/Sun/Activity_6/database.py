import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS major (
            major_id INTEGER PRIMARY KEY AUTOINCREMENT,
            major_name TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            stu_name TEXT NOT NULL,
            stu_email TEXT NOT NULL UNIQUE,
            stu_phone TEXT,
            major_id INTEGER,
            FOREIGN KEY (major_id) REFERENCES major(major_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturer (
            lecturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            lec_name TEXT NOT NULL,
            lec_email TEXT NOT NULL UNIQUE,
            lec_phone TEXT
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            lecturer_id INTEGER,
            major_id INTEGER,
            FOREIGN KEY (major_id) REFERENCES major(major_id),
            FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS class (
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT NOT NULL
        )
    ''')

    # Transaction tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_course (
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES student(student_id),
            FOREIGN KEY (course_id) REFERENCES course(course_id),
            PRIMARY KEY (student_id, course_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturer_course (
            lecturer_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id),
            FOREIGN KEY (course_id) REFERENCES course(course_id),
            PRIMARY KEY (lecturer_id, course_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS class_lecturer (
            class_id INTEGER,
            lecturer_id INTEGER,
            FOREIGN KEY (class_id) REFERENCES class(class_id),
            FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id),
            PRIMARY KEY (class_id, lecturer_id)
        )
    ''')    

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_lecturer (
            student_id INTEGER,
            lecturer_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES student(student_id),
            FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id),
            PRIMARY KEY (student_id, lecturer_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS major_lecturer (
            major_id INTEGER,
            lecturer_id INTEGER,
            FOREIGN KEY (major_id) REFERENCES major(major_id),
            FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id),
            PRIMARY KEY (major_id, lecturer_id)
        )
    ''')    


    conn.commit()
    conn.close()
