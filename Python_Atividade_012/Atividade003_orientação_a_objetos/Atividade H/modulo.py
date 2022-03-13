#Importando as biblitecas
import os



#classes:

class Taboada:
    a = 0
    

    # Método construtor
    def __init__(self, a, b):
        self.a = a
        
    
    # Método para encontrar Delta e as raízes
    def mutiplicar(a):
        print('-'*48)
        print(f'A TABUADA DE: {a}')
        print('-'*48)
        print(f'{a} x 1 = {a * 1}')
        print(f'{a} x 2 = {a * 2}')
        print(f'{a} x 3 = {a * 3}')
        print(f'{a} x 4 = {a * 4}')
        print(f'{a} x 5 = {a * 5}')
        print(f'{a} x 6 = {a * 6}')
        print(f'{a} x 7 = {a * 7}')
        print(f'{a} x 8 = {a * 8}')
        print(f'{a} x 9 = {a * 9}')
        print(f'{a} x 10 = {a * 10}')
        print('-'*48)    
            

    # Limpar tela:     
    def limpar_tela():
        os.system('cls')
        
    # Final:
    def final():
        print('='*80)
        print('Fim do programa')
        print('='*80)
        print()