#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data início: 28/10/2021
#Término: 28/10/2021
#Atividade 003: Exercicio H = Tabuada de mutiplicação.

#Progama que recebe um valor inteiro e mostra sua tabuada de mutiplicação.
#Entrada:

#importando as bibliotecas:
from modulo import Taboada

#declaração:

operacao = Taboada

lt = Taboada

# Limpando o terminal:
lt.limpar_tela()


#Texto:
print('-'*40)
print('TABUADA DE MUTIPLICAÇÃO')
print('='*40)

#Entrada de dados:
flag = True
while(True):    
    a = input('Por favor, insira um valor inteiro para fazer a tabuada: ')
    if (not(a.isnumeric())):
        print('Digite apenas o numeros inteiros')   
    else:
        a = int(a)
        break

resultado = Taboada.mutiplicar(a)

#Texto de encerramento:
print('FIM DO PROGRAMA')
print('='*40)


