from factory import CadeiraFactory

escolha = input('Qual o tamanho da cadeira que voce vai escolhe? \n')
cadeira = CadeiraFactory.get_cadeira(escolha)
print(f'{cadeira.get_dimensao()}')
