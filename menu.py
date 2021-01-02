import user
from dbconnect import dbconnect
import dbconnect
import karyawan
import customer
from dbmodel import dbmodel
import dbmodel
import model
from dborder import dborder
import dborder
import sqlite3
from datetime import datetime


menu_awal ="""\n Selamat Datang
Pilih salah satu opsi
1. Sign Up
2. menghapus data user
3. Melihat data user
4. Login
5. melihat model potong
6. booking potong
7. hapus booking
8. melihat booking
9. Exit

Opsi = """

Menu_signup = """Sign Up
"""

Menu_del = """Hapus data User
"""
menu_user = """Data User"""

menu_login = """Login"""

menu_model = """Data Model"""

menu_booking = """Booking"""

menu_del_booking = """delete Booking"""

connection = sqlite3.connect("wow.db")

def menu():
    user1 = dbconnect.dbconnect()
    model1 = dbmodel.dbmodel()
    dborder1 = dborder.dborder()
    user1.createUserTable(connection)
    model1.create_model_table(connection)
    dborder1.createOrderTable(connection)

    a = True
    while a == True:
        b = str(input(menu_awal))
        if b == '1':
            print(Menu_signup)
            nama = input('nama = ')
            telepon = input('telepon = ')
            gender = input('gender = ')
            email = input('email = ')
            alamat= input('alamat = ')
            password = input('password = ')
                
            user1.add_new_customer(connection, email, password, nama, gender, alamat, telepon)
                
            print ('berhasil')

        elif b == '2':
            print(Menu_del)
            id = input('id = ')
            user1.del_customer(connection, id)

        elif b == '3':
            print(menu_user)
            data = user1.get_customer(connection)
            base = ['email','password','nama','gender','alamat','telepon']
            print(base)
            for i in range(len(data)) :
                print (data[i])
        
        elif b == '4':
            print(menu_login)
            email = input('email = ')
            password = input('password = ')
            user1.login_customer(connection,email,password)

        elif b == '5':
            print(menu_model)
            data = model1.get_model(connection)
            base = ['id','nama','harga']
            print(base)
            for i in range(len(data)) :
                print (data[i])

        elif b == '6':
            print(menu_booking)
            tanggalPesan = input('tanggal booking = ')

            dborder1.add_new_order(connection, tanggalPesan)
                
            print ('berhasil')

        elif b == '7':
            print(menu_del_booking)
            id = input('id = ')
            dborder1.del_order(connection, id)

        elif b == '8':
            print(menu_booking)
            data = dborder1.getOrder(connection)
            base = ['id','tanggal','status']
            print(base)
            for i in range(len(data)) :
                print (data[i])

        elif b == '9':
            print('EXIT')
            break


menu()