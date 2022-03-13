# Curso Técnico de informática
# Autor: Denilsom Lobo   
# Data de início: 18/11/2021
# Término: 18/11/2021
# Atividade 007: Letra C.

#Programa que imprime os numero de 1 a 10 de forma inversa.

# Importando as bibliotecas:
import os


# Limpar terminal
os.system('cls')

# Texto de entrada:
print('=' * 80)
print('CONTAGEM DE 10 - 1 DE FORMA INVERSA.')
print('=' * 80)

#Entrada de declaração:
for c in range (10, 0, -1):
    print (f'Contagem : {c}')
    print()

# Texto de saida:
print('='* 80)
print('FIM DO PROGRAMA')
print('=' * 80)