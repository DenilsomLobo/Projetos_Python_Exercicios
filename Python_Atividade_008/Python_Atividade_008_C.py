# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 26/11/2021
# Data de termino: 26/11/2021
# Atividade 008: Letra C

# Programa que fatia a lista passando a informação de acordo com o que pede.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declarações:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista1a9 = lista [0:9]
lista8a13 = lista[7:13]
listaPares = lista[1:15:2]
listaImpares = lista[0:15:2]
listaM2 = lista[1:15:2]
listaM3 = lista[2:15:3]
listaM4 = lista[3:15:4]
listaReversa = lista[::-1]
lista5e6 = lista[4] + lista[5]
lista11e12 = lista[10] + lista[11]
mutiplicacao = lista5e6 * lista11e12

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

# Saida:
print(f'Lista de 1 até 9: {lista1a9}')
print()
print(f'Lista de 8 até 13: {lista8a13}')
print()
print(f'Lista de pares: {listaPares}')
print()
print(f'Lista de impares: {listaImpares}')
print()
print(f'Lista de multiplos de 2: {listaM2}')
print()
print(f'Lista de multiplos de 3: {listaM3}')
print()
print(f'Lista de multiplos de 4: {listaM4}')
print()
print(f'Lista reversa: {listaReversa}')
print()
print(f'Produto dos intervalos 5-6 e 11-12: {mutiplicacao}')
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)