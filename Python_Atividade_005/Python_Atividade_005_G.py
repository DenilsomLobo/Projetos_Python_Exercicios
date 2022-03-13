#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data de início: 10/11/2021
#Término: 10/11/2021
#Atividade 005: Letra G.

#Programa que calcula equação de segundo grau.

#Limpar tela:
import os
os.system('cls')

#Texto de entrada:
print('='*40)
print('PROGRAMA QUE CALCULA EQUAÇÃO 2º ')
print('='*40)

#Entrada de dados:
a = float(input('Insira o valor de A da equação: '))
b = float(input('Insira o valor de B da equação: '))
c = float(input('Insira o valor de C da equação: '))
delta = (b ** 2) - 4 * a * c
bhaskara1 = ((-1 * b) + (delta ** (1/2))) / (2*a)
bhaskara2 = ((-1 * b) - (delta ** (1/2))) / (2*a)

#Saida:
print(f'Os valores de da equanção são {a} , {b} e {c}')
print('-'*40)
print(f'O Delta dessa equanção e : {delta}')
print(f'Como Delta podemos fazer a forma de bhaskara para achar a raíz x1 e x2')
print('-'*40)
print(f'X1 = {bhaskara1}')
print(f'X2 = {bhaskara2}')
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)