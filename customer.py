from user import user

class customer(user):
    def __init__(self):
        super().__init__()
        self.customer_id = None

    def set_id_customer(self,customer_id):
        self.customer_id = customer_id

    def get_id_customer(self):
        return self.customer_id