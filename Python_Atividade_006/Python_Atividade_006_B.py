#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 13/11/2021
#Término: 13/11/2021
#Atividade 006: Letra B.

#Programa que recebe um nome "João da Silva" e troca o "Silva" pelo "Oliveira"

# Importando as bibliotecas:
import os

#Limpar terminal
os.system('cls')

#Texto de entrada:
print('='*50)
print('PROGRAMA QUE RECEBE O NOME "JOÃO DA SILVA" E TROCA PELO "OLIVEIRA"')
print('='*50)

#Entrada de Dados:
nome = 'João da Silva'
nomeAlterado = nome.replace('Silva', 'Oliveira')

#Saída:
print('-'*50)
print(f'Seu nome era: {nome}')
print(f'Seu nome novo é : {nomeAlterado}')

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)
