from abc import abstractmethod

from criadormesa1 import MesaGrande
from criadormesa2 import MesaMedia
from criadormesa3 import MesaPequena


class MesaFactory:
    @abstractmethod
    def get_mesa(cadeiraTipo):
        try:
            if cadeiraTipo == 'Mesa Grande':
                return MesaGrande()
            if cadeiraTipo == 'Mesa Medio':
                return MesaMedia()
            if cadeiraTipo == 'Mesa Pequena':
                return MesaPequena()
            raise AssertionError('Cadeira não encontrada')
        except AssertionError as _e:
            print(_e)
