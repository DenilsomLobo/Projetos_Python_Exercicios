# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 05/02/2022
# Data do término: 05/02/2022
# Atividade 011: Letra D

# Crie uma função que receba uma temperatura em fahrenheit e retorne o
#  valor em graus célsius.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Funções:
def conversor_temperatura(temp):
    r = (temp - 32) * (5/9)
    return r

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Entrada de dados:
print('insira a temperatura em Fahrenheit que deseja converter em celsius: ')
print()
valor = float(input('Temperatura ?: '))
print()
print('-'*80)
print()

# Saida de dados:
print(f'A temperatura solicitada foi: {valor}')
print()
resposta = conversor_temperatura(valor)
print(f'Valor convertido para celsius foi : {resposta}')
print()

# Texto de encerramento:
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)