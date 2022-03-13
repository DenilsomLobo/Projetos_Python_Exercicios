# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 28/11/2021
# Data de termino: 28/11/2021
# Atividade 008: Letra M

# Programa que recebe 7 numeros e separa de par e impar.

# Importando as bibliotecas:
import os
import copy


# Limpando o terminal:
os.system('cls')

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

# Entrada de dados:
listaDeNumeros = []


# Estruturas de repetição para entrada de dados:
for c in range (0,10):
    print(f'Numero {c+1}')
    numero = float(input('Insira um numero: '))
    listaDeNumeros.append(numero)
    listaNova = copy.copy(listaDeNumeros)
    listaAscendente = sorted(listaNova)
    listaDescendente = sorted(listaNova, reverse=True)

# Saida:
print('-'*80)
print(f'A sua lista e: {listaDeNumeros}')
print()
print(f'A sua lista ascendente: {listaAscendente}')
print()
print(f'A sua lista descentente: {listaDescendente}')
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)

