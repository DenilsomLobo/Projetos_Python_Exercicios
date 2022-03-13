# Curso Técnico de informática
# Autor: Denilsom Lobo   
# Data de início: 18/11/2021
# Término: 18/11/2021
# Atividade 007: Letra B.

#Programa que imprime os numero em um intervalo de 1 a 100.

# Importando as bibliotecas:
import os


# Limpar terminal
os.system('cls')

# Texto de entrada:
print('=' * 80)
print('CONTAGEM DE 1 - 100')
print('=' * 80)
inicio = (input('Valor inicial ? '))
final = (input('Qual valor quer o final ? '))

if (not(inicio.isnumeric()) and not(final.isnumeric())):
    print('Valor invalido!')
    
else:
    #casting:
    inicio = int(inicio)
    final = int(final)

    for c in range(inicio, final + 1):
        print(f'Contagem: {c}')
        print()


# Texto de saida:
print('='* 80)
print('FIM DO PROGRAMA')
print('=' * 80)

