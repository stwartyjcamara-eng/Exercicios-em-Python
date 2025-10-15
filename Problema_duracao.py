'''
Problema "duracao"
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos.
Exemplo 1:
Digite a duracao em segundos: 300
0:5:0
Exemplo 2:
Digite a duracao em segundos: 12506
3:28:26
Exemplo 3:
Digite a duracao em segundos: 140811
39:6:51 
'''
duracao_segundos = int(input('Digite a duração em segundos: '))
horas = duracao_segundos // 3600
minutos = (duracao_segundos % 3600) // 60
segundos = duracao_segundos % 60
print(f'{horas}:{minutos}:{segundos}')