from enum import Enum
from Vida import Vida
from Tipos_de_armas import Tipos_de_armas
from Tipos_de_guerreros import Tipos_de_guerreros

class Warrior(Vida):

    __list_ids = []
    def __init__(self, id, tipo, arma, salud, ataque, defensa):
        # Generamos excepciones en caso de que el formato introducido en el constructor sea incorrecto
        if type(tipo) != Tipos_de_guerreros or type(arma) != Tipos_de_armas:
            raise TypeError("El formato introducido es incorrecto")

        if type(id) != int or type(salud) != int or type(ataque) != int or type(defensa) != int:
            raise TypeError("El formato introducido es incorrecto")

        if id in Warrior.__list_ids:
            raise ValueError("Ese id ya existe, hay que introducir uno que no exista")

        if not 1 <= salud <= 100:
            raise ValueError("La salud del luchador no puede ser menor que 1 ni mayor que 100")

        if not 1 <= defensa <= 10:
            raise ValueError('La defensa del luchador debe tener un valor entre 1 y 10')

        if not 1 <= ataque <= 10:
            raise ValueError('El ataque del luchador debe tener un valor entre 1 y 10')

        self.__id = id
        Warrior.__list_ids.append(id)

        self.__tipo = tipo
        self.__arma = arma
        self._salud = salud
        self.__ataque = ataque
        self.__defensa = defensa

    def get_id(self):
        return self.__id

    def get_tipo(self):
        return self.__tipo

    def get_arma(self):
        return self.__arma

    def get_salud(self):
        return self._salud

    def get_ataque(self):
        return self.__ataque

    def get_defensa(self):
        return self.__defensa

    def set_arma(self, arma):
        if not isinstance(arma, Tipos_de_armas):
            raise TypeError("El formato introducido es incorrecto")

        self.__arma = arma
        self.set_ataque(arma.value)


    def set_ataque(self, ataque):
        if not isinstance(ataque, int):
            raise TypeError("El formato introducido es incorrecto")

        if not (1 <= ataque <= 10):
            raise ValueError("El ataque del luchador debe tener un valor entre 1 y 10")
        self.__ataque = ataque

    def is_alive(self):
        return self.is_vivo(self._salud)

    def fight_attack(self, warrior_to_attack):
        warrior_to_attack.fight_defense(self.__ataque)

    def fight_defense(self, points_of_damage):
        if not isinstance(points_of_damage, int):
            raise TypeError("El formato introducido es incorrecto")

        print(f'El guerrero {str(self)} recibe un ataque de {points_of_damage} punto de daño')
        if points_of_damage > self.__defensa:
            self._salud -= (points_of_damage - self.__defensa)
            print(f'Ahora tiene {self._salud} puntos de vida')
            if self._salud <= 0:
                self.die()
                print(f'{self.get_tipo().name} a muerto')

        else:
            print('El ataque no le ha afectado')

    def __del__(self):
        Warrior.__list_ids.remove(self.__id)


    def __str__(self):
        return f'{self.get_tipo().name} que lucha con {self.get_arma().name}'

    def __repr__(self):
        return f'{self.__id} - {str(self)}'


