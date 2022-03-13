#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data de início: 10/11/2021
#Término: 10/11/2021
#Atividade 005: Letra E.

#Programa que sorteia um numero de 1 a 20

#Importação:
#Limpar tela
import os
os.system('cls')

#Randomizador
from random import randint

#Entrada de dados:
numeroAleatorio = randint (1,20)

#Texto de entrada

print('='*40)
print('PROGRAMA QUE SORTEIA NUMEROS DE 1 A 20')
print('='*40)
entrada = str(input('Deseja sortear um numero de 1 a 20 ? '))
print('-'*40)

#Saida:
print(f'O numero sorteado foi: {numeroAleatorio}')

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)