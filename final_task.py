import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create the products table if it doesn't exist
cursor.execute("""CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    quantity INTEGER,
    price REAL
)""")

# Create the sales table if it doesn't exist
cursor.execute("""CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    quantity INTEGER,
    price REAL,
    sale_date DATETIME
)""")

# Function to add a new product
def add_product():
    product_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter cost price: "))
    cursor.execute("""INSERT INTO products VALUES (?, ?, ?, ?)""", (product_id, product_name, quantity, price))
    conn.commit()

# Function to update product details
def update_product():
    product_id = input("Enter product ID to update: ")
    product_name = input("Enter new product name: ")
    quantity = int(input("Enter new quantity: "))
    price = float(input("Enter new cost price: "))
    cursor.execute("""UPDATE products SET product_name = ?, quantity = ?, price = ? WHERE product_id = ?""", (product_name, quantity, price, product_id))
    conn.commit()

# Function to remove a product
def remove_product():
    product_id = input("Enter product ID to remove: ")
    cursor.execute("""DELETE FROM products WHERE product_id = ?""", (product_id,))
    conn.commit()

# Function to display all products
def display_products():
    cursor.execute("""SELECT * FROM products""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to add a new sale
def add_sale():
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter sales price: "))
    sale_date = input("Enter sale date (YYYY-MM-DD): ")

    # Update the product quantity in the products table
    cursor.execute("""UPDATE products SET quantity = quantity - ? WHERE product_id = ?""", (quantity, product_id))

    # Insert the sale record into the sales table
    cursor.execute("""INSERT INTO sales (product_id, quantity, price, sale_date) VALUES (?, ?, ?, ?)""", (product_id, quantity, price, sale_date))

    conn.commit()

# Function to display all sales
def display_sales():
    cursor.execute("""SELECT * FROM sales""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Main program loop
while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Remove Product")
    print("4. Display Products")
    print("5. Add Sale")
    print("6. Display Sales")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_product()
    elif choice == 2:
        update_product()
    elif choice == 3:
        remove_product()
    elif choice == 4:
        display_products()
    elif choice == 5:
        add_sale()
    elif choice == 6:
        display_sales()
    elif choice == 7:
        break

# Close the database connection
conn.close()