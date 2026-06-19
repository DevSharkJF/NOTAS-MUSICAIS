import random
import os
import time

def nota_do():
    while True:
        resposta_do = input('Qual a nota corresponde a C?\n')
        os.system('cls')

        if resposta_do.lower() == 'dó' or resposta_do.lower() == 'do':
            print('PROCESSANDO...')
            time.sleep(1.0)
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            time.sleep(1.3)
            os.system('cls')
            break
        elif resposta_do.lower() != 'dó' or resposta_do.lower() != 'do':
            print('PROCESSANDO...')
            time.sleep(1.0)
            os.system('cls')
            print('❌ Você Errou, Tente Novamente! ❌\n')

def nota_re():
    while True:
        resposta_re = input('Qual a nota correspondente a D?\n')
        os.system('cls')

        if resposta_re.lower() == 'ré' or resposta_re.lower() == 're':
            print('PROCESSANDO...')
            time.sleep(1.0)
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            time.sleep(1.3)
            os.system('cls')
            break
        elif resposta_re.lower() != 'ré' or resposta_re.lower() != 're':
            print('PROCESSANDO...')
            time.sleep(1.0)
            os.system('cls')
            print('❌ Você Errou, Tente Novamente! ❌\n')

def nota_mi():
    while True:
        resposta_mi = input('Qual a nota correspondente a E?\n')
        os.system('cls')

        if resposta_mi.lower() == 'mi':
            print('PROCESSANDO...')
            time.sleep(1.0)
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            time.sleep(1.3)
            os.system('cls')
            break
        elif resposta_mi.lower() != 'mi':
            print('PROCESSANDO...')
            time.sleep(1.0)
            os.system('cls')
            print('❌ Você Errou, Tente Novamente! ❌\n')

def nota_fa():
    while True:
        resposta_fa = input('Qual a nota correspondente a F?\n')
        os.system('cls')

        if resposta_fa.lower() == 'fa':
            print('PROCESSANDO...')
            time.sleep(1.0)
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            time.sleep(1.5)
            os.system('cls')
            break
        elif resposta_fa.lower() != 'fa':
            print('PROCESSANDO...')
            time.sleep(1.0)
            os.system('cls')
            print('❌ Você Errou, Tente Novamente! ❌\n')

def nota_sol():
    while True:
        resposta_sol = input('Qual a nota correspondente a G?\n')
        os.system('cls')

        if resposta_sol.lower() == 'sol':
            print('PROCESSANDO...')
            time.sleep(1.0)
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            time.sleep(1.3)
            os.system('cls')
            break
        elif resposta_sol.lower() != 'sol':
            print('PROCESSANDO...')
            time.sleep(1.0)
            os.system('cls')
            print('❌ Você Errou, Tente Novamente! ❌\n')

def nota_la():
    while True:
        resposta_la = input('Qual a nota correspondente a A?\n')
        os.system('cls')

        if resposta_la.lower() == 'la':
            print('PROCESSANDO')
            time.sleep(1.0)
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            time.sleep(1.3)
            os.system('cls')
            break
        elif resposta_la.lower() != 'la':
            print('PROCESSANDO...')
            time.sleep(1.0)
            os.system('cls')
            print('❌ Você Errou, Tente Novamente! ❌\n')

def nota_si():
    while True:
        resposta_si = input('Qual a nota correspondente a B?\n')
        os.system('cls')

        if resposta_si.lower() == 'si':
            print('PROCESSANDO')
            time.sleep(1.0)
            print('✅PARABÉNS, VOCÊ ACERTOU!✅')
            time.sleep(1.3)
            os.system('cls')
            break
        elif resposta_si.lower() != 'si':
            print('PROCESSANDO...')
            time.sleep(1.0)
            os.system('cls')
            print('❌ Você Errou, Tente Novamente! ❌\n')

random.seed()
def infinito():
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

def aprendizagem():
    print('AINDA EM CONSTRUÇÃO\n')

def menu():
    while True:
        print(
        'BEM VINDO AO GAME HON MUSICAS\n'
        '\nSELECIONE UMA DAS OPÇÕES ABAIXO'
        '\n[1] MODO APRENDIZAGEM 🎼'
        '\n[2] MODO INFINITO ♾️'
        '\n[3] SAIR ⚠️'
        )

        op = input('OPÇÃO: ')
        if op == '1':
            os.system('cls')
            aprendizagem()

        if op == '2':
            os.system('cls')
            infinito()

        if op == '3':
            os.system('cls')
            print('🚶🏻SAINDO DO JOGO...')
            time.sleep(2.5)
            os.system('cls')
            print('❗VOCÊ SAIU❗')
            break

time.sleep(1.5)
os.system('cls')
menu()

"""
IDEIAS
1) Modo de Aprendizagem - Ensina o usuário sobre a relação das notas (Tabela antes da pergunta / somente uma tabela de vizualização)
2) Modo Hardcore - Roda um loop em que conforme o usuário acerta as notas, ele acumula nota, caso erre,
o loop se quebra mostrando o record.
"""