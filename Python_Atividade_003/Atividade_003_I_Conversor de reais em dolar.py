#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data início: 28/10/2021
#Término: 28/10/2021
#Atividade 003: Exercicio I = Tabuada de mutiplicação.

#Progama que recebe um valor e converte em dolar.
#Entrada:
#Texto:
print('-'*40)
print('CONVERSOR DE REAIS EM DOLAR')
print('='*40)

#Entrada de dados:
a = float(input('Por favor, insira um valor em reais: '))

#Operações:
#Considerando a conversão com o valor do dolar em : USD: 5,6123998  
#Atualizado dia: 29/10/2021 | Fonte:Banco Central do Brasil
conversao = a / 5.6123998 

#Saída:
print('-'*40)
print(f'Com {a} BRL da para comprar: {conversao:.4f} USD')

#Texto de encerramento:
print('-'*40)
print('FIM DO PROGRAMA')
print('='*40)
