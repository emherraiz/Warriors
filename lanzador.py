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
        entrenador = input(f'Entrenador {i+1} introduce tu nombre:')
        with open(csvs[i], newline='') as csv_file:
            reader = csv.reader(csv_file)
            data_from_file = list(reader)
        
        print(data_from_file)

