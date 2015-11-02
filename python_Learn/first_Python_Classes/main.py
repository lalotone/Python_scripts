import first_Class

def helloWorld():
	x = "Hello World"
	return x 

hello = first_Class.Test()
'''Aqui invocamos la clase Test para poder acceder 
a las funciones a traves de la llamada mediante hello.nombreFuncion como se 
puede ver mas abajo'''

hi = hello.helloWorld()#tal que asi 

hiTwo = helloWorld()

returnNumX = hello.returnX()

print hi
print hiTwo
