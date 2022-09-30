"""Exercício 1"""
print()
n1 = input('Informe um número: ')

try:
    n1 = int(n1)
    c1 = n1 / 2
    if c1 == 0:
        print(f'{n1} é um número par')
    else:
        print(f'{n1} é um número impar ')
except:
    print('Isso não é um número')


"""Excercício 2"""
print()
hora = int(input('Digite uma hora: '))
min = int(input('Digite os minutos: '))

if hora < 24 and min < 60:
    if 0 <= hora <= 11:
        print(f'Bom dia, são {hora}:{min}')
    elif 12 <= hora <= 17:
        print(f'Boa tarde, são {hora}:{min}')
    else:
        print(f'Boa noite, são {hora}:{min}')
else:
    print('ERROR! O valor informado é inválido!!')


"""Exercício 3"""

n1 = input('Digite seu nome: ')
l1 = len(n1)

if l1 <= 4:
    print(f'{n1}, Seu nome é curto')
elif 5 <= l1 <=6:
    print(f'{n1}, seu nome é normal')
else:
    print(f'{n1}, Seu nome é grande demais')

    

