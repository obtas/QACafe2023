# This file is testing the functions of controller.py, all functions within this file should be tested. 
# Unit tests are not testing the entire app, just this single function
# When testing you should be using a TEST_DB, to easily do this modify the db.py so it is using a new DB
# When testing on a test_db you should automatically reset the DB after testing and populate it with some data before testing

# def test_read_by_id():
#     # Arrange - Variables and values needed for the test
#     test_id = 1
#     result = None
#     expected = Order("test name", "test mocha", False, 1.23)

#     # Act - What you are testing 
#     result = controller.read_by_id(test_id)

#     # Assert - Asserting whether what you assume happens, does happen
#     assert result == expected
    
#  ----------------------------------------------------------------------
from service import *

def test_createAnOrder(mocker):
    # Arrange
    test_data = True
    mocker.patch("db.createOrder", return_value = test_data)
    # customer_name = 'Zico'
    # drink = 'smoothie'
    # size = 'medium'
    # extras = 0
    # price = 2.95
    # result = None
    # expected = ({customer_name}, {drink}, {size}, {extras}, {price})
    
    # Act
    result = createOrder('Zico', 'smoothie', 'medium', 0, 2.95)
    
    # Assert
    assert result == True

def test_getOneOrder():
    # Arrange
    test_id = 1
    test_data = [('Abiodun', 'hot chocolate', 'medium', 0, 2.95)]
    
    # Act
    result = getOneOrder(test_id)
    
    # Assert
    result == test_data
    
def test_getAllOrders():
    # Arrange
    test_data = 
    
    # Act
    
    # Assert