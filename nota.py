import random

def nota_do():
    resposta_do = input('Qual a nota corresponde a C? ')
    if resposta_do.lower() == 'dó':
        print('CORRETO')
    else:
        while resposta_do != 'dó':
            print('Errado')
            resposta_do = input('Tente Novamente: ')

def nota_re():
    resposta_re = input('Qual a nota correspondente a D? ')
    if resposta_re.lower() == 'ré':
        print('CORRETO')
    else:
        while resposta_re != 'ré':
            print('ERRADO')
            resposta_re = input('TENTE NOVAMENTE: ')

def nota_mi():
    resposta_re = input('Qual a nota correspondente a E? ')
    if resposta_re.lower() == 'mi':
        print('CORRETO')
    else:
        while resposta_re != 'mi':
            print('ERRADO')
            resposta_re = input('TENTE NOVAMENTE: ')

def nota_fa():
    resposta_re = input('Qual a nota correspondente a F? ')
    if resposta_re.lower() == 'fa':
        print('CORRETO')
    else:
        while resposta_re != 'fa':
            print('ERRADO')
            resposta_re = input('TENTE NOVAMENTE: ')

def nota_sol():
    resposta_re = input('Qual a nota correspondente a G? ')
    if resposta_re.lower() == 'sol':
        print('CORRETO')
    else:
        while resposta_re != 'sol':
            print('ERRADO')
            resposta_re = input('TENTE NOVAMENTE: ')

def nota_la():
    resposta_re = input('Qual a nota correspondente a A? ')
    if resposta_re.lower() == 'la':
        print('CORRETO')
    else:
        while resposta_re != 'la':
            print('ERRADO')
            resposta_re = input('TENTE NOVAMENTE: ')

def nota_si():
    resposta_re = input('Qual a nota correspondente a B? ')
    if resposta_re.lower() == 'si':
        print('CORRETO')
    else:
        while resposta_re != 'si':
            print('ERRADO')
            resposta_re = input('TENTE NOVAMENTE: ')

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