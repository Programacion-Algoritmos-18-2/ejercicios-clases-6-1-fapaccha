from paquete_archivos.miarchivo import MiArchivo
from modelado.modelo import *

m = MiArchivo() # objeto para leer el archivo

lista = m.obtener_informacion()
lista = [l.split(",") for l in lista]
lista2 = []

for i in lista: 
	for j in i: 
		a = int(j) 
		lista2.append(a)

operacion = Operaciones(lista2)

print (operacion)
a = operacion.busqueda_binaria(33) 

print("La posicion del numero buscado es: %s"%a)

m.cerrar_archivo()
