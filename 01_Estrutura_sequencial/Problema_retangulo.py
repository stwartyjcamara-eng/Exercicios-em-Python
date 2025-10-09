# Problema "retangulo"
# Fazer um programa para ler as medidas da base e altura
# de um retângulo. Em seguida, mostrar o valor
# da área, perímetro e diagonal deste retângulo, 
# com quatro casas decimais, conforme exemplos:
'''
Exemplo:
Base do retangulo: 4.0
Altura do retangulo: 5.0
AREA = 20.0000
PERIMETRO = 18.0000
DIAGONAL = 6.4031 
'''
base_retangulo = float(input('Base do retangulo: '))
altura_retangulo = float(input('Altura do retangulo: '))
area_retangulo = base_retangulo * altura_retangulo
perimetro_retangulo = 2 * (base_retangulo + altura_retangulo)
diagonal_retangulo = (((base_retangulo ** 2) + (altura_retangulo ** 2)) ** 0.5)

print(f'AREA = {area_retangulo:.4f}')
print(f'PERIMETRO = {perimetro_retangulo:.4f}')
print(f'DIAGONAL = {diagonal_retangulo:.4f}')
