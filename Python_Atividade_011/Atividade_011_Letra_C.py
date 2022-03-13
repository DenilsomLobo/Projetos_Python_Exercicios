# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 05/02/2022
# Data do término: 05/02/2022
# Atividade 011: Letra A

# Crie uma função que verifica se uma aluno está cadastrado ou não em um
# dicionário. O dicionário deverá conter nome, matrícula e a data de nascimento
# do aluno.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')


# Função:
def validacao_Aluno(aluno, cadastro):
    """[Função que faz validação de aluno em lista de alunos]

    Args:
        aluno (dict): [Dicionario com o aluno]
        cadastro (List,Dict): [lista a ser verificada]
    """
    if aluno in cadastro:
        print('Aluno cadastrado')
    else:
        print('Aluno não cadastrado')


# Declaração
cadastroAlunos = [{'Nome': 'Denilsom', 'Matricula': 1, 'Data': '1994'},
                  {'Nome': "Vitor", "Matricula": 2, 'Data': '2003'}]
validacaoAluno = []
aluno = dict()

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print()

# Estrutura de repetição de entrada de dados:
print('Insira os dados do aluno novo: ')
print()
for c in range(0, 1):
    aluno['Nome'] = str(input('Nome: '))
    aluno['Matricula'] = int(input('Matricula: '))
    aluno['Data'] = str(input('Data de nacimento: '))
    aluno.copy()

# Saida de dados:
print()
print('Aluno a verificar:')
print(f'{aluno}')
print()
print('-'*70)
print()
print(f'Validação de cadastro: ')
validacao_Aluno(aluno, cadastroAlunos)
print()
print('-'*70)

# Estrutura de repetição de saida de dados:
print('lista de alunos cadastrados: ')
print()
for i, c in enumerate(cadastroAlunos):
    for chave, valor in c.items():
        print(f'{chave}:    {valor}')
    print()

# Texto de encerramento:
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
