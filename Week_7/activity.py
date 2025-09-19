import sqlite3
from abc import ABC, abstractmethod
from threading import Lock

class ConnectDatabase:
    _instance = None
    _lock = Lock()

    def __new__(cls):


        if cls._instance is None:
            cls._instance = super(ConnectDatabase, cls).__new__(cls)

        cls._instance.connection =  sqlite3.connect('app.db', check_same_thread=False)
        print("Database connection established.")        
        return cls._instance
    
    def get_connection(self):
        return self.connection
    


    def initialize_db(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS PaymentType (id INTEGER PRIMARY KEY, payment_name TEXT, amount INTEGER)''')
        cursor.execute("INSERT INTO PaymentType (payment_name, amount) VALUES ('CreditCard', 100)")
        cursor.execute("INSERT INTO PaymentType (payment_name, amount) VALUES ('PayPal', 200)")
        cursor.execute("INSERT INTO PaymentType (payment_name, amount) VALUES ('Bank Transfer',300)")
        cursor.execute("INSERT INTO PaymentType (payment_name, amount) VALUES ('CryptoPayment', 400)")
        cursor.execute("INSERT INTO PaymentType (payment_name, amount) VALUES ('GooglePay', 500)")
        conn.commit()

    def close_connection(self):
        conn = self.get_connection()
        conn.close()

#Creditcard, PayPal, Bank Transfer, CryptoPayment, GooglePay
class PaymentFactory:
    @abstractmethod
    def pay(self,database, name):
        pass

class CreditCardPayment(PaymentFactory):

    def pay(self,database, name):
        cursor = database.cursor()
        cursor.execute("SELECT * FROM PaymentType WHERE payment_name=?", (name,))
        result = cursor.fetchone()

        return f"Paying {result[2]} using {result[1]}"
    
class PayPalPayment(PaymentFactory):
    def pay(self,database, name):
        cursor = database.cursor()
        cursor.execute("SELECT * FROM PaymentType WHERE payment_name=?", (name,))
        result = cursor.fetchone()

        return f"Paying {result[2]} using {result[1]}"
    
class BankTransferPayment(PaymentFactory):
    def pay(self,database, name):
        cursor = database.cursor()
        cursor.execute("SELECT * FROM PaymentType WHERE payment_name=?", (name,))
        result = cursor.fetchone()

        return f"Paying {result[2]} using {result[1]}"
    
class CryptoPayment(PaymentFactory):
    def pay(self,database, name):
        cursor = database.cursor()
        cursor.execute("SELECT * FROM PaymentType WHERE payment_name=?", (name,))
        result = cursor.fetchone()

        return f"Paying {result[2]} using {result[1]}"
    
class GooglePayPayment(PaymentFactory):
    def pay(self,database, name):
        cursor = database.cursor()
        cursor.execute("SELECT * FROM PaymentType WHERE payment_name=?", (name,))
        result = cursor.fetchone()

        return f"Paying {result[2]} using {result[1]}"
    
class PaymentProcessor:
    _processors = {
        "creditcard": CreditCardPayment,
        "paypal": PayPalPayment,
        "banktransfer": BankTransferPayment,
        "cryptopayment": CryptoPayment,
        "googlepay": GooglePayPayment,
    }

    @classmethod
    def get_payment_processor(cls, payment_method: str): 
        processor_cls = cls._processors.get(payment_method.lower())
        if processor_cls is None:
            raise ValueError(f"Unknown payment method: {payment_method!r}. ")
        return processor_cls()
    
    def checkout(self, payment_method, database, name):
        processor = self.get_payment_processor(payment_method)
        return processor.pay(database, name)
    
def main():
    db_instance = ConnectDatabase()
    db_instance.initialize_db()
    connection = db_instance.get_connection()
    payment_processor = PaymentProcessor()
    print(payment_processor.checkout("creditcard", connection, "CreditCard"))
    print(payment_processor.checkout("paypal", connection, "PayPal"))
    print(payment_processor.checkout("banktransfer", connection, "Bank Transfer"))
    print(payment_processor.checkout("cryptopayment", connection, "CryptoPayment"))
    print(payment_processor.checkout("googlepay", connection, "GooglePay"))
    db_instance.close_connection()

if __name__ == "__main__":
    main()