# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 28/11/2021
# Data de termino: 28/11/2021
# Atividade 008: Letra L

# Programa que recebe 7 numeros e separa de par e impar.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

# Entrada de dados:
listaDeNumeros = []
listaDeImpares = []
listaDePares = []

# Estruturas de repetição para entrada de dados:
for c in range (0,7):
    print(f'Numero {c+1}')
    numero = int(input('Insira um numero: '))
    listaDeNumeros.append(numero)

for i, valor in enumerate(listaDeNumeros):
    if (valor % 2 == 0):
        listaDePares.append(valor)
    else:
        listaDeImpares.append(valor)

# Saida:        
print('-'*80)
print(f'A lista de numeros e: {listaDeNumeros}')
print()
print(f'A lista de pares é: {listaDePares}')
print()
print(f'A lista de impares é: {listaDeImpares}')
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)