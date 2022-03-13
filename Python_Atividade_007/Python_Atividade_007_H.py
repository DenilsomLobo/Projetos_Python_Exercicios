# Curso Técnico de informática
# Autor: Denilsom Lobo   
# Data de início: 18/11/2021
# Término: 18/11/2021
# Atividade 007: Letra H.

# Programa que imprime os numeros primos em intervalo 
# pré-determinado pelo usuario:

# Importando as bibliotecas:
import os


# Limpar terminal
os.system('cls')

# Texto de entrada:
print('=' * 80)
print('INICIO DO PROGRAMA:')
print('=' * 80)

# Entrada de dados:
inicio = int(input('Numero de inicio da contagem: '))
fim = int(input('Numero do fim da contagem : '))
break1 = int(input('Numero 1 que não quer que mostre: '))
break2 = int(input('Numero 2 que não quer que mostre: '))
break3 = int(input('Numero 3 que não quer que mostre: '))
print('-'*80)

# Estrutura de repetição:
for c in range(inicio, fim):
    if (c == break1):
        continue
    elif (c == break2):
        continue
    elif (c == break3):
        continue
    print('Contagem: ' + str(c)) 

print('-'*80)

# Texto de saida:
print('='* 80)
print('FIM DO PROGRAMA')
print('=' * 80)