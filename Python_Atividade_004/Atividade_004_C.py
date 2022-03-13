#Curso técnico de informática
#Autor: Denilsom Lobo
#Data de início: 04/11/2021
#Término: 04/11/2021
#Atividade 004: Letra C.

#Programa de medição de velocidade

#Limpar o terminal 
import os
os.system('cls')

#Texto de entrada:
print('='*40)
print('RADAR DE CARRO')
print('='*40)
print()

#Entrada de dados
velocidade = int(input('Insira a velocidade do seu carro: '))

#Condicionais:
print('-'*40)
if (velocidade > 60 ):
    print('Limite de velocidade acima do permitido')
elif (velocidade < 0):
    print('Erro de valor de velocidade.')
else:
    print(f'Velocidade normal !')
print()

#Saída:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)