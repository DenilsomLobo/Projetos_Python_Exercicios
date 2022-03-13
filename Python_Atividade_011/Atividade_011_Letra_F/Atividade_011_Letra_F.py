# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 06/02/2022
# Data do término: 06/02/2022
# Atividade 011: Letra F

# Crie uma função que receba 2 lista:
# lista 1: nome, peso, idade
# lista 2: John, 40, 1.8
# Sua função deve criar um dicionário contendo chave e valor
# utilizando como base essas duas
# listas. Depois, seu programa deverá imprimir esse dicionário
# utilizando o laço for ... items

# Importando as bibliotecas:
import os
from modulos_f.funcoes_f import *

# Limpando o terminal:
os.system('cls')


# Declaração:
lista1 = ['nome', 'peso', 'idade']
lista2 = ['John', 40, 1.8]

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Invocando a função:
retorno = formador_Dict(lista1, lista2)

# Texto de saida :
print('As listas são: ')
print()
print(f'Lista1: {lista1}')
print()
print(f'Lista2: {lista2}')
print()
print(f'Dicionario delas é: {retorno}')
print()

# Texto de encerramento:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
