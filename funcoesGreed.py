import re

def exibir_menu_principal():
    print('Bem vindo ao Cinemania')
    print('1 - Cadastrar filme')
    print('2 - Visualizar número de salas necessárias para exibição')
    print('3 - Número máximo de filmes que uma pessoa consegue assistir por dia')
    print('0 - Sair')
    opcao = int(input('\n\nQual opção você deseja realizar? '))
    opcao = valida_opcao(opcao)
    return opcao

def valida_opcao(opcao):
    while (opcao < 0 or opcao > 3):
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
        minutoTermino = int(minutosInicio) + int(duracao)%60

        if minutoTermino > 59:
            horaTermino = horaTermino + 1
            minutoTermino = minutoTermino - 60
        if horaTermino > 23:
            horaTermino = horaTermino - 24


        cadastroFilmes[nome.upper()] = {}   
        cadastroFilmes[nome.upper()]['genero'] = genero
        cadastroFilmes[nome.upper()]['ano'] = ano
        cadastroFilmes[nome.upper()]['classificacao'] = classificacao
        cadastroFilmes[nome.upper()]['diretor'] = diretor
        cadastroFilmes[nome.upper()]['horaInicio'] = horaInicio
        cadastroFilmes[nome.upper()]['minutosInicio'] = minutosInicio
        cadastroFilmes[nome.upper()]['duracao'] = duracao
        cadastroFilmes[nome.upper()]['horaTermino'] = horaTermino
        cadastroFilmes[nome.upper()]['minutoTermino'] = minutoTermino

        print('Filme cadastrado com sucesso')
        return cadastroFilmes


def retorna_dados(json_object, nome):
    for dicionario in json_object:
        if nome.lower() == dicionario['name'].lower():
            return dicionario['runtime'],dicionario['director'],dicionario['rating'],dicionario['genre'],dicionario['year']
    return None, None, None, None, None
