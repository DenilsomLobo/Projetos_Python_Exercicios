# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 09/12/21
# Data do término: 09/12/21
# Atividade 010: Letra F

# Programa que cadastra 5 tios de vinhos.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:
dicionarioVinhos = {}
listaVinhos = []

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Estrutura de repetição de entrada de dados:
print('Insira o nome dos vinhos para adicionar no registro: ')
print('-'*80)
print()
for c in range(0, 5):
    dicionarioVinhos['Nome'] = str(input('Nome: '))
    dicionarioVinhos['Tipo'] = str(input('Tipo: '))
    dicionarioVinhos['Teor Alcoólico'] = str(input('Teor Alcoólico: '))
    dicionarioVinhos['Ano'] = str(input('Ano: '))
    print()
    listaVinhos.append(dicionarioVinhos.copy())

# Saida:
print('-'*80)
print('Os vinhos são:')
print('-'*80)
for dicionarioVinhos in listaVinhos:
    for chave, valor in dicionarioVinhos.items():
        print(f'{chave}: {valor}')
print()
print('-'*80)

# Texto de encerramento:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)