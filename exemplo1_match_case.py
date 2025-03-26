linguagem = input('Linguagem: ')

# || ou Python = or 

match linguagem:
    case 'JavaScrip':
        print('Desemvolvedor web')
    case 'Python' | 'python':
        print('Cientista de dados')
    case 'PHP':
        print('Desenvolvedor backend')
    case 'Java' | 'java' | 'JAVA' :
        print('Desenvolvedor backend ou mobile')
    case 'Solidity':
        print('Desemvolvedor Blockchair')
    case _:
        print('Linguagem não encontrada!')
