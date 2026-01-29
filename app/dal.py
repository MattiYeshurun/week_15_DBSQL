from typing import List, Dict, Any
from db import get_db_connection

def get_all_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

conn = get_all_customers()

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    cursor = conn.cursor()
    cursor.execute("SELECT customerName, creditLimit FROM customers WHERE creditLimit < 10000 or creditLimit > 100000;")
    result = cursor.fetchall()
    cursor.close
    return result

def get_orders_with_null_comments():
    """Return orders that have null comments."""
    cursor = conn.cursor()
    cursor.execute("SELECT orderNumber, comments FROM `orders` where comments IS null order by orderDate;")
    result = cursor.fetchall()
    cursor.close
    return result

def get_first_5_customers():
    """Return the first 5 customers."""
    cursor = conn.cursor()
    cursor.execute("SELECT customerName, contactFirstName, contactLastName FROM `customers` order by contactLastName limit 5;")
    result = cursor.fetchall()
    cursor.close
    return result

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) as sum_amount, AVG(amount) as avg_amount, MIN(amount) as min_amount, MAX(amount) as max_amount FROM `payments`;")
    result = cursor.fetchall()
    cursor.close
    return result

def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    cursor = conn.cursor()
    cursor.execute("SELECT E.firstName, E.lastName, O.phone FROM employees AS E INNER JOIN offices AS O ON E.officeCode = O.officeCode;")
    result = cursor.fetchall()
    cursor.close
    return result

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    cursor = conn.cursor()
    cursor.execute("SELECT C.customerName, O.orderDate FROM customers AS C LEFT JOIN orders AS O ON C.customerNumber = O.customerNumber;")
    result = cursor.fetchall()
    cursor.close
    return result

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    cursor = conn.cursor()
    cursor.execute("SELECT C.customerName, SUM(OD.quantityOrdered) FROM customers AS C INNER JOIN orders AS O ON O.customerNumber = C.customerNumber INNER JOIN orderdetails AS OD ON O.orderNumber = OD.orderNumber GROUP BY C.customerName ORDER BY C.customerName;")
    result = cursor.fetchall()
    cursor.close
    return result

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    cursor = conn.cursor()
    cursor.execute("SELECT C.customerName, E.firstName, SUM(P.amount) as sum_amount FROM customers AS C INNER JOIN payments AS P ON C.customerNumber = P.customerNumber INNER JOIN employees AS E ON C.salesRepEmployeeNumber = E.employeeNumber WHERE C.contactFirstName NOT LIKE '%Mu%' OR C.contactFirstName NOT LIKE '%ly%' GROUP BY C.customerName, E.firstName ORDER BY sum_amount DESC;")
    result = cursor.fetchall()
    cursor.close
    return result