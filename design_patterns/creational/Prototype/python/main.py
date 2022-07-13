
import datetime
from concreteSummonerElf import SummonerElf
from concretePaladin import Paladin
from concreteMage import Mage

i = 1

#CRIANDO CADA PALADINO(OBJETO) UM A UM SEM USAR O PROTOTYPE
#print("Começando a criar um paladino em: ", datetime.datetime.now().time())
#paladino = Paladin(70, 70, 80)
#print("Terminou de criar os paladino", datetime.datetime.now().time())
#print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(paladino).items()))
#print(paladino.description())


#CRIANDO CADA MAGO(OBJETO) UM A UM SEM USAR O PROTOTYPE
print(f"Começando a criar os mago em: {datetime.datetime.now().time()}\n",)
for i in range(3):
    mago = Mage(23, 90, 70)
    print(f"Terminou de criar o {i+1} mago em: {datetime.datetime.now().time()}")
print(f"Criação de todos os {i+1} magos terminou em: {datetime.datetime.now().time()}\n")
print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(mago).items()))
print(f"{mago.description()}\n\n")


#CRIANDO UMA POPULAÇÃO DE ELFOS(VARIOS OBJETOS) CLONANDO ELES, E COM ISSO SENDO MAIS RAPIDO A CRIAÇÃO
print(f"Começando a clonar varios elfos em: {datetime.datetime.now().time()}\n")
elfo = SummonerElf(948, 67, 65)
for i in range(20):
    elfo_clones = elfo.clone()
    print(f"Terminado de criar {i+1} clone de elfo em: {datetime.datetime.now().time()}")
print(f"Terminou de criar a população elfos em: {datetime.datetime.now().time()}\n")
print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(elfo).items()))
print(f"{elfo.description()}\n\n")
