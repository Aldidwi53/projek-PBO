class Model:
    
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    @property
    def getNama(self):
        pass

    @getNama.getter
    def getNama(self):
        return self.__nama

    @property
    def getHarga(self):
        pass

    @getHarga.getter
    def getHarga(self):
        return self.__harga
