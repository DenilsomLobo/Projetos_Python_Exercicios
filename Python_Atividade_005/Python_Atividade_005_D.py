#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data de início: 10/11/2021
#Término: 10/11/2021
#Atividade 005: Letra D.

#Programa que insere um valor para o ângulo e o programa calcula.
#seno, cosseno e tangente.

#Importação:
#Limpar tela
import os
os.system('cls')

#Operações:
import math

#Texto de entrada:
print('='*40)
print('PROGRAMA DE CALCULAR SENO, COSSENO E TANGENTE  DE ÂNGULO:')
print('='*40)

#Entrada de dados:
angulo = float(input('Insira o valor do ângulo: '))
print('-'*40)

#Operações:
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

#Saida:
print(f'O seno do ângulo {angulo} e: {sen:.2f}')
print('-'*40)
print(f'O cosseno do ângulo {angulo} e: {cos:.2f}')
print('-'*40)
print(f'a tangente do ângulo {angulo} e: {tan:.2f}')

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)