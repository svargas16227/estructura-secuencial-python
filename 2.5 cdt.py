cantidad= float(input("Ingrese la cantidad invertida:"))
interes=float(input("Ingrese el porcentaje de interes (ej:0.05):"))
numDias=int(input("Ingrese el número de días:"))

intereses= cantidad*interes*numDias/360
descuento = interes * 0.07
total= cantidad +intereses-descuento
print("Intereses:", intereses)
print("Total a retirar:", total)

