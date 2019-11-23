class Alumno:
	def __init__(object, name, age):
		object.name = name
		object.age = age

	def imprimirDatos(abc):
		print("Hola mi nombre es", abc.name)
		print("Mi edad es", abc.age)


p1 = Alumno("Jhon", 18)		
p1.imprimirDatos()