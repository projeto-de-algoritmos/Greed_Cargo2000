import pandas as pd
import json
import os
import collections
from funcoesGreed import *

with open('movies.json') as json_file:
    data = json.load(json_file)

cadastroFilmes = {}
while True:
    opcao = exibir_menu_principal()
    if opcao == 1:
        os.system("clear")
        print("================= CADASTRE UM FILME ====================")
        cadastroFilmes = cadastra_filme(data, cadastroFilmes)

    elif opcao == 2:
        os.system("clear")
        print("================= FILMES CADASTRADOS ====================")
        imprime_filmes_cadastrados(cadastroFilmes)

    elif opcao == 3:
        os.system("clear")
        print("========== Disposição de salas para exibir todos os filmes cadastrados ================")
        filmesOrdenadosHorarioInicio = sorted(cadastroFilmes.items(), key = lambda i: i[1]['horarioInicio']) 
        salas = [0]
        executa_interval_partitioning(filmesOrdenadosHorarioInicio, salas)


    elif opcao == 4:
        os.system("clear")
        print("Aproveite o máximo de sua experiência no Cinemania!\n")
        print("Lista de filmes que você consegue assistir hoje:\n")
        filmesOrdenadosHorarioTermino = sorted(cadastroFilmes.items(), key = lambda i: i[1]['horarioTermino']) 
        executa_interval_sheduling(filmesOrdenadosHorarioTermino)

    else:
        os.system("clear")
        print('Programa Encerrado!')

        break


    