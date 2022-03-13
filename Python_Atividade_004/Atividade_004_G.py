#Curso técnico de informática
#Autor: Denilsom Lobo
#Data de início: 05/11/2021
#Término: 05/11/2021
#Atividade: Letra G.

#Programa que diz se os valores forma um triângulo ou não.

#Limpar terminal:
import os
os.system('cls')

#Texto de entrada:
print('='*40)
print('PROGRAMA QUE VALIDA TRIÂNGULOS')
print('='*40)

#Entrada de dados:
valor1 = float(input('Insira o primeiro valor: '))
valor2 = float(input('Insira o segundo valor: '))
valor3 = float(input('Insira o terceiro valor: '))

#Condicionais:
print('-'*40)
if (valor1 <= 0) or (valor2 <= 0) or (valor3 <= 0):
    print('Valor inválido !')
elif ((valor1 - valor2 ) < valor3 < (valor1 + valor2)):
    print('Forma um triângulo.')
elif ((valor2 - valor3) < valor1 < (valor2 + valor3)):
    print('Forma um triângulo.')
elif ((valor1 - valor3) > valor3 > (valor1 + valor3)):
     print('Forma um triângulo.')
else:
     print('Não forma um triângulo.')

#Texto de saída:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)