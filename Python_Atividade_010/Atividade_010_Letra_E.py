# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 08/12/21
# Data do término: 08/12/21
# Atividade 010: Letra E

# Programa que cadastra 5 ferramentas

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:
dicionarioFerramentas = {}
listaFerramentas = []

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Estrutura de repetição de entrada de dados:
print('Insira o nome das ferramentas para adicionar na lista: ')
print('-'*80)
print()
for c in range(0, 5):
    dicionarioFerramentas['Ferramenta'] = str(input('Nome: '))
    print()
    listaFerramentas.append(dicionarioFerramentas.copy())

# Saida:
print('-'*80)
print('As ferramentas são:')
print('-'*80)
for dicionarioFerramentas in listaFerramentas:
    for chave, valor in dicionarioFerramentas.items():
        print(f'{chave}: {valor}')
print()
print('-'*80)

# Verificarndo tamanho da lista:
tamanho = len(listaFerramentas)
print()
print(f'O tamanho do dicionario e: {tamanho}')
print()

# Texto de encerramento:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)