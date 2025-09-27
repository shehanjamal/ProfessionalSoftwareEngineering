
import sqlite3
import sys

DB_NAME = "cars.db"

MENU = (
    "\nCar Rental System"
    "\n1. Add Car"
    "\n2. List Cars"
    "\n3. Remove Car"
    "\n4. Search Car"
    "\n5. Update Car"
    "\n6. Exit"
    "\nChoose: "
)

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS cars (
            plate TEXT PRIMARY KEY,
            car_type TEXT NOT NULL,
            year INTEGER NOT NULL CHECK(year >= 1886)
        )
        """
    )
    conn.commit()
    conn.close()

def add_car(plate, car_type, year):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO cars (plate, car_type, year) VALUES (?, ?, ?)",
            (plate.strip().upper(), car_type.strip(), int(year)),
        )
        conn.commit()
        print(f"Car {plate} added.")
    except sqlite3.IntegrityError:
        print("❌ Car with this plate already exists!")
    finally:
        conn.close()

def list_cars():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT plate, car_type, year FROM cars ORDER BY plate")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("(no cars found)")
        return
    print("\nPlate\tType\tYear")
    print("-"*28)
    for plate, ctype, year in rows:
        print(f"{plate}\t{ctype}\t{year}")

def remove_car(plate):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM cars WHERE plate = ?", (plate.strip().upper(),))
    conn.commit()
    if cur.rowcount > 0:
        print(f"Car {plate} removed.")
    else:
        print("❌ No car found with that plate.")
    conn.close()

def search_car(plate):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT plate, car_type, year FROM cars WHERE plate = ?", (plate.strip().upper(),))
    row = cur.fetchone()
    conn.close()
    if row:
        print("\nPlate\tType\tYear")
        print("-"*28)
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
    else:
        print("❌ No car found with that plate.")

def update_car(plate, new_type=None, new_year=None):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT plate FROM cars WHERE plate = ?", (plate.strip().upper(),))
    if cur.fetchone():
        if new_type:
            cur.execute("UPDATE cars SET car_type = ? WHERE plate = ?", (new_type.strip(), plate.strip().upper()))
        if new_year:
            cur.execute("UPDATE cars SET year = ? WHERE plate = ?", (int(new_year), plate.strip().upper()))
        conn.commit()
        print(f"Car {plate} updated.")

    else:
        print("❌ No car found with that plate.")
    conn.close()

def main():
    create_table()
    while True:
        try:
            choice = input(MENU).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if choice == "1":
            plate = input("Plate: ").strip().upper()
            car_type = input("Type: ").strip()
            try:
                year = int(input("Year: ").strip())
            except ValueError:
                print("Year must be a number.")
                continue
            add_car(plate, car_type, year)
        elif choice == "2":
            list_cars()
        elif choice == "3":
            plate = input("Plate: ").strip().upper()
            remove_car(plate)
        elif choice == "4":
            plate = input("Plate: ").strip().upper()
            search_car(plate)
        elif choice == "5":
            plate = input("Plate of the car to update: ").strip().upper()
            new_type = input("New Type (leave blank to keep current): ").strip()
            new_year_input = input("New Year (leave blank to keep current): ").strip()
            new_year = int(new_year_input) if new_year_input else None
            update_car(plate, new_type if new_type else None, new_year)
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
