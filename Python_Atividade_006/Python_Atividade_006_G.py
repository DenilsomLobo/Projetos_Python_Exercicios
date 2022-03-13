# Curso Técnico de informática
# Autor: Denilsom Lobo   
# Data de início: 13/11/2021
# Término: 13/11/2021
# Atividade 006: Letra G.

# Programa que recebe um numero milhar e mostra o sistema de numeração decimal.

# Importando as bibliotecas:
import os
from random import randint

# Limpar terminal
os.system('cls')

# Texto de entrada:
print('='*80)
print('PROGRAMA QUE RECEBE UM NUMERO E MOSTA O SISTEMA DE NUMERAÇÃO DECIMAL:')
print('='*80)

# Entrada de Dados:
numero = int(input('Digite um número milhar: '))

# Conversão de string:
unidade = (numero // 1) % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# Saída:
print('-'*80)
print(f'Sua unidade é: {unidade}')
print(f'Sua dezena é: {dezena}')
print(f'Sua centena é: {centena}')
print(f'Sua milhar é: {milhar}')

# Texto de saida:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
