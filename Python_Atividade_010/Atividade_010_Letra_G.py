# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 09/12/21
# Data do término: 09/12/21
# Atividade 010: Letra G

# Programa que cadastra alunos em uma escola.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:
dicionarioAlunos = {}
listaAlunos = []

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Estrutura de repetição de entrada de dados:
print('Insira o nome dos vinhos para adicionar no registro: ')
print('-'*80)
print()
while(True):
    comando = str(input('Deseja adicionar um aluno na '+
    'lista de registro ? (s/n): ')).lower().strip()
    if (comando != 's') and (comando != 'n'):
        print('Entrada invalida ...')
    elif (comando == 's'):
        print()
        dicionarioAlunos['Nome'] = str(input('Nome: '))
        dicionarioAlunos['Data de Nacimento'] = str(input('Data de '+
        'Nacimento: '))
        dicionarioAlunos['Matricula'] = str(input('Matricula: '))
        print()
        listaAlunos.append(dicionarioAlunos.copy())
    elif (comando == 'n'):
        break

# Saida:
print('-'*80)
print('Os alunos são:')
print('-'*80)
for dicionarioAlunos in listaAlunos:
    for c in range(0, 1):
        for chave, valor in dicionarioAlunos.items():
            print(f'{chave}: {valor}')
    print()
print()
print('-'*80)

# Texto de encerramento:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)