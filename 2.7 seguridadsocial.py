salario=float(input("Ingrese su salario mensual:"))
salud= salario*0.04
pension= salario*0.04
descuento=salud+pension
neto= salario-descuento
print(" Descuento de salud:", salud)
print("Descuento pensión:", pension)
print("Salario neto:", neto)

