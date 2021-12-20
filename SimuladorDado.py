import DadoModule as dm
import time

print('\n\nSimulador de Dado')
time.sleep(1)
print('\nEscolha a quantidade de lados')
print('\n6 lados é um dado comum...')
print('\nMas você pode escolher quandos quiser, porém o número precisa ser par...')
time.sleep(3)

jogar = 1


while jogar != 0:

    try:
        lados = int(input('Número de lados: '))
    except ValueError:
        print('O número precisa ser um Inteiro\nSerá atribuído o 6 lados')
        lados = 6
        

    while lados % 2 != 0: 
        print('\nNúmero inválido')
        print('\nA quantidade de lados precisa ser par...')
        lados = int(input('Número de lados: '))

    if lados % 2 == 0 and lados > 0 :
        dado = dm.JogarDado(lados)
        print('\nO dado foi jogado')
        time.sleep(1)
        print('\nO resultado foi: {}'.format(dado))
    else:
        while lados % 2 != 0: 
            print('\nNúmero inválido')
            print('\nA quantidade de lados precisa ser par...')
            lados = int(input('Número de lados: '))
        
        while lados <= 1:
            print('\nNúmero inválido')
            print('\nA quantidade de lados precisa ser maior do que zero...')
            lados = int(input('Número de lados: '))

    try:
        jogar = int(input('Deseja jogar novamente? \n1 - sim \n0 - não\n'))
    except ValueError:
        print('A reposta precisa ser 1 ou 0')
        try:
            jogar = int(input('Sua resposta: '))
        except ValueError:
            print('Resposta inválida, encerrando o programa... ')
            time.sleep(2)
            exit()



    if jogar == 0:
        exit()
    elif jogar != 1:
        exit()

    

    


    
    
    

