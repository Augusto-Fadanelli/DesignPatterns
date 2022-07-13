
from factory import MesaFactory


escolha = input("Qual o tamanho da mesa que voce vai escolhe? \n")
mesa = MesaFactory.get_mesa(escolha)
print(f"{mesa.get_dimensao()}")