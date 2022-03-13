#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data de início: 10/11/2021
#Término: 10/11/2021
#Atividade 005: Letra F.

#Programa de adivinhação de numero de 1 a 3.

#Importação:
#Limpar tela
import os
os.system('cls')

#Randomizador
from random import randint

#Texto de entrada

print('='*40)
print('PROGRAMA DE ADIVINHAÇÃO DE 1 A 3:')
print('='*40)

#Entrada de dados:
numeroNpc = randint (1,3)
numeroUser = int(input('Qual o numero de 1 a 3 estou pensando ? '))
print('-'*40)

#condicionais:
if (numeroUser != 1) and (numeroUser != 2) and (numeroUser != 3):
    print('Numero digitado invalido !')
    exit()
else:
    print(f'O numero que eu pensei .......... " {numeroNpc} !"')
    print('-'*40)
if (numeroUser == numeroNpc):
    print('Parabens Você acertou ! Temos um vencedor !')
elif (numeroUser != numeroNpc):
    print('Infelizmente você não acertou. Você perdeu !')
else:
    print('Que estranho empantou ...')

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)