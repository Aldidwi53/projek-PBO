class customer():
    def __init__(self,nama,hp,kelamin,email,alamat,password,id_customer):
        self.nama = ""
        self.hp = ""
        self.kelamin = ""
        self.email = ""
        self.alamat = ""
        self.password = ""
    def set_nama(self,nama):
        self.nama = nama

    def get_nama(self):
        return self.nama

    def set_hp(self,hp):
        self.hp = hp

    def get_hp(self):
        return self.hp

    def set_kelamin(self,kelamin):
        self.kelamin = kelamin

    def get_kelamin(self):
        return self.kelamin
    
    def set_email(self,email):
        self.email = email

    def get_email(self):
        return self.email

    def set_alamat(self,alamat):
        self.alamat = alamat

    def get_alamat(self):
        return self.alamat

    def set_password(self,password):
        self.password = password
    
    def get_password(self,password):
        return self.password

    def set_id(self,id_customer):
        self.id_customer = id_customer

    def get_id(self):
        return self.id_customer

if __name__ == "__main__":
    pass