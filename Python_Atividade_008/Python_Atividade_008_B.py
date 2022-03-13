# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 26/11/2021
# Data de termino: 26/11/2021
# Atividade 008: Letra B

# Programa que cria uma lista com 5 numeros e depois soma eles.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')


# Entrada de dados:
lista = []
soma = 0

print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print('Vamos criar uma lista com 5 numeros inteiros:')

# Estrutura de repetição:
for c in range (0, 5):
    numero = input('Insira um numero: ')
    if (not(numero.isnumeric()) or int(numero) < 0 ):
        print('Numero invalido ...')
        exit()
    else:
        numero = int(numero)
        lista.append(numero)
        soma += numero


# Saida:
print('-'*80)
print(f'Sua lista é : {lista}')
print()
print(f'A soma dela é: {soma}')
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)


