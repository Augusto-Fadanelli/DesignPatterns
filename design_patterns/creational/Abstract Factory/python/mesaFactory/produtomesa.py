from abc import ABCMeta, abstractstaticmethod

class MinhaMesa(metaclass=ABCMeta):
	
	@abstractstaticmethod
	def get_dimensao():
		"A interface das mesas"
