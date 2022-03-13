#Curso técnico de informática
#Autor: Denilsom Lobo
#Data de inicío: 05/11/2021
#Término: 05/11/2021
#Atividade 004: Letra F

#Programa que calcula a distância de juiz de fora a São Paulo.

#Limpa terminal:
import os 
os.system('cls')

#Texto de entrada:
print('='*40)
print('PROGRAMA DE CALCULADORA DE DISTANCIA DE JUIZ DE FORA A SÃO PAULO')
print('='*40)

#Entrada de dados:
distancia = float(input('Insira a distância em Km: '))

#Condicionais:
print('-'*40)
if (distancia <= 200):
    print(f'O valor sera cobrado pela passagem sera de: R$ {distancia * 0.70}')
elif (distancia >= 200):
    print(f'O valor sera cobrado pela passam sera de: R$ {distancia * 0.40}')
else:
    print('Erro !')

#Texto saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)