# Curso Técnico de informática
# Autor: Denilsom Lobo   
# Data de início: 18/11/2021
# Término: 18/11/2021
# Atividade 007: Letra I.

# Programa que fica em looping te que o usuario use uma tecla para cancelar.

# Importando as bibliotecas:
import os


# Limpar terminal
os.system('cls')

# Texto de entrada:
print('=' * 80)
print('INICIO DO PROGRAMA:')
print('=' * 80)

# Entrada:
while (True):
    loop = str(input('Estamos em Looping até que você digite a telca "f": ')).lower().strip()
    if (loop != 'f'):
        print()
        print('ESTAMOS EM LOOPING !!!')
        print()
    else:
        print('-'*80)
        print('Você digitou "f" para sair. O Looping acabou...')
        break

# Texto de saida:
print('='* 80)
print('FIM DO PROGRAMA')
print('=' * 80)