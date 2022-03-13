#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 13/11/2021
#Término: 13/11/2021
#Atividade 006: Letra H.

#Programa que recebe um nome e mostra quantas vezes a letra "o" aparece e 
#que posição ela aparece na primeira e ultima vez.

# Importando as bibliotecas:
import os

#Limpar terminal
os.system('cls')

#Texto de entrada:
print('='*80)
print('PROGRAMA QUE RECEBE UM NOME E LISTA A LETRA "O":')
print('='*80)

#Entrada de Dados:
nome = str(input('Insira um nome: '))

#Conversão de string:
nomeMinusculo = nome.lower()

#Contagem:
contagemO = nomeMinusculo.count('o', 0, )
posicao1 = nomeMinusculo.find('o')
posicao2 = nomeMinusculo.rfind('o')

#Saída:
print('-'*80)
print(f'O nome é: {nome}')
print()
print(f'Numeros que aparece a letra "o": {contagemO}')
print(f'A primeira vez que aparece a letra "o" e: {posicao1}')
print(f'A ultima vez que aparece a letra "o" foi: {posicao2}')

#Texto de saida:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
