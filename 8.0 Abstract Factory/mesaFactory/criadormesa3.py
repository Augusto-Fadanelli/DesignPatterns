from produtomesa import MinhaMesa


class MesaPequena(MinhaMesa):
	
	def __init__(self):
		self.height = 110
		self.width = 50
		self.depth = 30
			
	def get_dimensao(self):
		return{"Altura": self.height, "Largura": self.width, "Profundidade": self.depth}