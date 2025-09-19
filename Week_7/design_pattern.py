import sqlite3
import time

def initialize_db():
    conn = sqlite3.connect('app.db')
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
    conn.close()

class UserService:
    def get_user(self, user_id):
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        for row in result:
            print(row)
        conn.close()
        return result
    
class OrderService:
    def get_order(self):
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        result = cursor.fetchall()
        for record in result:
            print(record)
        conn.close()
        return result
    
def main():
    initialize_db()
    user_service = UserService()
    order_service = OrderService()

    start_time = time.process_time()
    
    user = user_service.get_user(1)
    order = order_service.get_order()

    end_time = time.process_time()

    elapsed_time = end_time - start_time

    print(f"Execution Time: {elapsed_time:.10f} seconds")
    
    print("User:", user)

if __name__ == "__main__":
    main()
