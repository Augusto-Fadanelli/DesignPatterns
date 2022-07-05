
from receiver import Receiver
from controle import Controle

controle = Controle()
controle.enviarComandoSimples("Ola")

receiver = Receiver()
controle.enviarComandoComplexo("Calibrar o pneu")

controle.fazer()
