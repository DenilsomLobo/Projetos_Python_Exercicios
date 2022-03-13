# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 26/11/2021
# Data de termino: 26/11/2021
# Atividade 008: Letra A

# Programa que insere valor que falta a uma lista.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')


# Entrada de dados:
lista = [1, 2, 3, 5, 6]
soma = 0
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print(f'Na lista {lista} qual numero que falta ? ')
print('-'*80)

# Estrutura de repetição:
flag = True
while (True):
    add = input('Digite os numeros para adcionar na lista: ')
    if(not(add.isnumeric()) or int(add) != 4 ):
        print()
        print(f'Entrada inválida, digite novamente ...')
        print()
    else:
         # Casting
        add = int(add) 
        # Adicionando a lista
        pos = 0
        while pos < len(lista):
            if add <= lista[pos]:
                lista.insert(pos, add)
                break
            pos += 1
        # Estrutura de repetição de confirmação:
        flag = True
        
        while (flag == True):
            print()
            continuar = input('Deseja continuar (s/n): ').lower()
            if (continuar != 's' and continuar != 'n'):
                print('Digite "s" ou "n"...')
                
            else:
                if(continuar =='s'):
                    os.system('cls')                    
                    break
                elif(continuar =='n'):
                    print('-'*70)
                    # Saida de dados:
                    print(f'Está e a sua Lista : {lista}')
                    print('-'*70)
                print('='*80)
                print('FIM DO PROGRAMA')
                print('='*80)
                exit()
