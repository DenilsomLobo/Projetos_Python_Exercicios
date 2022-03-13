# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 09/12/21
# Data do término: 09/12/21
# Atividade 010: Letra K

# Programa que registra pessoas.

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
print('Insira o nome dos vinhos para adicionar no registro: ')
print('-'*80)
print()
while(True):
    comando = str(input('Deseja adicionar um aluno na '+
    'lista de registro ? (s / 999): ')).lower().strip()
    if (comando != 's') and (comando != '999'):
        print('Entrada invalida ...')
    elif (comando == 's'):
        print()
        dicionarioRegistro['Nome'] = str(input('Nome: '))
        dicionarioRegistro['Idade'] = str(input('idade: '))
        print()
        listaRegistro.append(dicionarioRegistro.copy())
    elif (comando == '999'):
        break

# Saida:
print('-'*80)
print('Os alunos são:')
print('-'*80)
for dicionarioRegistro in listaRegistro:
    for c in range(0, 1):
        for chave, valor in dicionarioRegistro.items():
            print(f'{chave}: {valor}')
    print()
print()
print('-'*80)

# Texto de encerramento:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)