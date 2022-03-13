# Curso Técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do início: 02/12/2021
# Data do término: 02/12/2021
# Atividade avaliativa.

# Programa que joga com um Npc. Pedra, Papel ou Tesoura.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declarações:
suaEscolha = []




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
    if(not(escolha.isnumeric()) or (int(escolha) != 1) or (int(escolha) != 2) or (int(escolha) != 3)):
        print('Você deve digitar 1, 2 ou 3. Caso contrario não sera possivel escolher.')
    else:
        escolha = int(escolha)
        flag = True

        while (flag == True):
            print()
            continuar = input('Deseja continuar (s/n): ').lower()
            if (continuar != 's' and continuar != 'n'):
                print('Digite "s" ou "n"...')
                
            else:
                if(continuar =='s'):
                    os.system('cls')                    
                    break
                elif(continuar =='n'):
                    print('-'*70)
                    print(f'Esta e a sua escolha : {escolha}')
                    print('-'*70)
               



