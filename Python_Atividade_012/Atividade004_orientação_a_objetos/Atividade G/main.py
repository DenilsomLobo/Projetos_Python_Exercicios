#Curso técnico de informática
#Autor: Denilsom Lobo
#Data de início: 05/11/2021
#Término: 05/11/2021
#Atividade: Letra G.

#Programa que diz se os valores forma um triângulo ou não.

# Importando as bibliotecas:
from modulo import Triangulo

# Delcaração

validar = Triangulo
ls = Triangulo

#Limpar terminal:
ls.limpar_tela()

#Texto de entrada:
print('='*40)
print('PROGRAMA QUE VALIDA TRIÂNGULOS')
print('='*40)

flag = True
while(True):
    try:
        print()
        valor1 = float(input('Insira o primeiro valor: '))
        break
    except ValueError:
        print('Erro de entrada de Valor !. Apenas numeros inteiros e flutuantes.')
        print()
    print()
while(True):
    try:
        print()
        valor2 = float(input('Insira o segundo valor: '))
        break
    except ValueError:
        print('Erro de entrada de Valor !. Apenas numeros inteiros e flutuantes.')
        print()
while(True):
    try:
        print()
        valor3 = float(input('Insira o terceiro valor: '))
        break
    except ValueError:
        print('Erro de entrada de Valor !. Apenas numeros inteiros e flutuantes.')
        print()
    print()

print()
validar.validando(valor1,valor2,valor3)
print()

#Texto de saída:
print('='*40)
print('FIM DO PROGRAMA')
print('='*40)