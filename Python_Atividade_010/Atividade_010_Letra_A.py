# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 07/12/21
# Data do término: 07/12/21
# Atividade 010: Letra A

# Programa com um dicionario com 4 elementos.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:

biblioteca = {} # Dicionario
lista = [] # Lista

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

# Estrutura de repetição de entrada de dados:
for c in range (0, 4):
    biblioteca['Nome'] = str(input('Insira o nome da pessoa: '))
    print()
    biblioteca['Idade'] = str(input('Insira a idade da pessoa: '))
    print()
    # Adição a biblioteca:
    lista.append(biblioteca.copy())

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