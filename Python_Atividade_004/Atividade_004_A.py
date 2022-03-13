#Curso técnico de informática
#Autor: Denilsom Lobo
#Data de início: 04/11/2021
#Término: 04/11/2021
#Atividade 004: Letra A

#Programa de validação de numeros inteiros e par ou impar.

#Limpar o terminal
import os
os.system('cls')

#Texto de entrada
print('='*40)
print('PROGRAMA PARA SABER SE E IMPAR OU PAR:')
print('='*40)

#Entrada de dados
valor = int(input('insira um valor: '))
print()
print('-'*40)
print() 

#condicionais 
if (valor % 2 ==  0):
    print(f'O valor digitado: {valor}, e par !')
else:
    print()
    print( f'O valor digitado: {valor} e impar ! ')

#Saida
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)