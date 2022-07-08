from Guerrero_ofensivo import Guerrero_ofensivo
from Guerrero_defensivo import *

class Super_guerrero(Guerrero_ofensivo, Guerrero_defensivo):
    def __init__(self, id, tipo, arma, salud, defensa, ataque_especial, defensa_especial):
        super().__init__(id, tipo, arma, salud, defensa, ataque_especial)
        super().__init__(id, tipo, arma, salud, defensa, defensa_especial)
        self.set_ataque_especial(ataque_especial)
        self.set_defensa_especial(defensa_especial)


a = Super_guerrero(1, Tipos_de_guerreros.MMA, Tipos_de_armas.Patada, 12, 3, 11, 11)

