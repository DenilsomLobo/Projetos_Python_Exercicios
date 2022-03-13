#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data início: 28/10/2021
#Término: 28/10/2021
#Atividade 003: Exercicio J = Cálculadora de metro quadrado.

#Progama que recebe um valor de uma largura, altura de uma parede e converte em metro quadrado.
#Entrada:
#Texto:
print('-'*40)
print('CÁLCULADORA DE M²')
print('='*40)

#Entrada de dados:
largura = float(input('Por favor coloque o valor da largura de sua parede: '))
altura = float(input('Por favor coloque o valor da altura de sua parede: '))

#Operações:
m2 = largura * altura 

#Saída:
print('-'*40)
print(f'O metro quadrado da sua área sera: {m2} m²')
#Texto de encerramento:
print('-'*40)
print('FIM DO PROGRAMA')
print('='*40)