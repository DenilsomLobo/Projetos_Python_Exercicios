# Curso Técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do início: 02/12/2021
# Data do término: 02/12/2021
# Atividade avaliativa.

# Programa que joga com um Npc. Pedra, Papel ou Tesoura.

# Importando as bibliotecas:
import os
from random import randint

# Limpando o terminal:
os.system('cls')

# Declarações:





# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)
print("""                                                   
,------.           ,--.                              
|  .--. ' ,---.  ,-|  |,--.--. ,--,--.               
|  '--' || .-. :' .-. ||  .--'' ,-.  |               
|  | --' \   --.\ `-' ||  |   \ '-'  |               
`--'      `----' `---' `--'    `--`--'               
                             ,--.                    
 ,---.  ,--,--. ,---.  ,---. |  |                    
| .-. |' ,-.  || .-. || .-. :|  |                    
| '-' '\ '-'  || '-' '\   --.|  |                    
|  |-'  `--`--'|  |-'  `----'`--'                    
`--'           `--'                                  
  ,--.                                               
,-'  '-. ,---.  ,---.  ,---. ,--.,--.,--.--. ,--,--. 
'-.  .-'| .-. :(  .-' | .-. ||  ||  ||  .--'' ,-.  | 
  |  |  \   --..-'  `)' '-' ''  ''  '|  |   \ '-'  | 
  `--'   `----'`----'  `---'  `----' `--'    `--`--'
""")
print('='*80)
print()
print('A maquina está olhando para sua alma antes de fazer sua escolha cuidadosamente ...')
print('Ao enfrentá-la ... ')
print('Você ira escolher. 1="Pedra", 2 ="Papel" ou 3 = "Tesoura".')
print()

while(True):
    escolha = input('Você escolhe ? : ')
    if(not(escolha.isnumeric()) or (int(escolha) < 1) or (int(escolha) > 3)):
        print('Você deve digitar 1, 2 ou 3. Caso contrario não sera possivel escolher.')
    else:
        escolha = int(escolha)
        if (escolha + 3 == 4):
            print()
            print('Sua escolha foi: "Pedra"')
        elif (escolha + 3 == 5):
            print()
            print('Sua escolha foi: "Papel"')
        elif (escolha + 3 == 6):
            print()
            print('Sua escolha foi "Tesoura"')
        flag = True

        while (flag == True):
            print()
            continuar = input('Deseja trocar a escolha ? (s/n): ').lower()
            if (continuar != 's' and continuar != 'n'):
                print('Digite "s" ou "n"...')
                
            else:
                if(continuar =='s'):
                    os.system('cls')                    
                    break
                elif(continuar =='n'):
                    print('='*80)
                    print('Agora e a vez da maquina escolher: ')
                    escolhaDaMaquina = randint (1, 3)
                    
                    





