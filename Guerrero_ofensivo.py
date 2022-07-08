from warrior import *

class Guerrero_ofensivo(Warrior):
    def __init__(self, id, tipo, arma, salud, defensa, ataque_especial):
        super().__init__(id, tipo, arma, salud, defensa)
        if not isinstance(ataque_especial, int):
            raise TypeError("El formato introducido es incorrecto")
        if not (11 <= ataque_especial <= 20):
            raise ValueError('El ataque especial debe estar en un rango ente 11 y 20')
        self.__ataque_especial = ataque_especial

    def get_ataque_especial(self):
        return self.__ataque_especial

    def set_ataque_especial(self, ataque_especial):
        if not isinstance(ataque_especial, int):
            raise TypeError("El formato introducido es incorrecto")
        if not (11 <= ataque_especial <= 20):
            raise ValueError('El ataque especial debe estar en un rango ente 11 y 20')
        self.__ataque_especial = ataque_especial
        self.__ataque_especial = ataque_especial



