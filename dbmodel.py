import sqlite3

create_model = "CREATE TABLE IF NOT EXISTS model (id INTEGER NOT NULL PRIMARY KEY, nama text , harga integer);"

query_insert_model = "INSERT INTO model (nama, harga) VALUES ('Top knot', 30000), ('Buzz cut', 30000), ('Front puff', 25000), ('Short and spiky', 20000), ('Pompadour', 25000), ('Quiff', 30000), ('Line up haircut', 25000);"

query_model = "SELECT * FROM model"

query_del_model = "DELETE FROM model"

class dbmodel:

    connection = sqlite3.connect("wow.db")

    def __init__(self):
        pass

    def create_model_table(self,connection):
        with connection:
            connection.execute(create_model)

    def insert_model(self,connection):
        with connection:
            connection.execute(query_insert_model)

    def get_model(self,connection):
        with connection:
            return connection.execute(query_model).fetchall()

    def del_model(self,connection):
        with connection:
            return connection.execute(query_del_model)

