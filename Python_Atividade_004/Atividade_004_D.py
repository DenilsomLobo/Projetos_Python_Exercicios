#Curso técnico de informática
#Autor: Denilsom Lobo
#Data de início: 04/11/2021
#Término: 04/11/2021
#Atividade 004: letra D.

#Programa que cálcula aumento salarial dos funcionários.

#Limpar terminal:
import os
os.system('cls')

#Texto de entrada
print('='*40)
print('PROGRAMA DE REAJUSTE DE AUMENTO SALARIAL')
print('='*40)
print()

#Entrada
salario = float(input('Insira o valor do seu salário: '))

#Condicionais:

print('-'*40)

if (salario <= 0):
    print('Valor incorreto !')
elif (salario >= 1500):
    print(f'Seu aumento salarial sera de: R$ {salario*5/100}')
elif (salario <= 1000):
    print(f'Seu aumento salarial sera de: R$ {salario*10/100}')
else:
    print('Erro.') 

print()

#Saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)