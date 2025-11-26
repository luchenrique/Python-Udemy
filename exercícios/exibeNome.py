"""
    Peça ao usuário digitar seu nome
    Peça ao usuário digitar sua idade
    Se nome e idade forem digitados:
        Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contem (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
        Exiba:
            "Desculpe, você deixou campos em vazio."
"""

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

if nome and idade != 0:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else: 
        print(f'Seu nome não contém espaços')
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print("Desculpe, você você deixou campos vazios")
