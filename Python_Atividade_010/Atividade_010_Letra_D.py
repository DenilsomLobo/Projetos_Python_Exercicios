# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 07/12/21
# Data do término: 07/12/21
# Atividade 010: Letra E

# Programa com um dicionario com 5 cores.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:

biblioteca = {} # Dicionario
lista = [] # Lista
contador = 0
# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

# Estrutura de repetição de entrada de dados:
for c in range (0, 5):
    biblioteca['cor'] = contador + c
    print()
    biblioteca['nome'] = str(input('Insira o  nome da cor: '))
    print()
    # Adição a biblioteca:
    lista.append(biblioteca.copy())
print('-'*80)

# Estrutura de repetição de saida de dados:
print('-'*80)
print('Sua lista de nomes e: ')
print()
for biblioteca in lista:
    for chave, valor in biblioteca.items():
        print(f'{chave}: {valor}')
        
# Texto de encerramento:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)