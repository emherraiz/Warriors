from enum import Enum
class Tipos_de_guerreros(Enum):
    Boxeador = 1
    Gladiador = 2
    UFC = 3
    MMA = 4

    @staticmethod
    def from_str(str_guerrero):
        str_guerrero = str_guerrero.lower()
        if str_guerrero == 'boxer':
            return Tipos_de_guerreros.BOXER
        elif str_guerrero == 'gladiator':
            return Tipos_de_guerreros.GLADIATOR
        elif str_guerrero == 'ufc':
            return Tipos_de_guerreros.UFC
        elif str_guerrero == 'mma':
            return Tipos_de_guerreros.MMA
        else:
            raise TypeError('No existe el tipo de guerrero ' + str_guerrero)

