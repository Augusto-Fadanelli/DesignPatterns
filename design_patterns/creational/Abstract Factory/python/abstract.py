from abc import ABCMeta, abstractstaticmethod

from .cadeiraFactory.factory import CadeiraFactory
from .mesaFactory.factory import MesaFactory


class MobiliariaFactory(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_mobiliaria(mobiliariaTipo):
        """interface"""


class MobiliariaFactory(MobiliariaFactory):
    @staticmethod
    def get_mobiliaria(mobiliariaTipo):
        try:
            if mobiliariaTipo in [
                'Cadeira Grande',
                'Cadeira Media',
                'Cadeira Pequena',
            ]:
                return CadeiraFactory.get_cadeira(mobiliariaTipo)

            if mobiliariaTipo in ['Mesa Grande', 'Mesa Media', 'Mesa Pequena']:
                return MesaFactory.get_mesa(mobiliariaTipo)

            AssertionError('Movel não encontrado')
        except AssertionError as _e:
            print(_e)


if __name__ == '__main__':
    escolha = input('Qual o movel que voce vai escolhe? \n')
    movel = MobiliariaFactory.get_mobiliaria(escolha)
    print(f'{movel.get_dimensao()}')
