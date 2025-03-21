print('*-* Calculo da média *-*')
print('------------------------')

n1 = float(input('N1: '))
n2 = float(input('N2: '))
n3 = float(input('N3: '))
faltas = int(input('Faltas: '))

#Processamento
media = (n1+n2+n3)/3

#Saída de dados
print('Média: ', media)

#Teste condocionais
if (media >= 6 and faltas <= 18):
    print('Aprovado!')
else:
    print('Reprovado!')
    


