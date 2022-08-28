nome = 'Lucas'
idade = 19
altura = 1.83
e_maior = idade > 18
peso = 70
imc = peso / (altura**2)

print(nome, 'tem', idade, 'anos de idade,', altura, 'de altura e', imc, 'de imc')
print(f'{nome} tem {idade} anos de idade, {altura} de altura e {imc:.2f} de imc')
print('{} tem {} anos de idade {} de altura e {:.2f} de imc'.format(nome, idade, altura, imc))