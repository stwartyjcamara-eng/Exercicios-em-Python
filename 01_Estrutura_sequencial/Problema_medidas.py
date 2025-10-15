'''
Problema "medidas"
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C
Exemplo 1:
Digite a medida A: 4.0
Digite a medida B: 3.5
Digite a medida C: 5.2
AREA DO QUADRADO = 16.0000
AREA DO TRIANGULO = 7.0000
AREA DO TRAPEZIO = 19.5000
Exemplo 2:
Digite a medida A: 7.13
Digite a medida B: 8.05
Digite a medida C: 11.912
AREA DO QUADRADO = 50.8369
AREA DO TRIANGULO = 28.6983
AREA DO TRAPEZIO = 90.4121
'''
medida_a = float(input('Digite a medida A: '))
medida_b = float(input('Digite a medida B: '))
medida_c = float(input('Digite a medida C: '))
area_quadrado = medida_a * medida_a
area_triangulo = (medida_a * medida_b) / 2
area_trapezio = ((medida_a + medida_b) * medida_c) / 2
print(f'AREA DO QUADRADO = {area_quadrado:.4f}')
print(f'AREA DO TRIANGULO = {area_triangulo:.4f}')
print(f'AREA DO TRAPEZIO = {area_trapezio:.4f}')