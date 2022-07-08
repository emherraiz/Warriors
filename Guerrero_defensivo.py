import random
from warrior import Warrior
from Tipos_de_armas import Tipos_de_armas
from Tipos_de_guerreros import Tipos_de_guerreros
class Guerrero_defensivo(Warrior):
    def __init__(self, id, tipo, arma, salud, ataque, defensa, defensa_especial):
        super().__init__(id, tipo, arma, salud, ataque, defensa)
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

    def fight_defense(self, points_of_damage):
        if not isinstance(points_of_damage, int):
            raise TypeError("El formato introducido es incorrecto")
        print(f'El guerrero {str(self)} recibe un ataque de {points_of_damage} punto de daño')

        usar_habilidad = random.randint(0, 1)
        if usar_habilidad:
            if points_of_damage > self.__defensa:
                self._salud -= (points_of_damage - self.__defensa)
                print(f'Ahora tiene {self._salud} puntos de vida')
                if self._salud <= 0:
                    self.die()
                    print(f'{self.get_tipo().name} a muerto')

            else:
                print('El ataque no le ha afectado')

        else:
            if points_of_damage > self.__defensa:
                self._salud -= (points_of_damage - self.__defensa_especial)
                print(f'Ahora tiene {self._salud} puntos de vida')
                if self._salud <= 0:
                    self.die()
                    print(f'{self.get_tipo().name} a muerto')

            else:
                print('El ataque no le ha afectado')


