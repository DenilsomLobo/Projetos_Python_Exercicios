#Curso técnico de informáica
#Autor: Denilsom Lobo
#Data de início: 05/11/2021
#Término: 05/11/2021
#Atividade 004: Letra F

#Programa para identificar se o ano e bissexto

#Limpar terminal:
import os
os.system('cls')

#Texto de entrada:
print('='*40)
print('PROGRAMA PARA CALCULAR SE O ANO E BISSEXTO')
print('='*40)

#Entrada de dados:
ano = int(input('Insira o ano que quer saber: '))

#Condicionais:
print('-'*40)
if (ano <= 0):
    print('{ano} inválido !')
elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 ==0):
    print(f'O {ano} e bissexto !')
else:
    print(f'O {ano} não e bissexto !')

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)
    
