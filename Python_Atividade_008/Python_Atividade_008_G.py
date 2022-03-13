# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 27/11/2021
# Data de termino: 27/11/2021
# Atividade 008: Letra G

# Programa que ler uma lista com 10 numeros depois mostrar o maior e o menor

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:
listaDeNumero= [5, 30, 3, 4, 7, 6, 20, 8, 1, 18]
maiorValor = max(listaDeNumero)
menorValor = min(listaDeNumero)

print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print(f'A sua lista: {listaDeNumero}')
print('-'*50)
print(f'O valor do maximo e: {maiorValor} ')
print()
print(f'O valor do minimo e: {menorValor}')
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)

