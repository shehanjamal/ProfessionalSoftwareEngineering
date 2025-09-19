import sqlite3
import time
import threading


class ConnectDatabase:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance.connection = None
        return cls._instance

    def connect_db(self):
        if self.connection is None:
            self.connection = sqlite3.connect('app.db', check_same_thread=False)
        return self.connection


    def initialize_db(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, item TEXT)''')
        cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
        cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
        cursor.execute("INSERT INTO users (name) VALUES ('Milly')")
        cursor.execute("INSERT INTO users (name) VALUES ('Kelly')")
        cursor.execute("INSERT INTO users (name) VALUES ('Lilly')")
        cursor.execute("INSERT INTO users (name) VALUES ('James')")
        cursor.execute("INSERT INTO users (name) VALUES ('Spade')")
        cursor.execute("INSERT INTO users (name) VALUES ('Eld')")
        cursor.execute("INSERT INTO orders (item) VALUES ('Laptop')")
        cursor.execute("INSERT INTO orders (item) VALUES ('mobile')")
        cursor.execute("INSERT INTO orders (item) VALUES ('Mouse')")
        cursor.execute("INSERT INTO orders (item) VALUES ('Keyboard')")
        cursor.execute("INSERT INTO orders (item) VALUES ('Printer')")
        cursor.execute("INSERT INTO orders (item) VALUES ('Bat')")
        cursor.execute("INSERT INTO orders (item) VALUES ('Cat')")
        cursor.execute("INSERT INTO orders (item) VALUES ('Dog')")
        cursor.execute("INSERT INTO orders (item) VALUES ('Wall')")
        cursor.execute("INSERT INTO orders (item) VALUES ('Tile')")
        conn.commit()

    def close_connection(self):
        conn = self.connect_db()
        conn.close()




class UserService:

    def __init__(self):
        self.db_instance = ConnectDatabase()

    def get_user(self, user_id):
        connection = self.db_instance.connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        for row in result:
            print(row)
        return result
    
class OrderService:
    
    def __init__(self):
        self.db_instance = ConnectDatabase()

    def get_order(self):
        connection = self.db_instance.connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders")
        result = cursor.fetchall()
        for row in result:
            print(row)
        return result
    
def main():
    db_instance = ConnectDatabase()
    db_instance.initialize_db()
    user_service = UserService()
    order_service = OrderService()

    start_time = time.process_time()
    
    user = user_service.get_user(1)
    order = order_service.get_order()

    end_time = time.process_time()

    elapsed_time = end_time - start_time

    print(f"Execution Time: {elapsed_time:.6f} seconds")
    
    print("User:", user)
    print("Order:", order)

if __name__ == "__main__":
    main()