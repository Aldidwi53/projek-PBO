import user

class Customer(user.User):

    def __init__(self, email, password, nama, gender, alamat, telepon):
        super.__init__(email, password, nama, gender, alamat, telepon)
        



