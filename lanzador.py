import csv
import random
from enum import Enum
from Vida import Vida
from Tipos_de_armas import Tipos_de_armas
from Tipos_de_guerreros import Tipos_de_guerreros
from warrior import Warrior
from Guerrero_ofensivo import Guerrero_ofensivo
from Guerrero_defensivo import Guerrero_defensivo
from Super_guerrero import Super_guerrero
from Coach import Coach




def lanzar():
    entrenadores = []
    csvs = ['coach_1_warriors.csv', 'coach_2_warriors.csv']
    for i in range(2):
        lista_guerreros = []
        nombre_entrenador = input(f'Entrenador {i+1} introduce tu nombre:')
        try:
            with open(csvs[i], newline='') as csv_file:
                reader = csv.reader(csv_file)
                data_from_file = list(reader)

        except Exception as e:
            print('No se han podido leer adecuadamente los archivos csv')
            print(e)

        for dt in data_from_file:
            lista_guerreros.append(Super_guerrero(int(dt[0]), Tipos_de_guerreros.from_str(dt[1]), Tipos_de_armas.from_str(dt[2]), int(dt[3]), int(dt[4]), int(dt[5]), int(dt[6]), int(dt[7])))

        entrenadores.append(Coach(nombre_entrenador, lista_guerreros))




lanzar()
