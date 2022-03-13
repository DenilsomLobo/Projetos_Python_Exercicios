#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 13/11/2021
#Término: 13/11/2021
#Atividade 006: Letra G.

#Programa que recebe um numero milhar e mostra o sistema de numeração decimal.

# Importando as bibliotecas:
import os
from random import randint

#Limpar terminal
os.system('cls')

#Texto de entrada:
print('='*80)
print('PROGRAMA QUE RECEBE UM NUMERO E MOSTA O SISTEMA DE NUMERAÇÃO DECIMAL:')
print('='*80)

#Entrada de Dados:
numero = randint (1000, 9999)
numero2 = str(numero)

#Conversão de string:
unidade = numero2[3:4]
dezena = numero2[2:4]
centena = numero2[1:4]
milhar = numero2[0:4]

#Saída:
print('-'*80)
print(f'O numero é: {numero}')
print('-'*80)
print(f'Sua unidade é: {unidade}')
print(f'Sua dezena é: {dezena}')
print(f'Sua centena é: {centena}')
print(f'Sua milhar é: {milhar}')

#Texto de saida:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
