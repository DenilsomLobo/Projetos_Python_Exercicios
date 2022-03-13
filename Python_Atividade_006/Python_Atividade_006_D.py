#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 13/11/2021
#Término: 13/11/2021
#Atividade 006: Letra D.

#Programa que recebe uma frase e mostra em minúsculo, maiúsculo, quantidade de caracteres
#e quantas letras tem na segunda palavra na frase.

# Importando as bibliotecas:
import os

#Limpar terminal
os.system('cls')

#Texto de entrada:
print('='*80)
print('PROGRAMA QUE ANALIZA UMA FRASE:')
print('='*80)

#Entrada de Dados:
frase = str(input('Insira uma frase: '))

#Conversão de string:
fraseMinusculo = frase.lower()
fraseMaiuscula = frase.upper() 
dividirFrase = frase.split()

#Contagem de caracteres:
contagemFrase = len(frase)
contagemPalavra2 = len(dividirFrase[1])

#Saída:
print('-'*80)
print(f'A frase em minúsculo ficaria: {fraseMinusculo}')
print(f'A frase em maiúsculo ficaria: {fraseMaiuscula}')
print(f'A quantidade de caracteres na frase é igual: {contagemFrase}')
print(f'A quantidade de Letras na segunda palavra é : {contagemPalavra2}')

#Texto de saida:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
