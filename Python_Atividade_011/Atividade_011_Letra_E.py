# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 06/02/2022
# Data do término: 06/02/2022
# Atividade 011: Letra E

# Crie uma função que receba a altura e o peso de uma pessoa.
# Depois retorne o seu IMC.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Função:
def calcular_Imc(altura,peso):
    """[Função que calcula o IMC]

    Args:
        altura ([float]): [description]
        peso ([float]): [description]

    Returns:
        [float]: [description]
    """

    imc = peso / (altura ** 2)
    return imc


# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Entrada de dados:
print('Insira os dados do aluno: ')
print()
alt = float(input('Insira a altura em metros: '))
print()
kg = float(input('Insira o peso: '))
print()

# Invocando a função:
retorno = calcular_Imc(alt,kg)

# Saida de dados:
print('-'*80)
print()
print(f'O IMC do aluno é: {retorno}')

# Texto de encerramento:
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)