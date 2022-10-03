
x = int(input('Digite um número para saber a tabuada: '))
cont = 0

print('')
print('*' * 30)
while cont <= 10:
    print(f'{x} X {cont} = {x*cont}')
    cont += 1
else:
    print('*' * 30)
    print('')
    print('Tabuada Finalizada')
    print('')