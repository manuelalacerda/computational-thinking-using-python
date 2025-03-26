# Escreva um programa em Python que leia o nome de um aluno e 3 notas. O
# programa deve calcular a média e verificar se o aluno está aprovado ou
# reprovado. Para estar aprovado, o aluno deve ter média maior ou igual a 6.
# Além, o programa deve determinar o conceito obtido pelo aluno, de acordo
# com a tabela abaixo:

# Conceito 'A' - media >= 9 E media <= 10
# Conceito 'B' - media >= 8 E media <= 9
# Conceito 'C' - media >= 7 E media <= 8
# Conceito 'D' - media >= 6 E media <= 7
# Conceito 'E' - media < 6

# O programa deve imprimir o nome do aluno, a méida, o status e o
# conceito obtido - match_case (de acordo com o conceito)

nome = input('Nome: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')

match media:
    case 9|10:
        conceito = 'A'
    case 8|9:
        conceito = 'B'
    case 7|8:
        conceito = 'C'
    case 6|7:
        conceito = 'D'
    case 0|1|2|3|4|5:
        conceito = 'E'

        
        
        

