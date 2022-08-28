"""
* Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
* Criar variável para o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-String 
"""

nome = 'Maria'
idade = 18
altura = 1.68
peso = 58.50
ano = 2022
nascimento = ano - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade, tem {altura} de altura e pesa {peso}kg')
print(f'{nome} nasceu no ano de {nascimento}')
print(f'O IMC de {nome} é de {imc:.2f}')