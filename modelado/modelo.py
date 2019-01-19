class Operaciones(object):
    
    
	def __init__(self, listado): #Metodo constructor recibe listado y elemento a buscar
  
      
		self.listado_numeros = listado

    

	def busqueda_binaria(self,elem):
        
		self.elementoBusqueda = elem
        
		self.menor = 0
        
		self.superior = len(self.listado_numeros)-1
        
		self.pos = -1
        
		self.pm = int((menor + superior + 1 ) /2)

        
		while ((menor <= superior) and (pos == -1)):

            
			if (elementoBusqueda == self.listado_numeros[pm]):
                
				pos = pm

            
			if (elementoBusqueda < self.listado_numeros[pm]):
                
				superior = pm - 1
            
			else:  
                
				menor = pm + 1

            
			pm= int(menor + superior + 1) / 2
        
        
		return pos