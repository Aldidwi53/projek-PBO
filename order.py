class Pesan:
    
    def __init__(self, tanggalPesan, status_order):
        self.__tanggalPesan = tanggalPesan
        self.__status_order = status_order

    @property
    def getOrderDate(self):
        pass

    @getOrderDate.getter
    def getOrderDate(self):
        return self.__tanggalPesan