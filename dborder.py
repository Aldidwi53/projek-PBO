import sqlite3
from datetime import datetime

create_order_table = "CREATE TABLE IF NOT EXISTS pesan (id INTEGER NOT NULL PRIMARY KEY, tanggalPesan TEXT, status_order TEXT);"

insert_order = "INSERT INTO pesan (tanggalPesan, status_order) VALUES ('02/12/2020', 'free');"

insert_new_customer = "INSERT INTO pesan (tanggalPesan, status_order) VALUES (?, 'dipesan');"

update_order_status = "UPDATE pesan SET status_order = 'dipesan' WHERE id = ?"

query_order = "SELECT id, tanggalPesan, status_order FROM pesan WHERE status_order = 'free'"

query_sales = "SELECT id, tanggalPesan, status_order FROM pesan WHERE statu_order = 'dipesan'"

query_del_order = "DELETE FROM pesan WHERE id=?"

connection = sqlite3.connect("wow.db")

def createOrderTable(connection):
    with connection:
        connection.execute(create_order_table)


def addOrder(connection):
    with connection:
        connection.execute(insert_order)


def updateStatus(connection):
    with connection:
        connection.execute(update_order_status)


def getOrder(connection):
    with connection:
        return connection.execute(query_order).fetchall()

def getSales(connection):
    with connection:
        return connection.execute(query_sales).fetchall()

def add_new_order(connection, tanggalPesan):
    with connection:
        connection.execute(
            insert_new_customer, (connection, tanggalPesan))

def del_order(connection, id):
    with connection:
        return connection.execute(query_del_order, (id,))


