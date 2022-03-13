#Curso técnico de informáica
#Autor: Denilsom Lobo
#Data de início: 05/11/2021
#Término: 05/11/2021
#Atividade 004: Letra F

#Programa para identificar se o ano e bissexto
 # Importando as bibliotecas:
from modulo import Validacao

conversao = Validacao
ls = Validacao

#Limpar terminal:
ls.limpar_tela()

#Texto de entrada:
print('='*40)
print('PROGRAMA PARA CALCULAR SE O ANO E BISSEXTO')
print('='*40)

#Entrada de dados:
flag = True
while(True):    
    a = input('Insira o ano que quer saber:  ')
    if (not(a.isnumeric())):
        print('Digite apenas o numeros inteiros')   
    else:
        a = int(a)
        break

conversao.validacaoano(a)

#Texto de saida:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)
    
