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
listaDeNomes = []

print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

flag = True
while (True):
    nome = input('Digite os nomes: ').strip()
    if (nome != str(nome)):
        print()
        print(f'Entrada inválida, digite novamente ...')
        print()
    else:
         # Casting
        nome = str(nome)
        # Adicionando a lista
        listaDeNomes.append(nome)
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
                    print(f'Esta e a sua lista de nomes : {listaDeNomes}')
                    print('-'*70)
                for i, nomeI in enumerate(listaDeNomes):
                        print(f'No Indice: {i} = Nome: {nomeI}')
                
                print('='*80)
                print('FIM DO PROGRAMA')
                print('='*80)
                exit()

