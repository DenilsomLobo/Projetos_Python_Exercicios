
#Importando as biblitecas
from calendar import c
import os



#classes:

class Equacao:
    a = 1
    b = -6
    c = 5  
    d = (b ** 2) - 4 * a * c
    # Método construtor
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c       
        self.d = d
    # Métodos
    def delta (a,b,c):
        delta = (b ** 2) - 4 * a * c
        return delta
        
    def bhaskara_1 (a,b,d):
        try:
            bk_1 = ((-1 * b) + (d ** (1/2))) / (2*a)
            return bk_1
        except ZeroDivisionError:
            return 'Erro ! Não foi possivel fazer uma divisão por zero'

    def bhaskara_2 (a,b,d):
        try:
            bk_2 = ((-1 * b) + (d ** (1/2))) / (2*a)
            return bk_2
        except ZeroDivisionError:
            return 'Erro ! Não foi possivel fazer uma divisão por zero'
            
            

    # Limpar tela:     
    def limpar_tela():
        os.system('cls')
 