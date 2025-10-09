# Problema "terreno":
# Fazer um programa para ler as medidas da largura e 
# comprimento de um terreno retangular com uma
# casa decimal, bem como o valor do metro quadrado do terreno 
# com duas casas decimais. 
# Em seguida, o programa deve mostrar o valor da área do terreno, 
# bem como o valor do preço do terreno, ambos com
# duas casas decimais, conforme exemplo. 

# Exemplo:
# Digite a largura do terreno: 10.0
# Digite o comprimento do terreno: 30.0
# Digite o valor do metro quadrado: 200.00
# Area do terreno = 300.00
# Preco do terreno = 60000.00 

largura_terreno = float(input("Digite a largura do terreno: "))
comprimento_terreno = float(input("Digite o comprimento do terreno: "))
valor_metro_quadrado = float(input("Digite o valor do metro quadrado: "))

area_terreno = largura_terreno * comprimento_terreno
preco_terreno = area_terreno * valor_metro_quadrado
print(f"Area do terreno = {area_terreno:.2f}")
print(f"Preco do terreno = {preco_terreno:.2f}")