#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data início: 27/10/2021
#Término: 27/10/2021
#Atividade 002: Cálculos aritméticos

#Entrada
#Texto de entrada:
print('='*40)
print('INSIRA OS DADOS PARA OS CÁLCULOS:')
print('-'*40) 

#Entrada de dados:
a = int (input('Entre com o primeiro valor: '))
b = int (input('Entre com o segundo valor: '))

#Entrada de cálculos:
#Soma
soma = a + b
#Subtração
subtracao = a - b
#Pruduto
produto = a * b
#Divisão
divisao = a / b
#Potencia
potencia = a ** b
#Divisão inteira
divisaoInteiros = a // b 
#Resto da divisão
restoDivisao = a % b
#Raiz quadrada
raizQuadrada = a ** (1/2)
raizQuadrada2 = b ** (1/2)
# Raiz cúbica 
raizCubica = a ** (1/3)
raizCubica2 = b ** (1/3)

#Saida
print('-'*40)
print('ESTUDO DE OPERADORES ARITMÉTICOS')
print('='*40)
print(f'O valor de {a} + {b} = {soma}')
print(f'O valor de {a} - {b} = {subtracao}')
print(f'O valor de {a} * {b} = {produto}')
print(f'O valor de {a} / {b} = {divisao}')
print(f'O valor de {a} ** {b} = {potencia}')
print(f'O valor de {a} // {b} = {divisaoInteiros}')
print(f'O valor de {a} % {b} = {restoDivisao}')
print(f'O valor de {a}√ = {raizQuadrada:.4f}')
print(f'O valor de  {b}√ = {raizQuadrada2:.4f}')
print(f'O valor de {a}∛ = {raizCubica:.4f}')
print(f'O valor de  {b}∛ = {raizCubica2:.4f}')
print('='*40)
print('Fim do programa !')
print('-'*40)