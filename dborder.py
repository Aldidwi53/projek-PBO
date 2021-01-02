import sqlite3
from datetime import datetime

create_order_table = "CREATE TABLE IF NOT EXISTS pesan (id INTEGER NOT NULL PRIMARY KEY, tanggalPesan TEXT, status_order TEXT);"

insert_order = "INSERT INTO pesan (tanggalPesan, status_order) VALUES ('02/12/2020', 'free');"

insert_new_order = "INSERT INTO pesan (tanggalPesan, status_order) VALUES (?, ?);"

query_order = "SELECT * FROM pesan"

query_sales = "SELECT id, tanggalPesan, status_order FROM pesan WHERE statu_order = 'dipesan'"

query_del_order = "DELETE FROM pesan WHERE id=?"

query_del_all_order = "DELETE FROM pesan"

class dborder:

    connection = sqlite3.connect("wow.db")

    def __init__(self):
        pass

    def createOrderTable(self,connection):
        with connection:
            connection.execute(create_order_table)


    def addOrder(self,connection):
        with connection:
            connection.execute(insert_order)

    def getOrder(self,connection):
        with connection:
            return connection.execute(query_order).fetchall()

    def getSales(self,connection):
        with connection:
            return connection.execute(query_sales).fetchall()

    def add_new_order(self,connection, tanggalPesan):
        with connection:
            connection.execute(
                insert_new_order, (tanggalPesan,'dipesan'))

    def del_order(self,connection, id):
        with connection:
            return connection.execute(query_del_order, (id,))

    def del_all_order(self,connection):
        with connection:
            return connection.execute(query_del_all_order)

