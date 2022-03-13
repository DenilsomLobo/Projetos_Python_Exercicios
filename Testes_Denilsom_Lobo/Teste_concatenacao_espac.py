#Curso Técnico de informática
#Autor:Sebastião Marcos
#Data início: 09/11/2021
#Término: 09/11/2021
#Concatenação

import os
os.system('cls')

print('-'*50)
print('CONCATENAÇÃO (JUNTAR STRINGS)')

#declaração
primeiroNome = (input('Nome: '))
segundoNome = (input('Sobrenome: '))
nascimento = (input('Data: '))


#operação de concatenação
nomeCompleto = primeiroNome + ' ' + segundoNome + ' ' +  nascimento

#Saída
print(f'Primeiro nome: {primeiroNome}')
print (f'Primeiro nome: {segundoNome}')
print (f'Primeiro nome: {nascimento}')
print(f'O nome  completo é: {nomeCompleto}')
print('-'*50)
print()
