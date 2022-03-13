# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 09/12/21
# Data do término: 09/12/21
# Atividade 010: Letra H

# Programa que mostra o registro de um usuario.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:

biblioteca = {
    'Nome':'Jhon',
    'Idade':'40',
    'Peso':'80',
    'Altura':'1.70'
}

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Estrutura de repetição:
print('Registo do usuario:')
print('-'*80)
print()
for chave, valor in biblioteca.items():
    print(f'{chave} : {valor}')
print()

# Comando para deletar
del(biblioteca['Peso'])

# Estrutura de repetição:
print('='*80)
print('Nova lista sem o peso:')
print('-'*80)
for chave, valor in biblioteca.items():
    print(f'{chave} : {valor}')
print()

# Texto de encerramento:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)