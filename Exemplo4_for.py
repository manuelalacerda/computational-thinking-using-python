'''
crie um programa em python que recebe como entrada quatro salário,
o prorama deve calcular  a média salarial e exibir os salários que estão abaixo da média
'''

salarios = []
soma = 0 

for i in range(4):
    salario = float(input('Salário R$: '))
    soma += salario
    salarios.append(salario) #adiciona salário em salários

media = soma/4

for salario in salarios:
    if salario < media:
        print(f'Salários: {salario:.2f}')