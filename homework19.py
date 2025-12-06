class Shaxs:
    def __init__(self, ism, t_yil):
        self.__ism = ism
        self.__t_yil = t_yil

    def get_ism(self):
        return self.__ism

    def set_ism(self, new_ism):
        self.__ism = new_ism

    def get_t_yil(self):
        return self.__t_yil

    def set_t_yil(self, new_t_yil):
        self.__t_yil = new_t_yil


    odamlar_soni = 0

    def __init__(self, ism, t_yil):
        self.__ism = ism
        self.__t_yil = t_yil
        Shaxs.odamlar_soni += 1


    odamlar_soni = 0

    def __init__(self, ism, t_yil):
        self.__ism = ism
        self.__t_yil = t_yil
        Shaxs.odamlar_soni += 1

    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni


shaxs1 = Shaxs('sarvar',2009)
shaxs2 = Shaxs('Ali',2008)

print(shaxs1.odamlar_soni)
print(shaxs1.get_ism()d
print(shaxs1.get_t_yil())
print(shaxs2.odamlar_soni)
print(shaxs2.get_ism())
print(shaxs2.get_t_yil())




