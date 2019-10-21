# Cinemania

**Número da Lista**: 3<br>
**Conteúdo da Disciplina**: Algoritimos ambiciosos<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 16/0006872  |  Gabriela Chaves de Moraes |
| 16/0012961  |  Lucas Arthur Lermen |

## Sobre 
<p align="justify">Essa lista consiste de um menu que permite o cadastro de diversos filmes na programação utilizando o dataset  <a href="https://www.kaggle.com/danielgrijalvas/movies/version/1">Movie Industry</a>. Após o cadastro, pode ser escolhida uma opção para organizar todos os filmes em diferentes salas de exibição, ou apresentar a maior quantidade de filmes que um espectador consegue assistir.

## Instalação 

**Linguagem**: Python v3.6 ou superior <br>

### Executando o projeto

#### Pré-requisitos

``` console
$ pip3 install pandas
```

#### Comandos para executar

``` console
$ python3 cinemania.py

```
## Uso 
Ao executar o comando será inicializado um menu com 5 opções
1 - Cadastrar filme
2 - Ver filmes cadastrados
3 - Visualizar número de salas necessárias para exibição
4 - Número máximo de filmes que uma pessoa consegue assistir por dia
0 - Sair

Caso deseje cadastrar um filme presente no dataset, selecione a opção 1. Ao selecionar a opção 2, lhe será apresentado uma lista com todos os filmes cadastrados. A opção 3 apresenta como os filmes ficariam dispostos a fim de  todos serem apresentados com o menor número possível de salas(Interval Partitioning). Já a opção 4, apresenta o maior número de filmes que uma pessoa consegue assistir de acordo com os filmes cadastrados(Interval Scheduling)


