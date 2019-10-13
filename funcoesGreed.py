import re
from pqdict import pqdict

def exibir_menu_principal():
    print('Bem vindo ao Cinemania')
    print('1 - Cadastrar filme')
    print('2 - Ver filmes cadastrados')
    print('3 - Visualizar número de salas necessárias para exibição')
    print('4 - Número máximo de filmes que uma pessoa consegue assistir por dia')
    print('0 - Sair')
    opcao = int(input('\n\nQual opção você deseja realizar? '))
    opcao = valida_opcao(opcao)
    return opcao

def valida_opcao(opcao):
    while (opcao < 0 or opcao > 4):
        print('Opção inválida! Por favor, digite novamente')
        opcao = int(input('\n\nQual opção você deseja realizar? '))
    return opcao

def cadastra_filme(data, cadastroFilmes):
    print("Cadastro Inicial")
    print(cadastroFilmes)
    nome = str(input('Digite o nome do filme: '))
    duracao, diretor, classificacao, genero, ano = retorna_dados(data, nome)
    if duracao == None:
        print('O filme digitado não pode ser localizado no catálogo')
        return cadastroFilmes
    else:
        x = []
        while x == []:
            horarioInicio = input('Digite o horário inicial do filme(XX:XX): ')
            x = re.findall("^(?:[0-1][0-9]|[2][0-3]):[0-5][0-9]$", horarioInicio)
            if x == []:
                print('Horário inválido!')

        listaHorarioInicio = horarioInicio.split(':')  # Split on whitespace
        minutosInicio = listaHorarioInicio[1]
        horaInicio = listaHorarioInicio[0]

        horaTermino = int(horaInicio) + int(int(duracao)/60)
        minutosTermino = int(minutosInicio) + int(duracao)%60

        if minutosTermino > 59:
            horaTermino = horaTermino + 1
            minutosTermino = minutosTermino - 60
        if horaTermino > 23:
            horaTermino = horaTermino - 24


        cadastroFilmes[nome.upper()] = {}   
        cadastroFilmes[nome.upper()]['genero'] = genero
        cadastroFilmes[nome.upper()]['ano'] = ano
        cadastroFilmes[nome.upper()]['classificacao'] = classificacao
        cadastroFilmes[nome.upper()]['diretor'] = diretor
        cadastroFilmes[nome.upper()]['horaInicio'] = horaInicio
        cadastroFilmes[nome.upper()]['minutosInicio'] = minutosInicio
        cadastroFilmes[nome.upper()]['horarioInicio'] = int(horaInicio + minutosInicio)
        cadastroFilmes[nome.upper()]['duracao'] = duracao
        cadastroFilmes[nome.upper()]['horaTermino'] = horaTermino
        cadastroFilmes[nome.upper()]['minutoTermino'] = minutosTermino
        cadastroFilmes[nome.upper()]['horarioTermino'] = int(str(horaTermino) + str(minutosTermino))

        print('Filme cadastrado com sucesso')
        return cadastroFilmes


def retorna_dados(json_object, nome):
    for dicionario in json_object:
        if nome.lower() == dicionario['name'].lower():
            return dicionario['runtime'],dicionario['director'],dicionario['rating'],dicionario['genre'],dicionario['year']
    return None, None, None, None, None

def imprime_filmes_cadastrados(cadastroFilmes):
    ctd = 0
    for filme in cadastroFilmes:
        ctd += 1
        print("\nFilme ", ctd)
        print("Nome: ", filme)
        print("Gênero: ", filme[filme]['genero'])
        print("Ano: ", filme[filme]['ano'])
        print("Clasificação: ", filme[filme]['classificacao'])
        print("Diretor: ", filme[filme]['diretor'])
        print("Duração: ", filme[filme]['duracao'])
        print("Horário de início da sessão: " + filme[filme]['horaInicio'] + ":" + filme[filme]['minutosInicio'])
        print("========================================================================================\n")


def executa_interval_sheduling(filmesOrdenadosHorarioTermino):
    horarioUltimoFilmeAdicionado = -1000
    nFilmes = 0

    for filme in filmesOrdenadosHorarioTermino:
        if(horarioUltimoFilmeAdicionado <= int(filme[1]['horarioInicio'])):
            horarioUltimoFilmeAdicionado = filme[1]['horarioTermino']
            nFilmes += 1
            print("\nFilme ", nFilmes)
            print("Nome: ", filme[0])
            print("Gênero: ", filme[1]['genero'])
            print("Ano: ", filme[1]['ano'])
            print("Clasificação: ", filme[1]['classificacao'])
            print("Diretor: ", filme[1]['diretor'])
            print("Duração: ", filme[1]['duracao'])
            print("Horário de início da sessão: " + filme[1]['horaInicio'] + ":" + filme[1]['minutosInicio'])
            print("========================================================================================\n")
           


def executa_interval_partioning(filmesOrdenadosHorarioInicio, salas, cntdSalas):
    salas.insert(0, filmesOrdenadosHorarioInicio[0][1]['horarioTermino']) 
    print(salas)
    print("\nSala 1 ")
    print("Nome: ", filmesOrdenadosHorarioInicio[0][0])
    print("Gênero: ", filmesOrdenadosHorarioInicio[0][1]['genero'])
    print("Ano: ", filmesOrdenadosHorarioInicio[0][1]['ano'])
    print("Clasificação: ", filmesOrdenadosHorarioInicio[0][1]['classificacao'])
    print("Diretor: ", filmesOrdenadosHorarioInicio[0][1]['diretor'])
    print("Duração: ", filmesOrdenadosHorarioInicio[0][1]['duracao'])
    print("Horário de início da sessão: " + filmesOrdenadosHorarioInicio[0][1]['horaInicio'] + ":" + filmesOrdenadosHorarioInicio[0][1]['minutosInicio'])
    print("========================================================================================\n")
           
    # filmesOrdenadosHorarioInicio.pop(0)
    print(filmesOrdenadosHorarioInicio)

    for filme in filmesOrdenadosHorarioInicio:
        print('AQUIIIIIIIIII',filmesOrdenadosHorarioInicio)
        # filmesOrdenadosHorarioInicio.pop(0)
        ctd = 1
        if(filme[1]['horarioInicio'] > min(salas)):
            print("\nSala  ", salas.index(min(salas)) + 1)
            print("Nome: ", filme[0])
            print("Gênero: ", filme[1]['genero'])
            print("Ano: ", filme[1]['ano'])
            print("Clasificação: ", filme[1]['classificacao'])
            print("Diretor: ", filme[1]['diretor'])
            print("Duração: ", filme[1]['duracao'])
            print("Horário de início da sessão: " + filme[1]['horaInicio'] + ":" + filme[1]['minutosInicio'])
            print("========================================================================================\n")
            salas[salas.index(min(salas))] = filme[1]['horarioTermino']
            # filmesOrdenadosHorarioInicio.pop(0)
        else:
            print("\nSala  ", len(salas) + 1)
            print("Nome: ", filme[0])
            print("Gênero: ", filme[1]['genero'])
            print("Ano: ", filme[1]['ano'])
            print("Clasificação: ", filme[1]['classificacao'])
            print("Diretor: ", filme[1]['diretor'])
            print("Duração: ", filme[1]['duracao'])
            print("Horário de início da sessão: " + filme[1]['horaInicio'] + ":" + filme[1]['minutosInicio'])
            print("========================================================================================\n")
            salas.append(filme[1]['horarioTermino']) 
            # filmesOrdenadosHorarioInicio.pop(0)    

