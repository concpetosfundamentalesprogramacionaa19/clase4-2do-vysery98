"""
    @vysery98
    Ejemplo de manejo de paquetes
"""
# Salida:
# Valor 2 elevado a la potencia 2 es igual a 4
from paquete1.informacion import valores
from paquete1.informacion2 import hacer_potencia
""" 
	para crear paquete, se debe crear siempre
	la carpeta "_init_.py"
""" 

for l in valores:
    r = hacer_potencia(l, 2)
    print("%s %d %s %d %s %.0f" % ("Valor", l, \
    	"elevado a la potencia", 2, \
    	"es igual a", r))
