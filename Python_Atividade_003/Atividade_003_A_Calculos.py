#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data início: 28/10/2021
#Término: 28/10/2021
#Atividade 003: Exercicio A = Cálculos

#Progama que recebe 3 valores e imprime a soma e a mutiplicação desse valores.
#Entrada:
#Texto:
print('-'*40)
print('CÁLCULADORA')
print('='*40)

#Valores:
a = float(input('insira o valor 1: '))
b = float(input('insira o valor 2: '))
c = float(input('insira o valor 3: '))

#Operações
soma = a + b + c
mutiplicacao = a * b * c

#Saída
print('-'*40)
print('RESULTADO:')
print('='*40)
print(f'O resultado da soma de {a} + {b} + {a} = {soma}')
print(f'O resultado da mutiplicação de {a} X {b} x {c} = {mutiplicacao}')

#Texto de encerramento:
print('-'*40)
print('FIM DO PROGRAMA')
print('='*40)