from Empleado import Empleado

empleado1 = Empleado("Juan", "Perez", 1000000, 1)
empleado2 = Empleado("Pedro", "Martinez", 6000000, 1)
empleado3 = Empleado("Maria", "Benitez", 6000000, 1)

print(empleado1.ConsultarSalario())
print(empleado2.ConsultarSalario())
print(empleado3.ConsultarSalario())

diferencia_salario = empleado1.DiferenciaSalarial(empleado3)
print(diferencia_salario)