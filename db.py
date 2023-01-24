# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data

import sqlite3 as sql
conn = sql.connect("order_db")
cursor = conn.cursor()

def setupTable():
    sql_file = open("orders.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)

def runQuery(query):
    data = cursor.execute(query).fetchall()
    return data

def createOrder(customer_name, drink, size, extras, price):
    # customer_name = input("Enter your name: ")
    # drink = input("Enter drink of choice: ")
    # size = input("Enter size (small, medium or large): ")
    # extras = input("Extras? (true or false): ")
    # price = input("Enter price: ")
    query = f"INSERT INTO orders (customer_name, drink, size, extras, price) VALUES ('{customer_name}', '{drink}', '{size}', '{extras}', '{price}');"
    runQuery(query)
    return True

def viewAnOrder(id):
    view_query= f"SELECT * FROM orders WHERE order_id = {id}"
    return runQuery(view_query)

def viewAllOrders():
    query = "SELECT * FROM orders;"
    data = runQuery(query)
    return data

def updateOrder(id, table_title, value):
    update_query = f"UPDATE orders SET {table_title} = '{value}' WHERE order_id = '{id}'"
    runQuery(update_query)
    return True

def deleteOrder(id):
    delete_query= f"DELETE * FROM orders WHERE order_id = {id}"
    runQuery(delete_query)
    return True

def deleteAllOrders():
    delete_all_query = f"DELETE * FROM orders;"
    runQuery(delete_all_query)
    return True

def commitChanges():
    conn.commit()

# Uncomment this and run the file once to set up the DB
# setupTable()

commitChanges()
print(viewAnOrder(2))
print("-----------------------------------------")
print(viewAllOrders())