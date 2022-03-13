# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 09/12/21
# Data do término: 09/12/21
# Atividade 010: Letra J.

# Programa que valida se possui abacaxi na lista.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração
dicionarioFrutas = {
    'Uva':'07',
    'Banana':'04',
    'Maça':'03',
    'Abacaxi':'01'
}
abacaxi = 'Abacaxi'

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Estrutura de repetição lista de frutas:
print('-'*80)
print('As frutas são: ')
print('-'*80)
for chave, valor in dicionarioFrutas.items():
    print(f'{chave}: {valor}')

print('-'*80)
if ('Abacaxi' in dicionarioFrutas):
    print('Está no dicionario')
else:
    print('Não está no dicionario')


# Texto de encerramento:
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)