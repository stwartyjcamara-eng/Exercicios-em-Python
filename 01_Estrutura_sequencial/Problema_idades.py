'''
Problema "idades"
Fazer um programa para ler o nome e idade de duas pessoas. 
Ao final mostrar uma mensagem com os
nomes e a idade média entre essas pessoas, com uma casa decimal, 
conforme exemplo.

Exemplo:
Dados da primeira pessoa:
Nome: Maria Silva
Idade: 19
Dados da segunda pessoa:
Nome: Joao Melo
Idade: 20
A idade média de Maria Silva e Joao Melo é de 19.5 anos
'''
print('Dados da primeira pessoa:')
nome_primeira_pessoa = input('Nome: ')
idade_primeira_pessoa = float(input('Idade: '))
print('Dados da segunda pessoa:')
nome_segunda_pessoa = input('Nome: ')
idade_segunda_pessoa = float(input('Idade: '))

idade_media = (idade_primeira_pessoa + idade_segunda_pessoa) / 2
print(f'A idade média de {nome_primeira_pessoa} e {nome_segunda_pessoa} é de {idade_media:.1f} anos')