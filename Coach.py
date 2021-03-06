
from warrior import Warrior
class Coach():
    def __init__(self, nombre, lista_guerreros):
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

    def añadir_guerreros(self, guerrero):
        if isinstance(guerrero, Warrior):
            self.__lista_guerreros.append()

        else:
            raise TypeError("El formato introducido es incorrecto")

    def eliminar_guerreros(self, posicion):
        if not isinstance(posicion, int):
            raise TypeError("El formato introducido es incorrecto")

        posiciom -= 1

        if 0 <= posicion < len(self.__lista_guerreros):
            self.__lista_guerreros.remove(self.__lista_guerreros[posicion])

        else:
            raise ValueError("Se tiene que introducir una posición correcta")

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



