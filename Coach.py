
from warrior import *
class Coach():
    def __init__(self, nombre, lista_guerreros):
        print(type(lista_guerreros))
        print(isinstance(lista_guerreros, Warrior))
        if not (isinstance(nombre, str) or isinstance(lista_guerreros, Warrior) or isinstance(lista_guerreros, list)):
            raise TypeError("El formato introducido es incorrecto")

        if type(lista_guerreros) == list:
            for warrior in lista_guerreros:
                if not isinstance(warrior, Warrior):
                    raise TypeError("El formato introducido es incorrecto")

        else:
            lista_guerreros = [lista_guerreros]


        self.__nombre = nombre
        self.__lista_guerreros = lista_guerreros

    def get_nombre(self):
        return self.__nombre

    def get_lista_guerreros(self):
        return self.__lista_guerreros

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def añadir_guerreros(self, guerrero):
        if isinstance(guerrero, Warrior):
            self.__lista_guerreros.append()

        else:
            raise TypeError("El formato introducido es incorrecto")

    def eliminar_guerreros(self, posicion):
        if not isinstance(posicion, int):
            raise TypeError("El formato introducido es incorrecto")

        if 0 <= posicion < len(self.__lista_guerreros):
            self.__lista_guerreros.remove(self.__lista_guerreros[posicion])

    def is_undefeated(self):
        equipo_vivo = False
        for guerrero in self.__lista_guerreros:
            if guerrero.is_vivo():
                equpo_vivo = True
                break

        return equipo_vivo

    def surrender(self):
        for guerrero in self.__lista_guerreros:
            guerrero.die()

    def __str__(self):
        texto_salida = ''
        for guerrero in self.__lista_guerreros:
            texto_salida += f'{guerrero.get_id()} - {str(guerrero)} y tiene {guerrero.get_salud()} puntos de salud\n'

        return texto_salida

    def __repr__(self):
        texto_salida = ''
        for guerrero in self.__lista_guerreros:
            texto_salida += f'{guerrero.get_id()} - {str(guerrero)}\n'



print(isinstance([1,2], list or int))

a = Warrior(1, Tipos_de_guerreros.MMA, Tipos_de_armas.Patada, 12, 3, 3)
b = Warrior(2, Tipos_de_guerreros.Boxeador, Tipos_de_armas.Patada, 12, 3, 3)

print(not isinstance(a, Warrior or list))
print(isinstance('doa', str))
x = Coach('dos', [a, b])
print(x)
