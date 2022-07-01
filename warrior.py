from enum import Enum
class Tipos_de_guerrero(Enum):
    Boxeador = 0
    Gladiador = 1
    UFC = 2
    MMA = 3

class Tipos_de_ataque(Enum):
    Puñetazo = 0
    Patada = 1
    Codazo = 2
    Espada = 3


class Warriors():
    def __init__(self, tipo, arma, salud, ataque, defensa):
        # Generamos excepción en caso de que el formato introducido en el constructor sea incorrecto
        if type(tipo) != Tipos_de_guerrero or type(arma) != Tipos_de_ataque:
            raise TypeError("El formato introducido es incorrecto")

        self.__tipo = tipo
        self.__arma = arma
        self.__salud = salud
        self.__ataque = ataque
        self.__defensa = defensa

    def get_tipo(self):
        return self.__tipo

    def get_arma(self):
        return self.__arma

    def get_salud(self):
        return self.__salud

    def get_ataque(self):
        return self.__ataque

    def get_defenda(self):
        return self.__defensa
