#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 10/11/2021
#Término: 10/11/2021
#Atividade 005: Letra A

#Programa que recebe um valor e cálcula a raiz quadrada arredondando os valores

#Imports:
#Limpar terminal
import os
os.system('cls')

#Operações:
# Raiz quadrada
from math import sqrt
#Arredondar
from math import ceil
from math import floor

#Texto de entrada:
print('='*40)
print('CALCULADORA DE RAIZ QUADRADA')
print('='*40)

#Entrada de dados:
valor = float(input('Insira o valor: '))

#Validação:
if (valor >= 0):
    print('-'*40)
else:
    print('-'*40)
    print('Não existe em R. Numero complexo.')
    print('='*40)
    print('FIM DO PROGRAMA')
    print('='*40)
    exit()

#Operações:
raizquadrada = sqrt(valor)
resultado1 = ceil(raizquadrada) 
resultado2 = floor(raizquadrada) 

#Condicionais da operação:
if ((raizquadrada + 0.5) >= resultado1):
    print(f'O resultado e: {resultado1:.4f}')
else:
    print(f'O resultado e: {resultado2}')

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)
