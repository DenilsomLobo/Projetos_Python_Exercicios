# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 21/02/2022
# Data do Término: 21/02/2022
# Atividade 003 - letra: D

# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

# Importando as bibliotecas:
from modulos import Divisao
import time

# instanciando o objeto
init = Divisao
end = Divisao
painel = Divisao
lt = Divisao
dividir = Divisao

# Limpando a tela
lt.limpar_tela()

# Inicio do programa
init.titulo()


flag = True
while(True):
    lt.limpar_tela()
    painel.painel()
    escolha = input('Qual escolha deseja ? ')
    if (not(escolha.isnumeric())) or (int(escolha) < 0) or (int(escolha) >2):
        print('Digite apenas o numero 1 ou 0.')
        lt.limpar_tela()
    else:
        escolha = int(escolha)
        
    if (escolha == 1):
        flag = True
        while(True):
            try:
                print()
                numero_1 = float(input('insira o primeiro numero: '))
                break
            except ValueError:
                print('Erro de entrada de Valor !. Apenas numeros inteiros e flutuantes.')
                print()
            print()
        while(True):
            try:
                print()
                numero_2 = float(input('insira o segundo numero: '))
                break
            except ValueError:
                print('Erro de entrada de Valor !. Apenas numeros inteiros e flutuantes.')
                print()
            print()
        print()    
        resultado = dividir.dividir(numero_1, numero_2)
        print()
        print(f'O resultado do cálculo  foi: {resultado:.4f}')
        time.sleep(1.7)
        print()

    elif (escolha == 0):
        end.final()
        break





