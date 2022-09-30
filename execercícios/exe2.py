print('\n'*2)
x1 = int(input('Digite 1 para iniciar a calculadora! '))

while x1 == 1:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    op = input('Digite um operador (+, -, * ou /): ')

    if op == '+':
        print(f'O valor da soma é de {n1 + n2}')

    elif op == '-':
        print(f'O valor da subtração é de {n1 - n2}')

    elif op == '*':
        print(f'O valor da multiplicação é de {n1 * n2}')

    elif op == '/':
        print(f'O valor da divisão é de {n1 / n2:.2f}')

    else:
        print('Operador inválido')

    x1 = int(input('\nDigite 1 para continuar ou 0 para parar! '))

    if x1 != 1:
        print('\n\nO programa será encerrado! \n\nPrograma Encerrado!!')

    else:
        print('Valor inválido')