#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data de início: 10/11/2021
#Término: 10/11/2021
#Atividade 005: Letra B.

#Programa que recebe 2 valores e faz a divisão.
#Se o valor não for inteiro arredonda o resultado.

#importação:
#Limpar tela
import os
os.system('cls')

#Operaçôes:
#arredondar
from math import ceil
from math import floor

#Texto de entrada:
print('='*40)
print('PROGRAMA DE DIVISÃO:')
print('='*40)

#Entrada de dados:
valor1 = float(input('Insira o valor 1: '))
print('-'*40)
valor2 = float(input('Insira o valor 2: '))
print('-'*40)

#Condicionais:
if (valor1 == 0) or (valor2 == 0):
    print('Valor invalido !')
    exit()
elif (valor1 == 0) and (valor2 == 0):
    print('valor invalido !')
    exit()
else:
    print()

#Operações:
resultado = valor1 / valor2
resultadoMais = ceil(resultado)
resultadoMenos = floor(resultado)

#Condicionais do resultado das operações:
if ((resultado + 0.5) >= resultadoMais):
    print(f'O resultado foi: {resultadoMais:.4f}')
else:
    print(f'O resultado foi: {resultadoMenos:.4f} ')

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)
