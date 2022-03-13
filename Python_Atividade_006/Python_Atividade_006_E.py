#Curso Técnico de informática
#Autor: Denilsom Lobo   
#Data de início: 13/11/2021
#Término: 13/11/2021
#Atividade 006: Letra E.

#Programa que recebe uma frase e mostra quantas vogais possui na frase.

# Importando as bibliotecas:
import os

#Limpar terminal
os.system('cls')

#Texto de entrada:
print('='*80)
print('PROGRAMA QUE MOSTRA QUANTAS VOGAIS POSSUI NA FRASE:')
print('='*80)

#Entrada de Dados:
frase = str(input('Insira uma frase: '))

#Conversão de string:
fraseMaiuscula = frase.lower()

#Contagem de caracteres:
contagemVogaisA = fraseMaiuscula.count('a', 0, )
contagemVogaisE = fraseMaiuscula.count('e', 0, )
contagemVogaisI = fraseMaiuscula.count('i', 0, )
contagemVogaisO = fraseMaiuscula.count('o', 0, )
contagemVogaisU = fraseMaiuscula.count('u', 0, )

#Operações
resultado = contagemVogaisA + contagemVogaisE + contagemVogaisI \
+ contagemVogaisO + contagemVogaisU

print('-'*80)
print(f'A frase possui a: {resultado} numero de vogais.')

#Texto de saida:
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
