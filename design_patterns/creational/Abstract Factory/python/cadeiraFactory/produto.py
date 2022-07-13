from abc import ABCMeta, abstractstaticmethod

class MinhaCadeira(metaclass=ABCMeta):
	
	@abstractstaticmethod
	def get_dimensao():
		"A interface das cadeiras"