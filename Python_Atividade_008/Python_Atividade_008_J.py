# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 28/11/2021
# Data de termino: 28/11/2021
# Atividade 008: Letra I

# Programa que sorteia numeros em uma lista de 0 a 50.

# Importando as bibliotecas:
import os
import copy
from random import randint

# Limpando o terminal:
os.system('cls')

# Declaração:
listaDeNumeros = []

# Estrutura de repetição de numeros aleatorios:
for c in range (0, 50):
    numerosAleatorios = randint (0, 100)
    listaDeNumeros.append(numerosAleatorios)

# Fatiamento de listas
listaCopiada = copy.copy(listaDeNumeros)
listaCrescente = sorted(listaCopiada)
lista1 = listaCrescente [0:10]
lista2 = listaCrescente [10:20]
lista3 = listaCrescente [20:30]
lista4 = listaCrescente [30:40]
lista5 = listaCrescente [40:50]

# Texto de saida:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()
print(f'A lista sorteada foi: {listaDeNumeros}')
print()
print(f'Sua lista em forma crescente e: {listaCrescente}')
print()
print('-'*80)
print()
print(f'O primeiro fatiamento é: {lista1}')
print()
print(f'O primeiro fatiamento é: {lista2}')
print()
print(f'O primeiro fatiamento é: {lista3}')
print()
print(f'O primeiro fatiamento é: {lista4}')
print()
print(f'O primeiro fatiamento é: {lista5}')
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
