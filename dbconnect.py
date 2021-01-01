import sqlite3

create_Table = "CREATE TABLE IF NOT EXISTS user" \
"(id INTEGER NOT NULL PRIMARY KEY, email TEXT, password TEXT,"\
" nama TEXT, gender TEXT, alamat TEXT, telepon INTEGER);"

insert_customer = "INSERT INTO user "\
"(email, password, nama, gender, alamat, telepon) "\
"VALUES ('wnykhza', 'wnykhza77*', 'Fathorrosi', 'Pria', 'Probolinggo', 085335211419), "\
"('eren', 'eren1234', 'Eren Yeager', 'Pria', 'Paradise', 837283628362),"\
"('naruto', 'naruto1234', 'Uzumaki Naruto', 'Pria', 'Konoha', 18371739173);"

insert_new_customer = "INSERT INTO user (email, password, nama, gender, alamat, telepon) VALUES (?, ?, ?, ?, ?, ?);"

insert_karyawan = "INSERT INTO user (email, password, nama, gender, alamat, telepon) VALUES ('synerfo', 'synerfo1234', 'Rafi Cahya Putra', 'Pria', 'Probolinggo', 081238657974);"

query_update_karyawan = "UPDATE user SET email = ?, password = ?, nama = ?, gender = ?, alamat = ?, telepon = ? WHERE nama = ?"

query_update_custmer = "UPDATE user SET email = ?, password = ?, nama = ?, gender = ?, alamat = ?, telepon = ? WHERE nama = ?"

query_customer = "SELECT email, password, nama, gender, alamat, telepon FROM user;"

query_karyawan = "SELECT email, password, nama, gender, alamat, telepon FROM user;"

query_del_customer = "DELETE FROM user WHERE id=?"

query_login1 = 'SELECT * from user WHERE email="%s" AND password="%s"'


connection = sqlite3.connect("wow.db")

def createUserTable(connection):
    with connection:
        connection.execute(create_Table)

def add_customer(connection):
    with connection:
        connection.execute(insert_customer)


def add_karyawan(connection):
    with connection:
        connection.execute(insert_karyawan)


def add_new_customer(connection, email, password, nama, gender, alamat, telepon):
    with connection:
        connection.execute(
            insert_new_customer, (email, password, nama, gender, alamat, telepon))

def update_karyawan(connection, email, password, nama, gender, alamat, telepon):
    with connection:
        connection.execute(query_update_karyawan, (email, connection, nama, password, nama, gender, alamat, telepon))

def update_customer(connection, email, password, nama, gender, alamat, telepon):
    with connection:
        connection.execute(query_update_custmer, (email, connection, nama, password, nama, gender, alamat, telepon))

def get_customer(connection):
    with connection:
        return connection.execute(query_customer).fetchall()


def get_karyawan(connection):
    with connection:
        return connection.execute(query_karyawan).fetchone()

def del_customer(connection, id):
    with connection:
        return connection.execute(query_del_customer, (id,))

def get_login(connection, email, password):
    with connection:
        connection.execute((query_login1) % (email, password)).fetchall

def login_customer(connection, email, password):
        if get_login(connection, email, password) is not None:
            print ("Welcome")
        else:
            print ("Login failed")