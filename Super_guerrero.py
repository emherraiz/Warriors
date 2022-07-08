import random
from warrior import Warrior
from Tipos_de_armas import Tipos_de_armas
from Tipos_de_guerreros import Tipos_de_guerreros

class Super_guerrero(Warrior):
    def __init__(self, id, tipo, arma, salud, ataque, defensa, ataque_especial, defensa_especial):
        super().__init__(id, tipo, arma, salud, ataque, defensa)

        if not (isinstance(ataque_especial, int) and isinstance(defensa_especial, int)):
            raise TypeError("El formato introducido es incorrecto")
        if not (11 <= ataque_especial <= 20):
            raise ValueError('El ataque especial debe estar en un rango ente 11 y 20')
        if not (11 <= defensa_especial <= 20):
            raise ValueError('La defensa especial debe estar en un rango ente 11 y 20')
        self.__ataque_especial = ataque_especial
        self.__defensa_especial = defensa_especial

    def get_defensa_especial(self):
        return self.__defensa_especial

    def get_ataque_especial(self):
        return self.__ataque_especial


    def set_defensa_especial(self, defensa_especial):
        if not isinstance(defensa_especial, int):
            raise TypeError("El formato introducido es incorrecto")
        if not (11 <= defensa_especial <= 20):
            raise ValueError('La defensa especial debe estar en un rango ente 11 y 20')
        self.__defensa_especial = defensa_especial


    def set_ataque_especial(self, ataque_especial):
        if not isinstance(ataque_especial, int):
            raise TypeError("El formato introducido es incorrecto")
        if not (11 <= ataque_especial <= 20):
            raise ValueError('El ataque especial debe estar en un rango ente 11 y 20')
        self.__ataque_especial = ataque_especial
        self.__ataque_especial = ataque_especial



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



    def fight_attack(self, warrior_to_attack):
        print(f'El guerrero {str(self)} ataca al guerrero {str(warrior_to_attack)}')
        usar_habilidad = random.randint(0, 1)
        if usar_habilidad:
            warrior_to_attack.fight_defense(self.__ataque)

        else:
            warrior_to_attack.fight_defense(self.__ataque_especial)



a = Super_guerrero(1, Tipos_de_guerreros.MMA, Tipos_de_armas.Patada, 12, 3, 9, 11, 11)

