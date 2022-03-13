#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 18/11/2021
#Término: 18/11/2021
#Atividade 007: Letra E.

#Programa que soma a quantidade de numeros pares encontrados:

# Importando as bibliotecas:
import os


# Limpar terminal
os.system('cls')

# Texto de entrada:
print('=' * 80)
print('NUMEROS PARES DE 0 A 100:')
print('=' * 80)

# Declarações:
contagem = 0

for c in range (0, 101):
     if ( c % 2 == 0):
          contagem += 1

print (f'De 0 a 100 possui : {contagem} numero de pares.')     

# Texto de saida:
print('='* 80)
print('FIM DO PROGRAMA')
print('=' * 80)