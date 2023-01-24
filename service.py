# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data

# Not a complete function, but a suggestion of what to do
# def read_by_id(id):
#     order_data = db.query(id)
#     order = order(order_data)
    
#  ---------------------------------------------------------------------
import db

def createOrder(customer_name, drink, size, extras, price):
    data = db.createOrder()
    return data
    # query = f"INSERT INTO orders (customer_name, drink, size, extras, price) VALUES ('{customer_name}', '{drink}', '{size}', '{extras}', '{price}');"
    # db.runQuery(query)
    # return True

def getOneOrder(id):
    data = db.viewAnOrder(id)
    return data
    # view_query= f"SELECT * FROM orders WHERE order_id = {id}"
    # data = db.runQuery(view_query)
    # return data 

def getAllOrders():
    data = db.viewAllOrders()
    return data

def updateOrder(id, table_title, value):
    data = db.updateOrder()
    return data
    # update_query = f"UPDATE orders SET {table_title} = '{value}' WHERE order_id = '{id}'"
    # db.runQuery(update_query)
    # return True

def deleteOrder(id):
    data = db.deleteOrder(id)
    return data
    # delete_query= f"DELETE FROM orders WHERE order_id = {id}"
    # db.runQuery(delete_query)
    # return True

def deleteAllOrders():
    data = db.deleteAllOrders()
    return data
    # delete_all_query = f"DELETE FROM orders;"
    # db.runQuery(delete_all_query)
    # return True   

def commitChanges():
    db.conn.commit()
    
    
# print(getOneOrder(1))
# print("-----------------------------")
# # print(createOrder('satta', 'earl gray tea', 'small', 2, 2.50))
# # commitChanges()
# print(getAllOrders())
# print("-----------------------------")
# print(updateOrder(6, "extras", 1))
# print(getAllOrders())
# commitChanges()
# print("------------------------------")
# print(getAllOrders())