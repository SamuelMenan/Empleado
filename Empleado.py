class Empleado:
    #aqui va el codigo
    '''--------------------------------------
      # Atributos
    --------------------------------------'''
    
    nombres=''
    apellido=''

    '''--------------------------------------
      1 = Masculino y 2 = Femenino
    --------------------------------------'''
    
    sexo=0
    salario=0

    '''--------------------------------------
     # Medodos
    --------------------------------------'''

    def cambiarsalario(self, nsalario):
      #aqui va el codigo
      self.salario = nsalario
      return "su nuevo salario es: " + self.salario 

    def consultarsalario(self):
      #aqui va el codigo
      return self.salario

    def aumentosalarial(self):
      #aqui va el codigo
      aumento = self.salario = 0,5
      nsalario = self.salario*aumento
      self.salario = nsalario
      return "su nuevo salario es:" + self.salario 
 