#Curso técnico de informática
#Autor: Denilsom Lobo
#Data de início: 05/11/2021
#Término: 05/11/2021
#Atividade 004: Letra H.

# Importando as bibliotecas:
from modulo import Equacao

# Declaração:
a = Equacao.a
b = Equacao.b
c = Equacao.c
delta = Equacao.delta(a,b,c)
bhaskara1 = Equacao.bhaskara_1(a,b,delta)
bhaskara2 = Equacao.bhaskara_2(a,b,delta)
ls = Equacao

#Programa que calcula equação de segundo grau.

#Limpar tela:
ls = Equacao.limpar_tela()

#Texto de entrada:
print('='*40)
print('PROGRAMA QUE CALCULA EQUAÇÃO 2º DE X² -6X +5')
print('='*40)


#Saida:
print(f'Os valores de da equanção são {a} , {b} e {c}')
print('-'*40)
print(f'O Delta dessa equanção e : {delta}')
print(f'Como Delta podemos fazer a forma de bhaskara para achar a raíz x1 e x2')
print('-'*40)
print(f'X1 = {bhaskara1}')
print(f'X2 = {bhaskara2}')
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)
