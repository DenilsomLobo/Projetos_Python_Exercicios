#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 18/11/2021
#Término: 18/11/2021
#Atividade 007: Letra F.

#Programa que imprime os numeros primos:

# Importando as bibliotecas:
import os


# Limpar terminal
os.system('cls')

# Texto de entrada:
print('=' * 80)
print('NUMEROS PRIMOS DE 0 A 100:')
print('=' * 80)

primos = []
for c in range (2, 101):
    cont = 0
    for c2 in range (1, c + 1):
        if c%c2==0:
            cont +=1
    if cont <=2:
        print(f'Os numeros primos são: {c}')

# Texto de saida:
print('='* 80)
print('FIM DO PROGRAMA')
print('=' * 80)