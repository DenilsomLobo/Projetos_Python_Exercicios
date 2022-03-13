#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data início: 28/10/2021
#Término: 28/10/2021
#Atividade 003: Exercicio C = Cálculadora de idade

#Progama que recebe o valor de 4 notas e cálcula a meda das notas.
#Entrada:
#Texto:
print('-'*40)
print('CÁLCULADORA DE NOTAS')
print('='*40)

#Entrada de dados:
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota.: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota..: '))

#Operações
resultado = (nota1 + nota2 + nota3 + nota4) / 4

#Saída:
print('-'*40)
print('A MEDIA DAS NOTAS SÃO:')
print('='*40)
print(f'Media: {resultado}')

#Texto de encerramento:
print('-'*40)
print('FIM DO PROGRAMA')
print('='*40)