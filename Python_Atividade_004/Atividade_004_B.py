#Curso técnico de informática
#Autor: Denilsom Lobo
#Data de início: 04/11/2021
#Término: 04/11/2021
#Atividade 004: B

#Programa que pede 3 valores e mostra do maior para o menor

#Limpar o terminal
import os
os.system('cls')

#Texto de entrada:
print('='*40)
print('PROGRAMA DE MEDIÇÃO DE VALORES')
print('='*40)

#Entradade dados:
valor1 = (input('Insira o valor 1: '))
valor2 = (input('Insira o valor 2: '))
valor3 = (input('Insira o valor 3: '))

#Condicionais
print('-'*40)
if (valor1 > valor2) and (valor1 > valor3):
   print (f'o {valor1} e o maior')
elif (valor2 > valor1) and (valor2 > valor3):
   print (f'O {valor2} e o maior')
elif (valor3 > valor1) and (valor3 > valor2):
   print (f'O {valor3} e o maior')

if (valor1 < valor2) and (valor1 < valor3):
   print (f'o {valor1} e o menor')
elif (valor2 < valor1) and (valor2 < valor3):
   print (f'O {valor2} e o menor')
elif (valor3 < valor1) and (valor3 < valor2):
   print (f'O {valor3} e o menor')
else:
   print('-'*40)
   print('Os demais valores são iguais')
   print('-'*40)

#Saida
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)