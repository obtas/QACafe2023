# The controller acts as the API for the app, in this case it will exist as a terminal based app
# using inputs and if statements to specify what the app should do

# It will run commands from the service file, which in turn uses the DB file to 
# query and create data and will return the data back to the user

import service
import db

def startApp():
    print(menu)
    exit = False
    while not exit:
        choice = input("Please select a choice: ")
        if choice == "1":
            print(createAnOrder())
        elif choice == "2":
            print(readOneOrder())
        elif choice == "3":
            print(readAllOrders())
        elif choice == "4":
            print(updateAnOrder())
        elif choice == "5":
            print(deleteAnOrder())
        elif choice == "6":
            print(deleteAllOrders())
        else:
            exit = True
            db.commitChanges()

def createAnOrder():
    customer_name = input("Enter your name: ")
    drink = input("Enter drink of choice: ")
    size = input("Enter size (small, medium or large): ")
    extras = input("Extras? (1:true or 0:false): ")
    price = input("Enter price: ")
    query = f"INSERT INTO orders (customer_name, drink, size, extras, price) VALUES ('{customer_name}', '{drink}', '{size}', '{extras}', '{price}');"
    db.runQuery(query)
    print("Order created :)")
    return True

def readOneOrder():
    id = input("Please enter order ID to read: ")
    return service.getOneOrder(id)
    
def readAllOrders():
    return service.getAllOrders()

def updateAnOrder():
    order_id = input("Input the order id you would like to update: ")
    table_title = input("input the item you would like to update: ")
    value = input("Input the updated value: ")
    query = f"UPDATE orders SET {table_title} = '{value}' WHERE order_id = '{order_id}'"
    db.runQuery(query)
    print("Order updated :)")
    return True

def deleteAnOrder():
    id = input("Please enter order ID you would like to delete: ")
    return service.deleteOrder(id)

def deleteAllOrders():
    return service.deleteAllOrders()


menu = """
    Welcome to the QA Cafe, what would you like to do? 

    1. Create an order
    2. Read an order
    3. Read all Orders
    4. Update an order
    5. Delete an order
    6. Delete all orders
    """

startApp()
# print(service.getAll())