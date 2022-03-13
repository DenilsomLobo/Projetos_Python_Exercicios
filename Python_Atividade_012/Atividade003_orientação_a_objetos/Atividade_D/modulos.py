#Importando as biblitecas
import os



#classes:

class Divisao:
    a = 0
    b = 0

    # Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Método para encontrar Delta e as raízes
    def dividir(a, b):
        try:
            x1 = a / b
            return x1
        except ZeroDivisionError:
            return 'Erro ! Não foi possivel fazer uma divisão por zero'
            
            

    # Limpar tela:     
    def limpar_tela():
        os.system('cls')
    # Titulo:
    def titulo():
        print('='*80)
        print('Inicio do programa')
        print('='*80)
        print()
    # Final:
    def final():
        print('='*80)
        print('Fim do programa')
        print('='*80)
        print()
    # painel
    def painel():   
        print("""
         ____________________________________________   
        | Digite um numero para definir uma função   |
        | para a calculadora:                        |
        |                                            |
        | 1 = Divir                                  |               
        |                                            |
        |               0 = SAIR                     |
        |____________________________________________|
        """)
