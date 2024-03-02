class Fecha:
    #aqui va el codigo
    '''----------------------------------------------------
    # Atributos
    ----------------------------------------------------'''
    
    dia=0
    mes=0
    anio=0

    
    '''----------------------------------------------------
    # Medodos
    ----------------------------------------------------'''

    def __init__(self, dia=0, mes=0, anio=0):
        #Aqui va el codigo del metodo
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def ConsultarDia(self):
        #Aqui va el codigo del metodo
        return self.dia
    
    def ConsultarMes(self):
        #Aqui va el codigo del metodo
        return self.mes

    def ConsultarAnio(self):
        #Aqui va el codigo del metodo
        return self.anio