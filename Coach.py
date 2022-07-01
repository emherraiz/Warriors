class Coach():
    def __init__(self, nombre, lista_guerreros):
        self.__nombre = nombre
        self.__lista_guerreros = lista_guerreros

    def get_nombre(self):
        return self.__nombre

    def get_lista_guerreros(self):
        return self.__lista_guerreros

