from user import user

class karyawan(user):
    def __init__(self):
        super().__init__()
        self.user_id = None

    def set_id_user(self,user_id):
        self.user_id = user_id

    def get_id_user(self):
        return self.user_id
