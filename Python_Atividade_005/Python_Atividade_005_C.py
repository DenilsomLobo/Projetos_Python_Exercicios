#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data de início: 10/11/2021
#Término: 10/11/2021
#Atividade 005: Letra C.

#Programa que calcula potencia inserindo valores de base e o expoente.

#Importação:
#Limpar tela
import os
os.system('cls')

#Operações:
#Potencia
from math import pow

#Texto de entrada:
print('='*40)
print('PROGRAMA DE CALCULAR POTÊNCIA:')
print('='*40)

#Entrada de dados:
base = float(input('Insira a base: '))
expoente = float(input('Insira um expoente: '))
resultado = pow(base, expoente)

#Saida
print('-'*40)
print(f'Resultado da base de {base} com o expoente {expoente}')
print(f'e igual a = {resultado:.4f}')


#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)