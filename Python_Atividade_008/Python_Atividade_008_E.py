# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 26/11/2021
# Data de termino: 26/11/2021
# Atividade 008: Letra E

# Programa que leia as vogais e imprime elas

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:
listaDeVogais = ['a', 'e', 'i', 'o', 'u']
listaInversa = sorted(listaDeVogais, reverse = True)

print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

# Saida:

print(f'A sua lista de vogais em forma inversa é: {listaInversa}')
print('='*70)
print('Fim do programa !')
print('='*70)