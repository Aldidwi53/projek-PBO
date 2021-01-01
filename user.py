class User:

    def __init__(self, email, password, nama, gender, alamat, telepon):
        self.__email = email
        self.__password = password
        self.__nama = nama
        self.__gender = gender
        self.__alamat = alamat
        self.__phone = telepon

    @property
    def getemail(self):
        pass

    @getemail.getter
    def getemail(self):
        return self.__email

    @property
    def getPassword(self):
        pass

    @getPassword.getter
    def getPassword(self):
        return self.__password

    @property
    def getnama(self):
        pass

    @getnama.getter
    def getnama(self):
        return self.__nama

    @property
    def getGender(self):
        pass

    @getGender.getter
    def getGender(self):
        return self.__gender

    @property
    def getalamat(self):
        pass

    @getalamat.getter
    def getalamat(self):
        return self.__alamat

    @property
    def getPhone(self):
        pass

    @getPhone.getter
    def getPhone(self):
        return self.__phone

    