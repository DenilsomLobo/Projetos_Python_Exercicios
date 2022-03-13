
#Importando as biblitecas
import os



#classes:

class Triangulo:
    valor1 = 0
    valor2 = 0
    valor3 = 0

    # Método construtor
    def __init__(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3
    
    # Métodos
    def validando(valor1, valor2, valor3):    
            if (valor1 <= 0) or (valor2 <= 0) or (valor3 <= 0):
                print('Valor inválido !')
            elif ((valor1 - valor2 ) < valor3 < (valor1 + valor2)):
                print('Forma um triângulo.')
            elif ((valor2 - valor3) < valor1 < (valor2 + valor3)):
                print('Forma um triângulo.')
            elif ((valor1 - valor3) > valor3 > (valor1 + valor3)):
                print('Forma um triângulo.')
            else:
                print('Não forma um triângulo.')

    # Limpar tela:     
    def limpar_tela():
        os.system('cls')
    
