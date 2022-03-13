#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 13/11/2021
#Término: 13/11/2021
#Atividade 006: Letra A.

#Programa que recebe um nome completo da pessoa e depois lista ele 
#separadamente.

# Importando as bibliotecas:
import os

#Limpar terminal
os.system('cls')

#Texto de entrada:
print('='*80)
print('PROGRAMA QUE SEPARA O NOME:')
print('='*80)

#Entrada de Dados:
nome = str(input('Insira um nome completo: '))

#Conversão de string:
dividirNome= nome.split()

#Saída:
print('-'*80)
print(f'O nome é: {dividirNome[0]}')
print(f'O nome do meio é: {dividirNome[1]}')
print(f'O sobrenome é: {dividirNome[len(dividirNome)-1]}')

#Texto de saida:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
