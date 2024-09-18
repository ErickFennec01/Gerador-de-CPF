import random
import os



while True:
    variavel = ''
    contador = 0
    grupo = []
    for cpf in range(1,10):
        contador +=1
        if contador == 3 or contador ==6:
            armazenador= random.randint(0,9)
            numero_str = str(armazenador)
            variavel += f'{numero_str}.'
            grupo.append(armazenador)
        elif contador ==9:
            armazenador= random.randint(0,9)
            numero_str = str(armazenador)
            variavel += f'{numero_str}-'
            grupo.append(armazenador)
        else:
            armazenador= random.randint(0,9)
            numero_str = str(armazenador)
            variavel += numero_str
            grupo.append(armazenador)
    contador = 10
    somatorio = 0
    
    for numeros in grupo:
        vezes = (numeros * contador)
        somatorio += vezes
        contador -=1
        
        
           
    resultado = somatorio % 11
    
    if resultado <2:
        grupo.append(0)
        variavel += '0'

    else:
        resto_resultante = 11-resultado
        grupo.append(resto_resultante)
        resto_formatado = str(resto_resultante)
        variavel += resto_formatado
    
    
    
    contadores = 12
    somatorio = 0
    for numeros in grupo:    
        vezes = (numeros * contadores)
        somatorio += vezes
        contador -=1
            
        

    resultado_2 = somatorio % 11
    if resultado_2 <2:
        grupo.append(0)
        variavel += '0'

    else:
        resto_resultantes = 11-resultado_2
        grupo.append(resto_resultantes)
        resto_formatado = str(resto_resultantes)
        variavel += resto_formatado
    
    print(f'Aqui Esta seu cpf gerado:{variavel}')
    opcao = input('(S)air / (C)ontinuar: ').lower()
    if opcao =='s' or opcao == 'sair':
        os.system('cls')
        break
        

    else:
        os.system('cls')
        continue
        

print('Programa finalizado!')
        
   
    
