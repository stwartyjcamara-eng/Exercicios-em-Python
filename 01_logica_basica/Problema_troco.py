'''
Problema "troco"
Fazer um programa para calcular o troco no processo de pagamento de um 
produto de uma mercearia.
O programa deve ler o preço unitário do produto, 
a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente 
(suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.

Exemplo:
Preço unitário do produto: 8.00
Quantidade comprada: 2
Dinheiro recebido: 20.00
TROCO = 4.00 
'''
preco_produto = float(input('Preço unitário do produto: '))
quantidade_produto = float(input('Quantidade comprada: '))
valor_total = preco_produto * quantidade_produto
dinheiro_recebido = float(input('Dinheiro recebido: '))

if valor_total < dinheiro_recebido: 
    troco = dinheiro_recebido - valor_total
    print(f'TROCO = {troco:.2f}')
else:
    print('Dinheiro insuficiente!') #add opção de dinheiro insuficiente utilizando o if|else