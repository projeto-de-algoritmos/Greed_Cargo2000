import pandas as pd
import json
import os
import collections
from funcoesGreed import *

with open('movies.json') as json_file:
    data = json.load(json_file)

cadastroFilmes = {}
while True:
    #os.system("clear")
    opcao = exibir_menu_principal()
    print(opcao)
    if opcao == 1:
        os.system("clear")
        cadastroFilmes = cadastra_filme(data, cadastroFilmes)
        print(cadastroFilmes)

    elif opcao == 2:
        os.system("clear")
        print("Filmes cadastrados")
        imprime_filmes_cadastrados(cadastroFilmes)

    elif opcao == 3:
        os.system("clear")
        print("Interval Partitioning")
        filmesOrdenadosHorarioInicio = sorted(cadastroFilmes.items(), key = lambda i: i[1]['horarioInicio']) 
        print(filmesOrdenadosHorarioInicio)
        cntdSalas = 0
        salas = []
        # salas['1'] = {}
        # salas['1'][filmesOrdenadosHorarioInicio[0][0]] = [filmesOrdenadosHorarioInicio[0][1]['horarioInicio'], filmesOrdenadosHorarioInicio[0][1]['horarioTermino']]
        # print(salas)

        executa_interval_partioning(filmesOrdenadosHorarioInicio, salas, cntdSalas)


    elif opcao == 4:
        os.system("clear")
        print("Aproveite o máximo de sua experiência no Cinemania")
        print("Lista de filmes que você consegue assistir hoje:")
        filmesOrdenadosHorarioTermino = sorted(cadastroFilmes.items(), key = lambda i: i[1]['horarioTermino']) 
        # print(filmesOrdenadosHorarioTermino)
        executa_interval_sheduling(filmesOrdenadosHorarioTermino)

    else:
        os.system("clear")
        print('Programa Encerrado!')

        break


    