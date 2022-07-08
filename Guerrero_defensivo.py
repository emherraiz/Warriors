from warrior import *
class Guerrero_defensivo(Warrior):
    def __init__(self, id, tipo, arma, salud, defensa, defensa_especial):
        super().__init__(id, tipo, arma, salud, defensa)
        if not isinstance(defensa_especial, int):
            raise TypeError("El formato introducido es incorrecto")
        if not (11 <= defensa_especial <= 20):
            raise ValueError('La defensa especial debe estar en un rango ente 11 y 20')
        self.__defensa_especial = defensa_especial

    def get_defensa_especial(self):
        return self.__defensa_especial

    def set_defensa_especial(self, defensa_especial):
        if not isinstance(defensa_especial, int):
            raise TypeError("El formato introducido es incorrecto")
        if not (11 <= defensa_especial <= 20):
            raise ValueError('La defensa especial debe estar en un rango ente 11 y 20')
        self.__defensa_especial = defensa_especial
        self.__defensa_especial = defensa_especial

