#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 13/11/2021
#Término: 13/11/2021
#Atividade 006: Letra A.

#Programa que recebe um nome, nome do meio e sobrenome, separadamente e mostra 
#o nome completo.

# Importando as bibliotecas:
import os

#Limpar terminal
os.system('cls')

#Texto de entrada:
print('='*50)
print('PROGRAMA QUE PEDE O NOME COMPLETO SEPARADAMENTE E MOSTRA ELE JUNTO:')
print('='*50)

#Entrada de Dados:
nome1 = str(input('Insira o primeiro nome: '))
nome2 = str(input('Insira o nome do meio: '))
nome3 = str(input('Insira o sobre nome: '))
nomeCompleto = nome1 + ' ' + nome2 + ' ' + nome3

#Saída:
print('-'*50)
print(f'Seu nome é : {nomeCompleto}')

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)
