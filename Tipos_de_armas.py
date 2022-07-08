from enum import Enum
class Tipos_de_armas(Enum):
    Puñetazo = 4
    Patada = 6
    Codazo = 8
    Espada = 10

    @staticmethod
    def from_str(str_tipo_de_arma):
        str_tipo_de_arma = str_tipo_de_arma.lower()
        if str_tipo_de_arma == 'punch':
            return Tipos_de_armas.Puñetazo
        elif str_tipo_de_arma == 'kick':
            return Tipos_de_armas.Patada
        elif str_tipo_de_arma == 'elbow':
            return Tipos_de_armas.Codazo
        elif str_tipo_de_arma == 'sword':
            return Tipos_de_armas.Espada
        else:
            raise TypeError("No existe el tipo de arma " + str_tipo_de_arma)
