import pandas as pd
import json
import os
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
        print("Interval Partitioning")

    elif opcao == 3:
        os.system("clear")
        print("Interval Scheduling")

    else:
        os.system("clear")
        print('Programa Encerrado!')

        break


    