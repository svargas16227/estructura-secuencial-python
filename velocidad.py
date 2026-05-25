x = float(input("Ingrese la distancia: "))
t = float(input("Ingrese el tiempo: "))

if t != 0:
    v = x / t
    print("La velocidad es:", v)
else:
    print("Error: el tiempo no puede ser 0")