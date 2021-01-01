import user
import sqlite3


class Karyawan(user.User):
    def __init__(self, email, password, nama, gender, alamat, telepon):
        super().__init__(email, password, nama, gender, alamat, telepon)