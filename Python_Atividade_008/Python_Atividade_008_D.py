# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 26/11/2021
# Data de termino: 26/11/2021
# Atividade 008: Letra D

# Programa que preencha uma listaDeNotas com as notas de 4 alunos e imprime a media

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Entrada de dados:
listaDeNotas = []
soma = 0
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

for c in range(0, 4):
    nota= input(f'insira o valor da nota {c+1}ª: ')
    if (not(float(nota)  > 0)) or (float(nota) < 0):
        print('Valor invalido...')
        exit()
    else:
        nota = float(nota)
        # GUardando em uma lista
        listaDeNotas.append(nota)
        soma += nota
        media = soma / 4

# Texto de saida:
print('-'*80)
print(f'A sua lista de notas é: {listaDeNotas}')
print(f'A soma das notas são: {soma}')
print(f'A media das notas é: {media}')
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)