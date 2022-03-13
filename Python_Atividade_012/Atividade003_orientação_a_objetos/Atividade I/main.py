#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data início: 28/10/2021
#Término: 28/10/2021
#Atividade 003: Exercicio I = Tabuada de mutiplicação.

#Progama que recebe um valor e converte em dolar.

# Importando as bibliotecas:
from modulo import Conversor

# Declarações:
conversao = Conversor

lt = Conversor

# Limpando o terminal:
lt.limpar_tela()

#Entrada:
#Texto:
print('-'*40)
print('CONVERSOR DE REAIS EM DOLAR')
print('='*40)

#Entrada de dados:
flag = True
while(True):
    try:
        print()
        a = float(input('insira o valor que deseja converter em Dolar: '))
        break
    except ValueError:
        print('Erro de entrada de Valor !. Apenas numeros inteiros e flutuantes.')
        print()
    print()

resultado = conversao.converter(a)

#Saída:
print('-'*40)
print(f'Com {a} BRL da para comprar: {resultado:.4f} USD')

#Texto de encerramento:
print('-'*40)
print('FIM DO PROGRAMA')
print('='*40)