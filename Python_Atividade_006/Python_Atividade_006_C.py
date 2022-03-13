#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 13/11/2021
#Término: 13/11/2021
#Atividade 006: Letra C.

#Programa que recebe um nome e verifica se existe "Oliveira" no nome.

# Importando as bibliotecas:
import os

#Limpar terminal
os.system('cls')

#Texto de entrada:
print('='*50)
print('PROGRAMA QUE VERIFICA SE EXISTE "OLIVEIRA" NO NOME:')
print('='*50)

#Entrada de Dados:
nome = str(input('Insira um nome: '))

#Verificação:
verificacao = 'Oliveira' in nome

#Condicionais:
if (verificacao == True):
    print(f'O nome: {nome}, o resultado e verdadeiro.')
else:
    print(f'O nome: {nome}, o resultado e falso.')

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)
