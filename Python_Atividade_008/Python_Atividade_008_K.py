# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 28/11/2021
# Data de termino: 28/11/2021
# Atividade 008: Letra K

# Programa que verifica nomes em uma lista.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:
listaDeNomes = ['Denilsom','João','Felipe','Pedro','Algusto','Bruno']

# Saida:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()
print(f'Esta e a sua lista de nomes: {listaDeNomes}')
print('-'*80)
print(f'Pedro esta na lista de nomes ?')
print()
# Condicionais:
if ('Pedro' not in listaDeNomes):
    print('"Pedro" não esta na lista !')
else:
    print('"Pedro" esta na lista !')
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)