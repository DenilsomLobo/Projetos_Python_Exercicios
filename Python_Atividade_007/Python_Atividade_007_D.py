# Curso Técnico de informática
# Autor: Denilsom Lobo   
# Data de início: 18/11/2021
# Término: 18/11/2021
# Atividade 007: Letra D.

#Programa que imprime os numero pares de 0 a 100.

# Importando as bibliotecas:
import os


# Limpar terminal
os.system('cls')

# Texto de entrada:
print('=' * 80)
print('NUMEROS PARES DE 0 A 100:')
print('=' * 80)

for c in range (0, 101, +2):
    print(f'Numeros pares: {c}')

# Texto de saida:
print('='* 80)
print('FIM DO PROGRAMA')
print('=' * 80)