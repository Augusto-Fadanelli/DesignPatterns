from criador1 import CadeiraGrande
from criador2 import CadeiraMedia
from criador3 import CadeiraPequena
from abc import abstractmethod

class CadeiraFactory():

	@abstractmethod
	def get_cadeira(cadeiraTipo):
		try:
			if cadeiraTipo == "Grande":
				return CadeiraGrande()
			if cadeiraTipo == "Médio":
				return CadeiraMedia()
			if cadeiraTipo == "Pequena":
				return CadeiraPequena()
			raise AssertionError("Cadeira não encontrada")
		except AssertionError as _e:
			print(_e)
