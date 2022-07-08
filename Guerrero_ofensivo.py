import random
from warrior import Warrior
from Tipos_de_armas import Tipos_de_armas
from Tipos_de_guerreros import Tipos_de_guerreros

class Guerrero_ofensivo(Warrior):
    def __init__(self, id, tipo, arma, salud, ataque, defensa, ataque_especial):
        super().__init__(id, tipo, arma, salud, ataque, defensa)
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

    def fight_attack(self, warrior_to_attack):
        print(f'El guerrero {str(self)} ataca al guerrero {str(warrior_to_attack)}')
        usar_habilidad = random.randint(0, 1)
        if usar_habilidad:
            warrior_to_attack.fight_defense(self.__ataque)

        else:
            warrior_to_attack.fight_defense(self.__ataque_especial)



