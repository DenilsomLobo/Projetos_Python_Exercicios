# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 05/02/2022
# Data do término: 05/02/2022
# Atividade 011: Letra A

# Crie uma função que receba uma lista de números. Depois retorne duas listas
# com os números pares, os números ímpares, a quantidade de números pares e
# quantidade de números ímpares.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Função:


def filtragem_listas(*listas):
    """[Função que recebe uma lista e filtra os pares dos impares.]
    Args:
        listas    ([int]): [lista dos numeros]

    Returns:
        listaPar    ([int]): [lista dos pares]
        listaImpar    ([int]): [lista dos impares]
        contagemPar    ([int]): [lista contagem de par
        contagemImpar ([int]): [lista contagem de impar]
    """
    listaPar = []
    listaImpar = []
    contagemPar = 0
    contagemImpar = 0
    for i, c in enumerate(listas):
        if (c % 2 == 0):
            listaPar.append(c)
            contagemPar += 1
        else:
            listaImpar.append(c)
            contagemImpar += 1

    return listaPar, listaImpar, contagemPar, contagemImpar


# Declaração:
lista = []

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()
print('Crie uma lista com 10 numeros: ')
print()
print('-'*70)
print()

# Estrutura de repetição lista:
for c in range(0, 10):
    numero = int(input(f"{c + 1}ª. Insira um numero: "))
    lista.append(numero)

# Invocando função:
lp,li,ci,cp = filtragem_listas(*lista)

# Saida de dados:
print('Resultado da função: ')
print('-'*80)
print()
print(f'Está e a sua lista: {lista}')
print()
print(f'Está e a lista de par: {lp}')
print()
print(f'Está e a lista de impar: {li}')
print()
print(f'Está e a contagem de numeros par na lista: {cp}')
print()
print(f'Está e a contagem de numeros impar na lista: {ci}')
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
