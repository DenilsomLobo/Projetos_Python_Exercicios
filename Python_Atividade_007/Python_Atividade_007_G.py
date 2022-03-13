# Curso Técnico de informática
# Autor: Denilsom Lobo   
# Data de início: 18/11/2021
# Término: 18/11/2021
# Atividade 007: Letra G.

# Programa que imprime os numeros primos em intervalo 
# pré-determinado pelo usuario:

# Importando as bibliotecas:
import os


# Limpar terminal
os.system('cls')

# Texto de entrada:
print('=' * 80)
print('PROGRAMA QUE IMPRIME NUMEROS PRIMOS:')
print('=' * 80)

# Entrada de dados:
soma = 0
inicio = int(input('De qual inicio deseja começar? '))
if (inicio <= 2):
    inicio = 2
print('-'*80)
final = int(input('Aonde quer que pare ? '))
print('-'*80)

# Estrutura de repetição:
for c in range (inicio, final):
    cont = 0
    for c2 in range (1, c + 1):
        if c%c2==0:
            cont +=1
    if cont <=2:
        print(f'Os números primos são: {c}')
        soma += c
        
print('')
print(f'A soma entre eles são : {soma} ')

#Operações:

# Texto de saida:
print('='* 80)
print('FIM DO PROGRAMA')
print('=' * 80)
