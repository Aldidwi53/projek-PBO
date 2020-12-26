from datetime import date
from customer import customer

class order(customer):
    def __init__(self,status_booking,id_status,waktu_booking,durasi,id_booking,harga,id_order):
        self.status_booking = ""
        self.id_status = None
        self.waktu_booking = None
        self.durasi = None
        self.id_booking = None
        self.harga = None
        self.id_order = None
