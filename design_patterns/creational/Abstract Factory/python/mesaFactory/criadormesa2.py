from produtomesa import MinhaMesa


class MesaMedia(MinhaMesa):
	
	def __init__(self):
		self.height = 140
		self.width = 80
		self.depth = 50
			
	def get_dimensao(self):
		return{"Altura": self.height, "Largura": self.width, "Profundidade": self.depth}