# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 09/12/21
# Data do término: 09/12/21
# Atividade 010: Letra I

# Programa que cadastra alunos em uma escola.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:
dicionarioRegistro = {}
listaRegistro = []

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Estrutura de repetição de entrada de dados:
print('Insira o nome dos novos usuários no registro: ')
print('-'*80)
print()
while(True):
    comando = str(input('Deseja adicionar um registro de '+
    'novo usuário ? (s/n): ')).lower().strip()
    if (comando != 's') and (comando != 'n'):
        print('Entrada invalida ...')
    elif (comando == 's'):
        print()
        dicionarioRegistro['Nome'] = str(input('Nome: '))
        dicionarioRegistro['Data de Nacimento'] = str(input('Data de '+
        'Nacimento: '))
        dicionarioRegistro['idade'] = str(input('Idade: '))
        dicionarioRegistro['Matricula'] = str(input('Matricula: '))
        print()
        listaRegistro.append(dicionarioRegistro.copy())
    elif (comando == 'n'):
        break

# Saida de novos usuários:
print('-'*80)
print('Os usuários são:')
print('-'*80)
for dicionarioRegistro in listaRegistro:
    for c in range(0, 1):
        for chave, valor in dicionarioRegistro.items():
            print(f'{chave}: {valor}')
    print()
print()
print('-'*80)

# Comando para apagar o dicionário matricula do ultimo:
novaAgenda = dicionarioRegistro.popitem()

# Saida de usuários sem matricula:
print('-'*80)
print('Os usuários são (Sem a matricula no ultimo):')
print('-'*80)
for novaAgenda in listaRegistro:
    for c in range(0, 1):
        for chave, valor in novaAgenda.items():
            print(f'{chave}: {valor}')
    print()
print()

# Texto de encerramento:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)