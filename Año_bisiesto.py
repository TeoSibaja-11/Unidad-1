Año = int(input("Ingresa un año: "))
if (Año % 4 == 0 and Año % 100 != 0) or (Año % 400 == 0):
    print(f"El año {Año} es un año bisiesto.")
else:
    print(f"El año {Año} no es un año bisiesto.")
