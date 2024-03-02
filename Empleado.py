
from Fecha import Fecha

class Empleado:
   #Codigo para Determinar la Clase
   '''-----------------------------------------------------
   # Atributos
   -----------------------------------------------------'''
   
   nombres=''
   apellidos=''
   
   '''----------------------------------------------------
   1 = Masculino y 2 = Femenino
   -----------------------------------------------------'''
   
   numero_hijos = 0
   sexo=0
   salario=0
   
   '''-----------------------------------------------------
   # Asociaciones
   -----------------------------------------------------'''
   fechaNacimiento = Fecha()
   fechaIngreso = Fecha()
   
   '''-----------------------------------------------------
   # Medodos
   -----------------------------------------------------'''
   
   def __init__(self, nombres, apellidos, salario, sexo, numero_hijos=0):
      #Aqui va el codigo del metodo
      self.nombres = nombres
      self.apellidos = apellidos
      self.salario = salario
      self.sexo = sexo 
      self.numero_hijos = numero_hijos
   
   def CambiarSalario(self, nsalario):
      #Aqui va el codigo del metodo
      self.salario = nsalario
      return "su nuevo salario es: " + str(self.salario) 
   
   def ConsultarSalario(self):
      #Aqui va el codigo del metodo
      return (self.salario)
   
   def AumentoSalarial(self):
      #Aqui va el codigo del metodo
      aumento = 0.5
      self.salario *= (1 + aumento)
      return "Su nuevo salario es: " + str(self.salario)
   
   def DuplicarSalario(self):
      #Aqui va el codigo del metodo
      
      #Forma 1
      #nuevoSalario = self.salario*2
      #Self.salario = nuevoSalario
      
      #Forma 2 
       self.salario *= 2
   
   def CalcularSalarioAnual(self):
      #Aqui va el codigo del metodo
      
      #Forma 1
      SalarioAnual=self.salario*12
      return SalarioAnual
      
      #Forma 2
      #return self.salario*12
   
   def ConsultarDiaCumpleanios(self):
      #Aqui va el codigo del metodo
      return self.fechaNacimiento.ConsultarDia()
   
   def CalcularImpuestoAnual(self):
      #Aqui va el codigo del metodo
   
      #Forma 1
      total=self.CalcularSalarioAnual()
      total=total * (19.5/100)
      return total
      #Forma 2
      #return self.CalcularSalarioAnual()*0.195
   
   def InformarNumeroHijos(self):
	   #Informa el número de hijos que tiene un empleado.
      return self.nombres + " " + self.apellidos + "tiene" + str(self.numero_hijos) + "hijos."
   
   def CalcularAuxilioEducativo(self):
      #Calcula el auxilio educativo del empleado
      auxilio = 0.05 * self.salario * self.numero_hijos
      return "El auxilio educativo para " + self.nombres + " " + self.apellidos + " es: " + str(auxilio)
   
   def CalcularAuxilioEducativoParametrizado(self, porcentaje):
      #Calcula el auxilio educativo del empleado con porcentaje del salario
      auxilio = porcentaje * self.salario
      return "El auxilio educativo para " + self.nombres + " " + self.apellidos + " es: " + str(auxilio)
   
   def DiferenciaSalarial(self, otro_empleado):
      #Calcula la diferencia salarial respecto a otro empleado
      diferencia = self.salario - otro_empleado.salario
      return "La diferencia salarial entre " + self.nombres + " " +    self.apellidos + " y " + otro_empleado.nombres + " " + otro_empleado.apellidos + " es: " + str(diferencia)

