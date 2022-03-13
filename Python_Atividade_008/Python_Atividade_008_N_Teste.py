# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 28/11/2021
# Data de termino: 28/11/2021
# Atividade 008: Letra N

# Programa que sorteia numeros da Mega Sena e da lotofácil.

# Importando as bibliotecas:
import os
import copy
from random import randint

# Limpando o terminal:
os.system('cls')

# Entrada de dados:
ApostaMega = []
ApostaLoto = []

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

# Etrutura de repetição da entrada da aposta mega sena:
for c in range (0, 6):
    while (True):
        megaAdd = input('Digite os numeros que você quer apostar: ')
        if(not(megaAdd.isnumeric()) or int(megaAdd) < 0 or int(megaAdd) > 60):
            print()
            print(f'Entrada inválida, digite novamente ...')
            print()
        else:
            megaAdd = int(megaAdd)
            if megaAdd in ApostaMega:
                print('Este numero ja foi apostado ...')
                continue
            elif megaAdd not in ApostaMega:
                ApostaMega.append(megaAdd)
                break      
# Etrutura de repetição da entrada da aposta mega sena:
print('-'*80)
print('Agora vamos apostar a Loto facil:')
print('-'*80)
for c2 in range (0, 15):
    while (True):
        lotoAdd = input('Digite os numeros que você quer apostar: ')
        if(not(lotoAdd.isnumeric()) or int(lotoAdd) < 0 or int(lotoAdd) > 25):
            print()
            print(f'Entrada inválida, digite novamente ...')
            print()
        else:
            lotoAdd = int(lotoAdd)
            if lotoAdd in ApostaLoto:
                print('Este numero ja foi apostado ...')
                continue
            elif lotoAdd not in ApostaLoto:
                ApostaLoto.append(lotoAdd)
                break      
# Declaração:
listaDeNumerosMega = []
listaDeLotofacil = []

# Estrutura de repetição de numeros aleatorios:
# Mega Sena:
for c3 in range (0, 6):
    # Validações de numeros repetidos:
    while (True):
        numerosAleatoriosMega = randint (0, 60)
        if numerosAleatoriosMega in listaDeNumerosMega:
            continue
        else:
            numerosAleatoriosMega not in listaDeNumerosMega
            listaDeNumerosMega.append(numerosAleatoriosMega)
            break
# Lotofácil:     
for c4 in range (0, 15):
    # Validações de numeros repetidos:
    while (True):
        numerosAleatoriosLoto = randint (0, 25)
        if numerosAleatoriosLoto  in listaDeLotofacil:
            continue
        else:
            numerosAleatoriosLoto not in listaDeLotofacil
            listaDeLotofacil.append(numerosAleatoriosLoto)
            break
         
# Fatiamento de listas
listaCopiada = copy.copy(listaDeNumerosMega)
listaCopiada2 = copy.copy(listaDeLotofacil)
listaCrescenteMega = sorted(listaCopiada)
listaCrescenteLoto = sorted(listaCopiada2)
megasena = listaCrescenteMega [0: ]
lotofacil = listaCrescenteLoto [0: ]

# Texto de saida:
print('='*80)
print('O RESULTADO DO SORTEIO DA MEGA SENA FOI !!!')
print('='*80)
print()
print(f'Os numeros da Mega sena sorteados foi: {listaDeNumerosMega}')
print()
print(f'Anote os numeros: {megasena}')
print()
print('-'*80)
print()
print(f'Os numeros da Lotofácil sorteados foi: {listaDeLotofacil}')
print()
print(f'Anote os numeros: {lotofacil}')
print()
print('='*80)
print()
print(f'Sua aposta foi da mega sena foi:{ApostaMega}')
print()
print()
print(f'Sua aposta da lotofácil foi: {ApostaLoto}')
# Futuramente uma verificação de quantos numeros acertou e se ganhou ou não.
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)






