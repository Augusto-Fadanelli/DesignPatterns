from produtomesa import MinhaMesa


class MesaGrande(MinhaMesa):
	
	def __init__(self):
		self.height = 150
		self.width = 110
		self.depth = 70
			
	def get_dimensao(self):
		return{"Altura": self.height, "Largura": self.width, "Profundidade": self.depth}
