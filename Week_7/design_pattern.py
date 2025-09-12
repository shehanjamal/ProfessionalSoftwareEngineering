import sqlite3
import time

def initialize_db():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, item TEXT)''')
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO orders (item) VALUES ('Laptop')")
    conn.commit()
    conn.close()

class UserService:
    def get_user(self, user_id):
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result
    
class OrderService:
    def get_order(self, order_id):
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
        result = cursor.fetchone()
        conn.close()
        return result
    
def main():
    initialize_db()
    user_service = UserService()
    order_service = OrderService()

    start_time = time.process_time()
    
    user = user_service.get_user(1)
    order = order_service.get_order(1)

    end_time = time.process_time()

    elapsed_time = end_time - start_time

    print(f"Execution Time: {elapsed_time:.6f} seconds")
    
    print("User:", user)
    print("Order:", order)

if __name__ == "__main__":
    main()
