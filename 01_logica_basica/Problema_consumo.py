'''
Problema "consumo"
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
médio do carro, com três casas decimais.
Exemplo 1:
Distancia percorrida: 500
Combustível gasto: 38.5
Consumo medio = 12.987
Exemplo 2:
Distancia percorrida: 1108
Combustível gasto: 71.4
Consumo medio = 15.518 

'''
distancia_percorrida = float(input('Distancia percorrida: '))
combustivel_gasto = float(input('Combustível gasto: '))
consumo_medio = distancia_percorrida / combustivel_gasto
print(f'Consumo medio = {consumo_medio:.3f}')
#utilizei o float para aceitar valores decimais, e o :.3f para limitar a 3 casas decimais no print


