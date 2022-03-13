# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 27/11/2021
# Data de termino: 28/11/2021
# Atividade 008: Letra H

# Programa que ler uma quantidade indetermnada de notas.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declaração:
listaDeNotas = []
soma = 0
# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

flag = True 
# Estrutura de repetição de entrada de dados:
while (True):
    nota = input('Digite as nota que deseja adicionar a lista de notas: ')
    if(not(nota.isnumeric()) or int(nota) < 0 ):
        print()
        print(f'Entrada inválida, digite novamente ...')
        print()
    else:
         # Casting
        nota = int(nota) 
        # Adicionando a Lista de Notas
        listaDeNotas.append(nota)
        flag = True
       # Estrutura de repetição de confirmação:
        while (flag == True):
            print()
            continuar = input('Deseja continuar (s/0): ').lower()
            if (continuar != 's' and continuar != '0'):
                print('Digite "s" ou "n"...')
                
            else:
                if(continuar =='s'):
                    os.system('cls')                    
                    break
                elif(continuar =='n'):
                    print('-'*70)
                    print(f'Esta e a sua Lista : {listaDeNotas}')
                    print('-'*70)
                # Estrutura de repetição de operações:
                for i, numero in enumerate(listaDeNotas):
                        # Declarações:
                        soma += numero
                        tamanhoLista = len(listaDeNotas)
                        media = soma / tamanhoLista
                        listaInvertida = listaDeNotas[::-1]
                # Texto de Saida: 
                print('-'*80)
                print(f'Quantidade de Notas na sua lista é: {tamanhoLista} ')
                print()
                print(f'A sua lista de notas é: {listaDeNotas} ')
                print('')
                print(f'A sua lista de nota inversa é: ')
                print('-'*31)
                #Estrutura de repetição de print de lista:
                for i, nota in enumerate(listaInvertida):
                    print(f'Na entrada: {i} | A nota foi: {nota}')
                print('-'*31)
                print (f'A soma da sua lista de notas é: {soma}')
                print()
                print(f'A media das notas são: {media}')
                print()
                print('='*80)
                print('FIM DO PROGRAMA')
                print('='*80)
                exit()

