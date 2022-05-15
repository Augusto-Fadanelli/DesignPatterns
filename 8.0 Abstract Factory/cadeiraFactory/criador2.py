
from produto import MinhaCadeira

class CadeiraMedia(MinhaCadeira):
	
	def __init__(self):
		self.height = 50
		self.width = 40
		self.depth = 40
			
	def get_dimensao(self):
		return{"Altura": self.height, "Largura": self.width, "Profundidade": self.depth}