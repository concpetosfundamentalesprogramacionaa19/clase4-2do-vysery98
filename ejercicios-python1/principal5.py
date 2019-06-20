"""
    @vysery98
    Manejo de estructuras
"""

diccionario = {"nombre": "Fernando", "apellidos": "Quizhpe"}
diccionario2 = {"nombre": "Brandon", "apellidos": "Vega"}

lista = [diccionario, diccionario2]

print("Imprimir diccionario")
for l in lista:
	midiccionario = l
	print("%s: %s %s: %s" %
		("Mi nombre es", midiccionario["nombre"], \
			"y mi apellido es", \
			midiccionario["apellidos"])
		)