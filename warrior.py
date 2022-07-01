from enum import Enum
from Vida import Vida
class Tipos_de_guerrero(Enum):
    Boxeador = 0
    Gladiador = 1
    UFC = 2
    MMA = 3

class Tipos_de_ataque(Enum):
    Puñetazo = 4
    Patada = 6
    Codazo = 8
    Espada = 10


class Warrior(Vida):
    def __init__(self, tipo, arma, salud, ataque, defensa):
        # Generamos excepciones en caso de que el formato introducido en el constructor sea incorrecto
        #if type(tipo) != Tipos_de_guerrero or type(arma) != Tipos_de_ataque:
            #raise TypeError("El formato introducido es incorrecto")

        if type(salud) != int or type(ataque) != int or type(defensa) != int:
            raise TypeError("El formato introducido es incorrecto")

        if not 1 <= salud <= 100:
            raise ValueError("La salud del luchador no puede ser menor que 1 ni mayor que 100")

        if not 1 <= defensa <= 10:
            raise ValueError('La defensa del luchador debe tener un valor entre 1 y 10')
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

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_arma(self, arma):
        self.__arma = arma

    def set_salud(self, salud):
        self.__salud = salud

    def set_ataque(self, ataque):
        self.__ataque = ataque

    def set_defensa(self, defensa):
        self.__defensa = defensa

    def is_alive(self):
        return self.is_vivo(self.__salud)

    def fight_attack(self, warrior_to_attack):
        e =None

    def fight_defense(self, points_of_damage):
        e = None


tipo_1 = Tipos_de_ataque
tipo_2 = Tipos_de_guerrero
a = Warrior(tipo_2, tipo_1, 10, -2, -3)
