# MODO INFINITO
# os.system('cls')
# time.sleep(1)
import random
import os
import time

def nota_do():
    while True:
        resposta_do = input('Qual a nota corresponde a C?')
        os.system('cls')

        if resposta_do.lower() == 'dó' or resposta_do.lower() == 'do':
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            break
        elif resposta_do.lower() != 'dó' or resposta_do.lower() != 'do':
            print(
                ''
                '\n!Você Errou, Tente Novamente!'
            )

def nota_re():
    while True:
        resposta_re = input('Qual a nota correspondente a D?')
        os.system('cls')

        if resposta_re.lower() == 'ré' or resposta_re.lower() == 're':
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            break
        elif resposta_re.lower() != 'ré' or resposta_re.lower() != 're':
            print(
                ''
                '\n!Você Errou, Tente Novamente!'
            )

def nota_mi():
    while True:
        resposta_mi = input('Qual a nota correspondente a E?')
        os.system('cls')

        if resposta_mi.lower() == 'mi':
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            break
        elif resposta_mi.lower() != 'mi':
            print(
                ''
                '\n!VOCÊ ERROU, TENTE NOVAMENTE!'
            )

def nota_fa():
    while True:
        resposta_fa = input('Qual a nota correspondente a F?')
        os.system('cls')

        if resposta_fa.lower() == 'fa':
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            break
        elif resposta_fa.lower() != 'fa':
            print(
                ''
                '\n!Você Errou, Tente Novamente!'
            )

def nota_sol():
    while True:
        resposta_sol = input('Qual a nota correspondente a G?')
        os.system('cls')

        if resposta_sol.lower() == 'sol':
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            break
        elif resposta_sol.lower() != 'sol':
            print(
                ''
                '\n!Você Errou, Tente Novamente!'
            )

def nota_la():
    while True:
        resposta_la = input('Qual a nota correspondente a A?')
        os.system('cls')

        if resposta_la.lower() == 'la':
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            break
        elif resposta_la.lower() != 'la':
            print(
                ''
                '\n!Você Errou, Tente Novamente!'
            )

def nota_si():
    while True:
        resposta_si = input('Qual a nota correspondente a B?')
        os.system('cls')

        if resposta_si.lower() == 'si':
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            break
        elif resposta_si.lower() != 'si':
            print(
                ''
                '\n!Você Errou, Tente Novamente!'
            )

while True:
    contador = int(random.random() * 6)
    if contador == 0:
        nota_do()
    elif contador == 1:
        nota_re()
    elif contador == 2:
        nota_mi()
    elif contador == 3:
        nota_fa()
    elif contador == 4:
        nota_sol()
    elif contador == 5:
        nota_la()
    elif contador == 7:
        nota_si()

"""
Ideia de fazer um menu com 2 opções, uma de aprendizagem que ensina sobre as notas, e um modo infinito
em que o jogador irá conseguir uma pontuação
"""
# def menu():
#     while True:
#         print(
#             'BEM VINDO AO GAME HON MUSICAS'
#             '\nSELECIONE A OPÇÃO QUE DESEJA USAR'
#             '\n[1] MODO APRENDIZAGEM'
#             '\n[2] MODO INFINITO'
#             '\n[3] SAIR'
#         )

#         op = input('OPÇÃO: ')
#         if op == '1':
#             aprendizagem()
#         if op == '2':
#             infinito()
#         if op == '3':
#             print ('SAINDO DO JOGO')
#             print ('VOCÊ SAIU')
#             break
# menu()