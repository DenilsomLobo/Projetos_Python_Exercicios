
#Importando as biblitecas
import os



#classes:

class Validacao:
    a = 0
    # Método construtor
    def __init__(self, a, ):
        self.a = a
        
    
    # Métodos
    def validacaoano(a):    
        if (a <= 0):
            print('{a} inválido !')
        elif (a % 4 == 0 and a % 100 != 0) or (a % 400 ==0):
            print(f'O {a} e bissexto !')
        else:
            print(f'O {a} não e bissexto !')

    # Limpar tela:     
    def limpar_tela():
        os.system('cls')
    
