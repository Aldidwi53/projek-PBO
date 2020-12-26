import sqlite3
from customer import customer

create_table = "CREATE TABLE IF NOT EXISTS customer (id INTEGER NOT NULL PRIMARY KEY, nama TEXT, hp TEXT, kelamin TEXT, email TEXT, alamat TEXT, password TEXT);"

insert_table = "INSERT INTO customer (nama, hp, kelamin, email, alamat, password) VALUES (?, ?, ?, ?, ?, ?, ?);"

get_Table = "SELECT * FROM customer"

def connect():
    return sqlite3.connect("projek.db")

def create_customer(connection):
    with connection:
        connection.execute(create_table)

def add_customer(connection, nama, hp, kelamin, email, alamat, password):
    with connection:
        connection.execute(
            insert_table, (nama, hp, kelamin, email, alamat, password))

def get_customer(connection):
    with connection:
        return connection.execute(get_Table).fetchall()

