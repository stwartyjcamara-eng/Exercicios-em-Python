"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
#  0123456
#  Stwarty
# -7654321 
input_nome = str(input('Digite seu nome: '))
input_idade = str(input('Digite sua idade: '))
contador_espaco = input_nome.count(' ') 
if input_nome and input_idade:
    print(f'Seu nome é {input_nome}')
    print(f'Seu nome invertido é {input_nome[::-1]}')
    if ' ' in input_nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    if contador_espaco >= 1:
        contador_espaco2 = len(input_nome) - contador_espaco
        print(f'Seu nome tem {contador_espaco2} letras')
    else:
        print(f'Seu nome tem {len(input_nome)} letras')
    print(f'A primeira letra do seu nome é {input_nome[0:1]}')
    print(f'A última letra do seu nome é {input_nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
    