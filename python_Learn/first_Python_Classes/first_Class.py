class Test():
	z = 2
	y = "hi"
	def helloWorld(self):
		x= "Hello world"
		return x
	def returnX(self):#Este self se utiliza para referenciar a este metodo de LA CLASE en la que esta
		#El "self" es como el this en java, de esta manera referenciariamos a la variable z de arriba con un this.z, pues aqui es lo mismo pero con self.z
		z = int(raw_input("Introduce un numero: ")) #Esta z es la variable DENTRO de este metodo, no la z = 2 de arriba 
		print self.z #El self se utiliza para hacer referencia a la variable de arriba,la de la clase, la z = 2, esta imprimira 2, que es el valor de la de arriba
		print z #Esta imprimira el valor que le metamos cuando llamemos al metodo
		print self.y
		self.y = str(raw_input("Introduce un mensaje: "))
		print self.y 
