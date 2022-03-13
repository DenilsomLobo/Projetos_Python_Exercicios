#Curso Técnico de informática
#Autor: Denilsom Lobo
#Data início: 26/10/2021
#Término: 26/10/2021
#Atividade 001: Cadastro

#cabeçalho do cadastro:
print ('-'*68)
print ('SEJA BEM VINDO, POR FAVOR CONFIRME OS DADOS PARA FAZER O CADASTRO')
print ('='*68)

#Variavéis de entradada do cadastro:
#Entrada
nome = str(input('Nome do usuário: '))
dataNacimento = str(input('Sua data de nascimento: '))
rg = str(input('Sua identidade: '))
cpf = str(input('Seu CPF: '))
print ('-'*68)
print ('AGORA POR FAVOR O SEU ENDREÇO: ')
print ('='*68)
rua = str(input('Sua rua:'))
numero = int(input('Numero da sua residencia: '))
complemento = str(input('Complemento: '))
cep = str(input('CEP: '))
cidade = str(input('Cidade: '))
estado = str(input('Estado: '))
pais = str (input ('País: '))

#Resposta após prenchimento de dados:
print ('-'*68)
print ('OBRIGADO PELAS INFORMAÇÕES')
print ('='*68)

#Variavéis de saidas:
#Saida
print ('Seus dados são:')
print (f'Nome:..............: {nome} ')
print (f'Data de nacimento..: {dataNacimento} ')
print (f'Sua identidade.....: {rg} ')
print (f'Seu CPF............: {cpf} ')
print ('Seu endereço é: ')
print (f'Rua ...............: {rua} ')
print (f'Numero ............: {numero} ')
print (f'complemento........: {complemento} ')
print (f'CEP................: {cep} ')
print (f'Cidade.............: {cidade} ')
print (f'Estado.............: {estado} ')
print (f'País...............: {pais}')

#Resposta após o preenchimento:
print ('-'*68)
print ('CADASTRO CONCLUIDO')
print ('='*68)