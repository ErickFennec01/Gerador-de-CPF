'''
Gerador de cpf
'''
import random
import os
def tela_inicio():
    print('\t𝔾𝕖𝕣𝕒𝕕𝕠𝕣 𝕕𝕖 𝕔𝕡𝕗') 
    print('''
    1 - Gerar um cpf aleatorio
    2 - validar um cpf''')
    escolha = int(input('\n\tDigite Sua Escolha: '))
    os.system('cls')
    return(escolha)




def gerador_digitos():
    cpf = ''

    for contador in range(0,9):
        armazenador = random.randint(0,9)
        cpf += str(armazenador)
    return cpf



def validador_cpf(escolha):
#colocaremos um cpf para validar nosso algoritmo
    cpf = ''
    escolha = escolha

    if escolha ==1:
        armazem = gerador_digitos()
        cpf += armazem

    elif escolha ==2:
        cpf_informado = input('Digite seu cpf: ').replace('.','').replace('-','')
            

        
        cpf = cpf_informado[:9]
    
    else:
        print('Digite Apenas Valores Validos!',os.system('cls'),main())
        os.system('cls')
    
    
    cpf = cpf
    nove_digitos = cpf[:9]
    contador_regressivo_1 = 10
    somador_1 = 0

# primeiro numero
    for digitos in nove_digitos:
        somador_1 += int(digitos) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito = (somador_1 * 10)  % 11
    digito = digito if digito <= 9 else 0
    cpf += str(digito)

#segundo numero

    dez_digitos = cpf[:10]
    contador_regressivo_2 = 11
    somador_2 = 0

    for digitos in dez_digitos:
        somador_2 += int(digitos) * contador_regressivo_2
        contador_regressivo_2 -=1

    digito_2 = (somador_2 *10) %11
    digito_2 = digito_2 if digito_2 <=9 else 0
    cpf += str(digito_2)

    cpf_formatado = ''
    contador = 1
    
    for formatado in cpf:
        if contador ==3 or contador ==6:
            cpf_formatado += f'{formatado}.'
            contador+=1
        elif contador ==9:
            cpf_formatado += f'{formatado}-'
            contador+=1
        else:
            cpf_formatado += formatado
            contador+=1
    
    if escolha == 1 :
        print(f'{cpf_formatado} ✅' )
    
    
    if escolha ==2:
        if cpf_formatado.replace('.','').replace('-','') == cpf_informado:
            print(f'o cpf {cpf_formatado} ✅')
        else:
            print(f'cpf:{cpf_informado} ❌')


def main():
    resposta = tela_inicio()
    validador_cpf(resposta)



if __name__ == '__main__':
    main()